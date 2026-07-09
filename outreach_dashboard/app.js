/**
 * ═══════════════════════════════════════════════════════
 * app.js — Interactive Logic & OSM Data Loader
 * Internship Command Center for Haroun Jaafar
 * ═══════════════════════════════════════════════════════
 */

let db = []; // Merged database of curated (COMPANIES) and OSM parsed companies
let statuses = JSON.parse(localStorage.getItem('icc_statuses') || '{}');
let selectedId = null;
let markers = {};
let map;
let activeFilter = 'all';
let searchQuery = '';

// Set default statuses for some companies if not present
COMPANIES.forEach(c => {
  if (!statuses[c.id]) {
    statuses[c.id] = 'new';
  }
});
saveStatuses();

function saveStatuses() {
  localStorage.setItem('icc_statuses', JSON.stringify(statuses));
}

function getStatus(id) { return statuses[id] || 'new'; }

// ─── MAP INITIALIZATION ───
function initMap() {
  // Center on Europe / North Italy
  map = L.map('map', { zoomControl: false }).setView([46.0, 10.0], 5);
  L.control.zoom({ position: 'bottomright' }).addTo(map);

  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '© OpenStreetMap © CARTO',
    subdomains: 'abcd',
    maxZoom: 19
  }).addTo(map);

  // Load curated first
  loadDatabase(COMPANIES);
  
  // Auto-select first company on boot to ensure the right panel is visible
  if (COMPANIES.length > 0) {
    selectCompany(COMPANIES[0].id);
  }
  
  // Load OSM data immediately
  loadOsmData();
  
  // Auto-refresh every 60 seconds
  setInterval(loadOsmData, 60000);

  // Risolve il bug delle dimensioni iniziali con Flexbox
  setTimeout(() => {
    if (map) map.invalidateSize();
  }, 300);

  // Aggiorna le dimensioni quando l'utente ridimensiona o zooma
  window.addEventListener('resize', () => {
    if (map) map.invalidateSize();
  });
}

function loadOsmData() {
  console.log("Polling for new companies database update...");
  fetch('osm_companies.json?t=' + new Date().getTime()) // Query string prevents browser caching
    .then(response => {
      if (!response.ok) throw new Error('OSM data not generated yet');
      return response.json();
    })
    .then(osmData => {
      const mappedOsm = osmData.map((c, index) => {
        const id = 'osm_' + index;
        return {
          id: id,
          name: c.name,
          city: c.city,
          country: c.country,
          coords: c.coords,
          sector: c.sector,
          category: c.sector === 'Finance' ? 'Finance' : 'Data',
          strategy: 'Global',
          size: 'Medium',
          rating: 4.0,
          contactEmail: c.email,
          careersUrl: c.careers,
          description: c.note,
          culture: 'Rilevato tramite OpenStreetMap. Questa azienda si trova lungo la rotta di ricerca geografica.',
          pros: ['Presenza locale reale', 'Contatto diretto disponibile o ricercabile'],
          cons: ['Dettagli di stage non pubblicati'],
          openPositions: [
            {
              title: `${c.sector} / IT Internship (Erasmus+)`,
              type: "Speculative / Traineeship",
              skills_required: c.sector === 'Finance' ? ["Excel", "Finance Basics"] : ["Python", "SQL", "IT Basics"],
              skills_nice: ["Data Analysis", "English"],
              your_fit: c.fit === 'high' ? 85 : 70,
              note: "Candidatura spontanea consigliata usando il modello Erasmus+ a costo zero per l'azienda."
            }
          ],
          skillGaps: [],
          emailSubject: `Traineeship Inquiry (Erasmus+ Program) — ${c.sector} & Data Student`,
          emailTemplate: generateTemplate(c)
        };
      });
      
      const combined = [...COMPANIES, ...mappedOsm];
      
      // Update database and map without losing current selection
      const currentSelected = selectedId;
      loadDatabase(combined);
      if (currentSelected) {
        selectedId = currentSelected;
        // Keep active class in list
        const activeCard = document.getElementById(`ccard-${selectedId}`);
        if (activeCard) activeCard.classList.add('active');
      }
      
      console.log(`Aggiornato! ${combined.length} aziende totali.`);
    })
    .catch(err => {
      console.log("OSM database loading error / not ready: ", err);
    });
}

function generateTemplate(c) {
  return `Dear ${c.name} Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I am looking for a 2-month internship starting in January 2027 in a ${c.sector || 'data/business'} analytics or IT-support role.

My placement is fully funded by the Erasmus+ Traineeship program, meaning my university covers my stipend and insurance. There are no salary or administrative costs for your company. I also have secured housing ready, making relocation straightforward.

My background bridges IT and economics: I completed an IT high school diploma before starting my business degree. I recently built a quantitative financial data pipeline in Python that automates data ingestion into PostgreSQL, runs portfolio optimization, and simulates risk scenarios using Monte Carlo methods: github.com/RealHarounJ/quant-data-pipeline

I would love to support your team and gain practical experience. I've attached my CV for your review.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`;
}

function loadDatabase(data) {
  // Clear existing markers
  for (let id in markers) {
    map.removeLayer(markers[id]);
  }
  markers = {};
  db = data;
  
  // Populate markers
  db.forEach(c => {
    addMarker(c);
  });
  
  renderList();
  updateStats();
}

function statusColor(s) {
  return { new: '#3b82f6', sent: '#f59e0b', accepted: '#10b981', rejected: '#ef4444' }[s] || '#3b82f6';
}
function statusLabel(s) {
  return { new: 'Non contattata', sent: 'Email inviata', accepted: 'Accettata!', rejected: 'Rifiutata' }[s] || s;
}

function addMarker(c) {
  const status = getStatus(c.id);
  const color = statusColor(status);
  const isUrgent = c.id === 'blackrock'; // Urgent marker

  const m = L.circleMarker(c.coords, {
    radius: isUrgent ? 13 : 8,
    fillColor: color,
    color: isUrgent ? '#fbbf24' : 'rgba(255,255,255,0.3)',
    weight: isUrgent ? 3 : 1,
    opacity: 1,
    fillOpacity: 0.85
  }).addTo(map);

  m.bindPopup(`
    <div class="popup-inner">
      <div class="popup-name">${isUrgent ? '⚡ ' : ''}${c.name}</div>
      <div class="popup-city">📍 ${c.city}</div>
      <div style="font-size:10px;color:var(--text-3);margin-bottom:6px;">Settore: ${c.sector}</div>
      <button class="popup-open-btn" onclick="selectCompany('${c.id}')">Apri Scheda</button>
    </div>
  `, { maxWidth: 220 });

  m.on('click', () => {
    selectCompany(c.id);
  });

  markers[c.id] = m;
}

function refreshMarker(id) {
  if (!markers[id]) return;
  markers[id].setStyle({ fillColor: statusColor(getStatus(id)) });
}

// ─── SIDEBAR LIST & FILTERING ───
function filteredCompanies() {
  const q = searchQuery.toLowerCase();
  return db.filter(c => {
    const matchQ = !q || c.name.toLowerCase().includes(q) || c.city.toLowerCase().includes(q) || c.sector.toLowerCase().includes(q);
    let matchF = true;
    if (activeFilter === 'Maastricht') matchF = c.city.toLowerCase().includes('maastricht') || c.city.toLowerCase().includes('heerlen');
    else if (activeFilter === 'Global') matchF = c.strategy === 'Global';
    else if (activeFilter === 'Finance') matchF = c.category === 'Finance' || c.sector === 'Finance';
    else if (activeFilter === 'Data') matchF = c.category === 'Data' || c.sector === 'Data' || c.sector === 'Tech';
    else if (activeFilter === 'urgent') matchF = c.id === 'blackrock';
    return matchQ && matchF;
  });
}

function renderList() {
  const list = document.getElementById('company-list');
  const companies = filteredCompanies();
  list.innerHTML = '';

  if (companies.length === 0) {
    list.innerHTML = `<div class="empty-state"><div class="empty-state-icon">🔍</div><div class="empty-state-text">Nessuna azienda trovata</div></div>`;
    return;
  }

  companies.slice(0, 150).forEach(c => { // Limit to 150 items for DOM performance
    const status = getStatus(c.id);
    const isUrgent = c.id === 'blackrock';
    const div = document.createElement('div');
    div.className = `ccard${selectedId === c.id ? ' active' : ''}`;
    div.id = `ccard-${c.id}`;
    div.innerHTML = `
      <div class="ccard-top">
        <div>
          <div class="ccard-name">${isUrgent ? '⚡ ' : ''}${c.name}</div>
          <div class="ccard-info">
            <span>📍 ${c.city}</span>
            <span>📂 ${c.sector}</span>
          </div>
        </div>
        <span class="badge badge-${status}">${statusLabel(status)}</span>
      </div>
    `;
    div.addEventListener('click', () => {
      selectCompany(c.id);
      map.flyTo(c.coords, 12, { animate: true, duration: 1.2 });
    });
    list.appendChild(div);
  });

  if (companies.length > 150) {
    const moreDiv = document.createElement('div');
    moreDiv.style.cssText = 'text-align:center;font-size:11px;color:var(--text-3);padding:10px;';
    moreDiv.textContent = `... e altre ${companies.length - 150} aziende. Usa i filtri o la ricerca per trovarle.`;
    list.appendChild(moreDiv);
  }

  updateStats();
}

function updateStats() {
  document.getElementById('stat-total').textContent = db.length;
  document.getElementById('stat-sent').textContent = db.filter(c => getStatus(c.id) === 'sent').length;
  document.getElementById('stat-ok').textContent = db.filter(c => getStatus(c.id) === 'accepted').length;
  document.getElementById('stat-no').textContent = db.filter(c => getStatus(c.id) === 'rejected').length;
  // Aggiorna stats mobile topbar
  const mobTotal = document.getElementById('mob-total');
  const mobOk = document.getElementById('mob-ok');
  if (mobTotal) mobTotal.textContent = db.length;
  if (mobOk) mobOk.textContent = db.filter(c => getStatus(c.id) === 'accepted').length;
}

// ─── SELECTION & DETAIL PANEL ───
function selectCompany(id) {
  selectedId = id;
  renderList();
  const c = db.find(x => x.id === id);
  if (!c) return;

  map.closePopup();

  document.getElementById('d-name').textContent = c.name;
  const meta = document.getElementById('d-meta');
  meta.innerHTML = `
    <span class="d-pill">📍 ${c.city}</span>
    <span class="d-pill">📂 ${c.sector}</span>
    <span class="d-pill">🏢 ${c.size || 'Medium'}</span>
  `;

  document.getElementById('d-desc').textContent = c.description || '';
  document.getElementById('d-culture').textContent = c.culture || '';

  const r = c.rating || 4.0;
  const fullStars = Math.floor(r);
  let starsHtml = '★'.repeat(fullStars) + '☆'.repeat(5 - fullStars);
  document.getElementById('d-stars').textContent = starsHtml;
  document.getElementById('d-rating-num').textContent = r.toFixed(1);

  const prosConsEl = document.getElementById('d-pros-cons');
  prosConsEl.innerHTML = `
    <div class="pros-box">
      <strong>✅ Pro</strong>
      ${(c.pros || ['Opportunità di crescita']).map(p => `• ${p}`).join('<br>')}
    </div>
    <div class="cons-box">
      <strong>⚠️ Contro</strong>
      ${(c.cons || ['Richiede spirito d\'iniziativa']).map(con => `• ${con}`).join('<br>')}
    </div>
  `;

  const link = document.getElementById('d-careers-link');
  link.href = c.careersUrl || '#';
  document.getElementById('d-careers-url').textContent = c.careersUrl || 'N/A';

  document.getElementById('d-status-select').value = getStatus(id);

  // Positions
  const posList = document.getElementById('d-positions-list');
  if (c.openPositions && c.openPositions.length) {
    posList.innerHTML = c.openPositions.map(pos => `
      <div class="position-card">
        <div class="pos-title">${pos.title}</div>
        <div class="pos-meta">
          <span>📋 ${pos.type}</span>
          <span>Fit: <strong style="color:${fitColor(pos.your_fit)}">${pos.your_fit}%</strong></span>
        </div>
        ${pos.note ? `<div style="font-size:11px;color:var(--text-3);margin-bottom:8px;font-style:italic;">${pos.note}</div>` : ''}
        <div class="pos-fit">
          ${(pos.skills_required || []).map(s => `<span class="skill-tag ${CV.skills_have.some(h => h.toLowerCase().includes(s.toLowerCase())) ? 'skill-have' : 'skill-missing'}">${s}</span>`).join('')}
          ${(pos.skills_nice || []).map(s => `<span class="skill-tag skill-learn">${s}</span>`).join('')}
        </div>
      </div>
    `).join('');
  } else {
    posList.innerHTML = `<div class="empty-state"><div class="empty-state-icon">📭</div><div class="empty-state-text">Candidatura diretta consigliata.</div></div>`;
  }

  // Skill Gaps
  const bestFit = c.openPositions && c.openPositions.length ? Math.max(...c.openPositions.map(p => p.your_fit)) : 75;
  const fitBar = document.getElementById('d-fit-bar');
  document.getElementById('d-fit-pct').textContent = bestFit + '%';
  fitBar.style.width = bestFit + '%';
  fitBar.style.background = fitColor(bestFit);

  const gapsList = document.getElementById('d-gaps-list');
  gapsList.innerHTML = `
    <div class="sec-title">Risorse consigliate per questa azienda</div>
    <div style="font-size:12px;color:var(--text-2);margin-bottom:12px;">Prepara le tue competenze per il colloquio o lo stage:</div>
    <div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px;">
      <span class="skill-tag skill-have">Python</span>
      <span class="skill-tag skill-have">SQL</span>
      <span class="skill-tag skill-learn">Bloomberg BMC</span>
      <span class="skill-tag skill-learn">Excel Finance</span>
    </div>
  `;

  // Email Builder
  document.getElementById('d-email-to').textContent = c.contactEmail || 'portal-only';
  document.getElementById('d-email-subject').value = c.emailSubject || `Traineeship Inquiry (Erasmus+) — Haroun Jaafar`;
  document.getElementById('d-email-body').value = c.emailTemplate || '';

  document.getElementById('detail-panel').classList.add('open');
  activateTab('overview');
  
  // Forza Leaflet a ricalcolare le dimensioni dopo che il pannello si è aperto
  setTimeout(() => {
    if (map) map.invalidateSize();
  }, 400);

  // Su mobile: chiudi la sidebar e apri il pannello
  if (window.innerWidth <= 768) {
    const mob_sidebar = document.querySelector('.sidebar');
    const mob_btn = document.getElementById('mobile-menu-btn');
    if (mob_sidebar) mob_sidebar.classList.remove('mobile-open');
    if (mob_btn) mob_btn.textContent = '☰';
  }
}

function fitColor(pct) {
  if (pct >= 80) return '#10b981';
  if (pct >= 65) return '#f59e0b';
  return '#ef4444';
}

function activateTab(name) {
  document.querySelectorAll('.dtab').forEach(t => t.classList.toggle('active', t.dataset.tab === name));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.toggle('active', p.id === `tab-${name}`));
}

// ─── EVENT LISTENERS ───
document.querySelectorAll('.dtab').forEach(tab => {
  tab.addEventListener('click', () => activateTab(tab.dataset.tab));
});

document.getElementById('search-input').addEventListener('input', e => {
  searchQuery = e.target.value;
  renderList();
});

document.getElementById('filter-chips').addEventListener('click', e => {
  const chip = e.target.closest('.chip');
  if (!chip) return;
  document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
  chip.classList.add('active');
  activeFilter = chip.dataset.filter;
  renderList();
});

document.getElementById('d-status-select').addEventListener('change', e => {
  if (!selectedId) return;
  statuses[selectedId] = e.target.value;
  saveStatuses();
  refreshMarker(selectedId);
  renderList();
  showToast(`Stato aggiornato: ${statusLabel(e.target.value)}`);
});

document.getElementById('d-close-btn').addEventListener('click', () => {
  document.getElementById('detail-panel').classList.remove('open');
  selectedId = null;
  renderList();
});

document.getElementById('btn-copy-email').addEventListener('click', () => {
  const c = db.find(x => x.id === selectedId);
  if (!c || c.contactEmail === 'portal-only') {
    showToast('❌ Solo candidatura via portale.');
    return;
  }
  navigator.clipboard.writeText(c.contactEmail).then(() => showToast('✅ Email copiata!'));
});

document.getElementById('btn-copy-all').addEventListener('click', () => {
  const subj = document.getElementById('d-email-subject').value;
  const body = document.getElementById('d-email-body').value;
  navigator.clipboard.writeText(`Oggetto: ${subj}\n\n${body}`).then(() => showToast('✅ Testo completo copiato!'));
});

document.getElementById('btn-open-gmail').addEventListener('click', () => {
  const c = db.find(x => x.id === selectedId);
  if (!c) return;
  const to = c.contactEmail !== 'portal-only' ? encodeURIComponent(c.contactEmail) : '';
  const subj = encodeURIComponent(document.getElementById('d-email-subject').value);
  const body = encodeURIComponent(document.getElementById('d-email-body').value);
  const url = `https://mail.google.com/mail/?view=cm&fs=1&to=${to}&su=${subj}&body=${body}`;
  window.open(url, '_blank');
});

// Toast
let toastTimer;
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2500);
}

// ─── MOBILE LOGIC ───
const mob_menuBtn = document.getElementById('mobile-menu-btn');
const mob_sidebar = document.querySelector('.sidebar');

if (mob_menuBtn && mob_sidebar) {
  mob_menuBtn.addEventListener('click', () => {
    const isOpen = mob_sidebar.classList.toggle('mobile-open');
    mob_menuBtn.textContent = isOpen ? '✕' : '☰';
  });
}

// Startup
window.addEventListener('load', () => {
  initMap();
});
