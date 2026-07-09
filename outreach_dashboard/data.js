/**
 * ═══════════════════════════════════════════════════════
 * data.js — Complete Company & Resource Database
 * Internship Command Center for Haroun Jaafar
 * ═══════════════════════════════════════════════════════
 */

// ─── HAROUN'S CV PROFILE (for email generation) ───
const CV = {
  name: "Haroun Jaafar",
  email: "haroun.jaafar@studenti.univpm.it",
  phone: "+39 3515246876",
  linkedin: "linkedin.com/in/harounjaafar",
  github: "github.com/RealHarounJ",
  university: "UNIVPM — Università Politecnica delle Marche",
  degree: "Digital Economics and Business (Economics, BSc)",
  year: "3rd year (graduating 2026)",
  erasmus: "Erasmus+ Traineeship Program (fully funded — no salary cost to host)",
  housing: "Housing in Maastricht already secured (friend lives there)",
  period: "January 2027 onwards, ~2 months",
  skills_have: ["Python", "SQL", "PostgreSQL", "Docker", "Apache Airflow", "Data Analysis", "Excel", "Financial Modeling Basics"],
  project: "quant-data-pipeline (automated ETL: market data → PostgreSQL → Markowitz optimization + 10,000 Monte Carlo paths | Airflow + Docker): github.com/RealHarounJ/quant-data-pipeline",
  learning: ["Google Data Analytics Certificate (Coursera)", "Bloomberg Market Concepts (BMC)", "PCAP Python Certification (edube.org / Python Institute)", "Power BI (Microsoft Learn)", "SQL Mode Analytics Tutorial"],
  summary: "Digital Economics student with an IT high school background, strong Python/SQL data skills, and a published finance data project on GitHub. Looking for a 2-month Erasmus+ funded traineeship (no cost to host)."
};

// ─── LEARNING RESOURCES DATABASE ───
const RESOURCES = {
  free: [
    {
      id: "google_python",
      name: "Google's Python Class",
      provider: "Google Developers",
      url: "https://developers.google.com/edu/python/",
      cost: "FREE",
      duration: "~10 hours",
      cert: false,
      tags: ["Python", "Basics"],
      recognition: 3,
      desc: "Google's original internal Python training. Hands-on exercises with real code. Best Python starter."
    },
    {
      id: "edube_pcap",
      name: "Python Essentials 1 & 2",
      provider: "Edube.org (Python Institute)",
      url: "https://edube.org/",
      cost: "FREE",
      duration: "~60 hours",
      cert: false,
      tags: ["Python", "PCAP Prep"],
      recognition: 4,
      desc: "The official free preparation course for the PCEP and PCAP certification exams by the Python Institute."
    },
    {
      id: "sqlzoo",
      name: "SQLZoo Interactive SQL",
      provider: "SQLZoo",
      url: "https://sqlzoo.net/",
      cost: "FREE",
      duration: "~15 hours",
      cert: false,
      tags: ["SQL", "Database"],
      recognition: 3,
      desc: "Browser-based SQL exercises from SELECT to window functions. Universally recommended by EU data hiring managers."
    },
    {
      id: "mode_sql",
      name: "Mode SQL Tutorial",
      provider: "Mode Analytics",
      url: "https://mode.com/sql-tutorial/",
      cost: "FREE",
      duration: "~20 hours",
      cert: false,
      tags: ["SQL", "Advanced"],
      recognition: 3,
      desc: "Real-world datasets in an in-browser SQL editor. Basic → Advanced with subqueries and window functions."
    },
    {
      id: "powerbi_learn",
      name: "Power BI Learning Path",
      provider: "Microsoft Learn",
      url: "https://learn.microsoft.com/en-us/training/paths/power-bi-first-steps/",
      cost: "FREE",
      duration: "~20 hours",
      cert: false,
      tags: ["Power BI", "Data Visualization"],
      recognition: 4,
      desc: "Full PL-300 curriculum for free. Power BI is the dominant BI tool in European corporate finance and banking."
    },
    {
      id: "tableau_free",
      name: "Tableau Public + Free Training",
      provider: "Tableau (Salesforce)",
      url: "https://www.tableau.com/learn/training",
      cost: "FREE",
      duration: "~20 hours",
      cert: false,
      tags: ["Tableau", "Data Visualization"],
      recognition: 4,
      desc: "Free training videos + free Tableau Public platform. Build and publish dashboards for your portfolio."
    },
    {
      id: "cfi_free",
      name: "CFI Free Course Library",
      provider: "Corporate Finance Institute",
      url: "https://corporatefinanceinstitute.com/resources/free-courses/",
      cost: "FREE",
      duration: "~3-4 hrs/course",
      cert: true,
      tags: ["Finance", "Excel", "Certificate"],
      recognition: 4,
      desc: "Includes Excel for Finance, Reading Financial Statements, Accounting Fundamentals. Digital completion certificates per course."
    },
    {
      id: "bloomberg_bmc",
      name: "Bloomberg Market Concepts (BMC)",
      provider: "Bloomberg for Education",
      url: "https://portal.bloombergforeducation.com/",
      cost: "FREE (via university email)",
      duration: "~9 hours",
      cert: true,
      tags: ["Finance", "Markets", "Certificate", "⭐ TOP PRIORITY"],
      recognition: 5,
      desc: "The #1 most recognized finance certificate in EU banking and asset management hiring. Check if your UNIVPM email gives free access first!"
    },
    {
      id: "py4e",
      name: "Python for Everybody (audit)",
      provider: "University of Michigan / Coursera",
      url: "https://www.py4e.com/",
      cost: "FREE (audit)",
      duration: "~50 hours",
      cert: false,
      tags: ["Python", "Beginner"],
      recognition: 3,
      desc: "100% of the content available free at py4e.com. Pay only if you want the official Coursera certificate."
    }
  ],
  paid: [
    {
      id: "pcep",
      name: "PCEP™ — Certified Entry-Level Python Programmer",
      provider: "Python Institute / OpenEDG",
      url: "https://pythoninstitute.org/pcep",
      cost: "$69 USD",
      duration: "45-min exam (prep: ~30-60 hrs)",
      cert: true,
      tags: ["Python", "Entry-Level Cert"],
      recognition: 3,
      desc: "Official Python Institute certification. Study free with Edube.org Python Essentials 1. ⚠️ PCEP-30-02 retires Aug 31 2026."
    },
    {
      id: "pcap",
      name: "PCAP™ — Certified Associate Python Programmer",
      provider: "Python Institute / OpenEDG",
      url: "https://pythoninstitute.org/pcap",
      cost: "$295 USD",
      duration: "65-min exam (prep: ~60-100 hrs)",
      cert: true,
      tags: ["Python", "Associate Cert"],
      recognition: 4,
      desc: "Intermediate Python cert. Pearson VUE delivery across Europe. Free prep via Edube.org Python Essentials 2."
    },
    {
      id: "google_da",
      name: "Google Data Analytics Professional Certificate",
      provider: "Google / Coursera",
      url: "https://www.coursera.org/professional-certificates/google-data-analytics",
      cost: "~$49/month (2-3 months)",
      duration: "~180 hours",
      cert: true,
      tags: ["Data Analysis", "Google Cert", "ECTS Credit"],
      recognition: 4,
      desc: "Covers SQL, R, Tableau, spreadsheets. Now ECTS credit-recommended in EU. Google brand widely trusted by EU employers."
    },
    {
      id: "ibm_ds",
      name: "IBM Data Science Professional Certificate",
      provider: "IBM / Coursera",
      url: "https://www.coursera.org/professional-certificates/ibm-data-science",
      cost: "~$49/month (4 months)",
      duration: "~150 hours",
      cert: true,
      tags: ["Data Science", "Python", "ML", "ECTS Credit"],
      recognition: 4,
      desc: "More technical than Google cert. Python, SQL, ML, AI modules. ECTS credit-recommended. Good for EU fintech data roles."
    },
    {
      id: "cfa_if",
      name: "CFA Investment Foundations® Certificate",
      provider: "CFA Institute",
      url: "https://www.cfainstitute.org/en/programs/investment-foundations",
      cost: "$79 (students) / $350 standard",
      duration: "~60-100 hours",
      cert: true,
      tags: ["Finance", "CFA", "⭐ High Value"],
      recognition: 5,
      desc: "CFA Institute brand. Covers investments, portfolio management, ethics. Student price = exceptional ROI for EU finance applications."
    },
    {
      id: "fmva",
      name: "FMVA® Financial Modeling & Valuation Analyst",
      provider: "Corporate Finance Institute (CFI)",
      url: "https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/",
      cost: "$497/year (Self-Study)",
      duration: "~200 hours",
      cert: true,
      tags: ["Financial Modeling", "Excel", "IB", "⭐ Top Finance Cert"],
      recognition: 5,
      desc: "The gold standard for self-taught financial modelers targeting EU investment banking, PE, and asset management. 3-statement, DCF, LBO, M&A."
    },
    {
      id: "wsp_premium",
      name: "Wall Street Prep — Self-Study Premium Package",
      provider: "Wall Street Prep",
      url: "https://www.wallstreetprep.com/self-study-programs/",
      cost: "$499 (one-time)",
      duration: "~120 hours",
      cert: true,
      tags: ["Financial Modeling", "IB Training", "⭐ Top Finance Cert"],
      recognition: 5,
      desc: "Used by Goldman Sachs and JPMorgan to train new hires. One-time payment. Best for IB/PE internship applicants in EU."
    },
    {
      id: "dp900",
      name: "Azure Data Fundamentals (DP-900)",
      provider: "Microsoft",
      url: "https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/",
      cost: "$99 (exam fee)",
      duration: "~25 hours study",
      cert: true,
      tags: ["Cloud", "Azure", "Microsoft Cert"],
      recognition: 4,
      desc: "Dominant cloud platform in EU enterprise. Study materials 100% free on Microsoft Learn. Watch for free voucher events."
    },
    {
      id: "pl300",
      name: "Power BI Data Analyst Associate (PL-300)",
      provider: "Microsoft",
      url: "https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/",
      cost: "$165 (exam fee)",
      duration: "~50 hours study",
      cert: true,
      tags: ["Power BI", "Microsoft Cert", "BI"],
      recognition: 5,
      desc: "Power BI is #1 BI tool in EU corporate finance and banking. Free study on Microsoft Learn. Free annual renewal after cert."
    },
    {
      id: "tableau_cert",
      name: "Tableau Desktop Foundations Cert",
      provider: "Salesforce / Tableau",
      url: "https://www.tableau.com/learn/certification",
      cost: "$75 (exam fee)",
      duration: "~60-min exam",
      cert: true,
      tags: ["Tableau", "Visualization"],
      recognition: 4,
      desc: "Official Salesforce certification. Pearson VUE delivery across Europe. Complement with a Tableau Public portfolio."
    }
  ]
};

// ─── COMPANY DATABASE ───
const COMPANIES = [
  // ══════════════════════════════════════════════════════
  // STRATEGIA 1: AREA MAASTRICHT/EUREGIO
  // ══════════════════════════════════════════════════════
  {
    id: "liof",
    name: "LIOF",
    city: "Maastricht, Netherlands",
    country: "NL",
    coords: [50.8483, 5.6889],
    sector: "Investment / Regional Development",
    size: "Medium",
    employees: "~250",
    strategy: "Maastricht",
    category: "Finance",
    rating: 4.0,
    contactEmail: "hr@liof.nl",
    careersUrl: "https://liof.nl/werken-bij",
    description: "LIOF (Limburgse Ontwikkelingsmaatschappij) is the regional development agency for the Province of Limburg. They fund and support scale-ups, startups, and SMEs in the Euregio (NL/BE/DE border region) through loans, equity, and business development programs. They analyze regional economic data and support innovation clusters.",
    culture: "Collaborative, mission-driven environment. Work directly with founders and investors. The team is relatively small which means interns get real responsibility. Dutch-speaking workplace but English is used in many international projects.",
    pros: ["Right in Maastricht city centre (walk/bike to work)", "Real responsibility from day 1", "Erasmus+ funded internship = no cost to LIOF", "Work with startups and regional data", "Perfect size for genuine learning"],
    cons: ["Primarily Dutch-speaking", "Not a paid internship (Erasmus+ grant only)", "Limited international brand recognition vs big banks"],
    openPositions: [
      {
        title: "Business / Data Analysis Trainee",
        type: "Traineeship (Erasmus+)",
        skills_required: ["Excel", "Data Analysis", "Business Acumen", "Report Writing"],
        skills_nice: ["Python", "SQL", "Power BI"],
        your_fit: 88,
        note: "No public posting — direct cold outreach recommended. They regularly host Erasmus trainees."
      }
    ],
    skillGaps: [],
    emailSubject: "Traineeship inquiry: Economics & Data student looking for an internship (Jan 2027)",
    emailTemplate: `Hi LIOF HR Team,

I hope you're doing well.

My name is Haroun, and I'm a third-year student in "Digital Economics and Business" at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027 in a business analysis or data analytics role, and I wanted to check if you have any availability.

To give you some quick context, the internship would be fully funded by my university through the Erasmus+ Traineeship program — so there are no salary or administrative costs for LIOF, just a simple Host Agreement to sign.

Also, I already have housing sorted out in Maastricht, so commuting to your office won't be an issue at all.

My background is a mix of tech and business: I finished an IT high school diploma before starting my economics degree. I'm comfortable using Python and SQL to handle data, and I recently built a portfolio data pipeline using PostgreSQL, Docker, and Apache Airflow to run Markowitz optimizations and Monte Carlo simulations. The code is public on my GitHub: github.com/RealHarounJ/quant-data-pipeline

On top of that, I'm currently working through the Bloomberg Market Concepts certificate (Bloomberg's official finance markets credential) and the Google Data Analytics Certificate on Coursera — resources used by the top professionals in the industry.

I'd love to help your team analyze local startup data or support your regional investment projects. I've attached my CV for details.

Would you be open to a quick call sometime next week?

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
linkedin.com/in/harounjaafar | github.com/RealHarounJ`
  },
  {
    id: "apg",
    name: "APG",
    city: "Heerlen, Netherlands",
    country: "NL",
    coords: [50.8872, 5.9754],
    sector: "Asset Management / Pension Funds",
    size: "Large",
    employees: "~3,000",
    strategy: "Maastricht",
    category: "Finance",
    rating: 3.9,
    contactEmail: "apg@magnitglobal.com",
    careersUrl: "https://werkenbijapg.nl/",
    description: "APG manages over €600 billion in pension assets, making it one of the largest asset managers in the world. Their Heerlen headquarters houses data science, AI, risk management, and quantitative investment research teams. They are actively investing in data-driven investment processes and alternative data analysis.",
    culture: "Professional and structured, typical of large Dutch institutional finance. Strong focus on responsible investing (ESG). Excellent internal learning programs and formal mentorship for trainees. English widely spoken in technical teams.",
    pros: ["One of the largest pension managers globally — elite brand", "Cutting-edge data science and AI team in Heerlen", "15 minutes from Maastricht by train", "Structured internship programs with mentors", "ESG focus aligns with macro trends"],
    cons: ["Large bureaucratic organization — less flexibility", "Formal and process-heavy environment", "Competitive for formal spots — cold outreach needed"],
    openPositions: [
      {
        title: "Data Analytics / Quantitative Research Trainee",
        type: "Traineeship",
        skills_required: ["Python", "SQL", "Data Analysis", "Statistics"],
        skills_nice: ["Machine Learning", "R", "Bloomberg"],
        your_fit: 82,
        note: "Active trainee programs. Check werkenbijapg.nl for current openings or contact directly."
      }
    ],
    skillGaps: ["Bloomberg Terminal basics → study Bloomberg Market Concepts (BMC) FREE"],
    emailSubject: "Internship inquiry: Digital Economics student with IT background (Jan 2027)",
    emailTemplate: `Dear APG Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year Economics and Business student at UNIVPM (Italy), focusing on Digital Economics. I'm looking for a 2-month internship starting in January 2027, and I'm very interested in joining your data analytics, risk, or portfolio operations teams in Heerlen.

The internship is fully funded by my university through the Erasmus+ Traineeship program, so it won't cost APG anything in terms of salary. I've also already secured my accommodation in Maastricht, so I can commute daily to the Heerlen office without any housing issues.

I have a hybrid background: before studying economics, I completed an IT high school diploma. To bridge my IT skills with finance, I recently built an automated portfolio data pipeline in Python. The system pulls market prices into a PostgreSQL database, calculates covariance matrices for a basic Markowitz optimization, and runs 10,000 Monte Carlo paths (GBM) to forecast risk. The entire project is containerized using Docker and scheduled with Apache Airflow. You can see the code here: github.com/RealHarounJ/quant-data-pipeline

I'm also currently working through the Bloomberg Market Concepts (BMC) certificate and the Google Data Analytics Certificate on Coursera — the same resources used by quantitative analysts across the industry.

I'd love to support your data teams while learning how institutional asset management works at APG's scale. I've attached my CV for your review.

I would appreciate the chance to discuss if there is a project I could contribute to.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "axians",
    name: "Axians NL",
    city: "Heerlen, Netherlands",
    country: "NL",
    coords: [50.8800, 5.9600],
    sector: "IT Consulting / Data & BI",
    size: "Large",
    employees: "~1,500 (NL)",
    strategy: "Maastricht",
    category: "Data",
    rating: 3.8,
    contactEmail: "jasper.both@axians.com",
    careersUrl: "https://werkenbijaxians.nl/",
    description: "Axians is a global ICT solutions brand (part of VINCI Energies) with a strong Netherlands footprint in Heerlen. Their data & analytics division builds BI dashboards, data warehouses, ETL pipelines, and cloud solutions for large corporate clients across the Euregio region.",
    culture: "Consultancy culture — fast-paced, client-oriented. Interns work directly on billable client projects. Strong technical mentorship from senior data engineers and BI consultants. English is used in client work, Dutch in daily office life.",
    pros: ["Work on real client data projects from day 1", "Learn Power BI and modern data stack in practice", "Heerlen office (15 min from Maastricht)", "VINCI Energies backing = stability", "Strong technical mentorship"],
    cons: ["Consultancy pace can be intense", "Primarily Dutch-speaking office culture", "Client confidentiality limits portfolio building"],
    openPositions: [
      {
        title: "Data Analytics / BI Intern",
        type: "Traineeship",
        skills_required: ["SQL", "Data Visualization", "Analytical Thinking"],
        skills_nice: ["Power BI", "Python", "Azure"],
        your_fit: 80,
        note: "Axians NL regularly hosts students. Direct outreach to team leaders (Jasper Both, Bert van Oort) is the best approach."
      }
    ],
    skillGaps: ["Power BI → FREE on Microsoft Learn", "Azure basics → DP-900 ($99 exam)"],
    emailSubject: "Economics & IT student looking for a Data Analytics internship (Jan 2027)",
    emailTemplate: `Hi Jasper, Bert, and Yannick,

I hope you're doing well.

My name is Haroun, and I'm a third-year "Digital Economics and Business" student in Italy. I'm looking for a 2-month internship in data analytics or business intelligence starting in January 2027, and I wanted to check if you have any spots open in the Heerlen office.

The internship is fully funded by my university through the Erasmus+ Traineeship program, so there are no salary or administrative costs for Axians. Also, I've already secured housing in Maastricht, so commuting to Heerlen daily is completely sorted on my end.

My background is a mix of tech and business. I finished an IT high school diploma before starting my economics degree. I work regularly with Python and SQL, and I recently built an automated ETL pipeline that pulls market data, stores it in PostgreSQL, and runs portfolio simulations. I containerized everything in Docker and orchestrated the flow with Apache Airflow: github.com/RealHarounJ/quant-data-pipeline

I'm currently also working through the Microsoft Power BI learning path and the Google Data Analytics Certificate on Coursera, so I can contribute to your BI projects quickly.

I'd love to help your team build data solutions for clients while learning from your consultants. I've attached my CV for you to look at.

Let me know if you'd be open to a brief chat.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "dsm",
    name: "dsm-firmenich",
    city: "Heerlen, Netherlands",
    country: "NL",
    coords: [50.8940, 5.9850],
    sector: "Nutrition / Science / Corporate Finance",
    size: "Very Large",
    employees: "~28,000",
    strategy: "Maastricht",
    category: "Finance",
    rating: 4.1,
    contactEmail: "careers@dsm-firmenich.com",
    careersUrl: "https://www.dsm-firmenich.com/en/careers.html",
    description: "dsm-firmenich is a Swiss-Dutch multinational science company created by the merger of DSM and Firmenich. Their global headquarters is in Heerlen, NL. They have large finance, business intelligence, and data science teams supporting global operations. Finance interns work in FP&A, Treasury, Controlling, or Business Analytics.",
    culture: "Structured multinational culture. Strong D&I focus. Formal mentorship programs for interns. English is the working language globally. Known as an excellent learning environment for finance and data students.",
    pros: ["Global HQ literally in Heerlen (10 min from Maastricht)", "Highly structured intern program with mentors", "English-language working environment", "Paid internship positions available", "28,000-person brand on your CV"],
    cons: ["Large corporate bureaucracy", "Formal hiring process — online portal required", "Long onboarding procedures"],
    openPositions: [
      {
        title: "Finance / Business Analytics Intern",
        type: "Paid Internship",
        skills_required: ["Excel", "Financial Analysis", "Data Analysis"],
        skills_nice: ["Power BI", "SAP", "Python"],
        your_fit: 75,
        note: "Apply via careers portal with formal application. Paid positions available."
      }
    ],
    skillGaps: ["SAP basics (ERP) — no free cert available, but not required", "Power BI → FREE Microsoft Learn"],
    emailSubject: "Finance / Business Analytics Internship Inquiry — Erasmus+ Funded (Jan 2027)",
    emailTemplate: `Dear dsm-firmenich Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027 in a Finance, Business Analytics, or FP&A role at your Heerlen headquarters.

My placement is fully funded by my university through the Erasmus+ Traineeship program. I have also already secured housing in Maastricht (10 minutes from your Heerlen office), which means there are no logistical or housing costs involved.

My academic background covers corporate finance, macroeconomics, and statistics, which I complement with strong technical skills. I recently built an automated data pipeline in Python that ingests financial data into a PostgreSQL database, runs a Markowitz portfolio optimization, and simulates 10,000 Monte Carlo risk scenarios — all containerized in Docker and orchestrated with Apache Airflow. Code: github.com/RealHarounJ/quant-data-pipeline

I'm also currently completing the Bloomberg Market Concepts (BMC) certificate and the Google Data Analytics Professional Certificate on Coursera — the same credentials used by financial analysts across the industry.

I would love to support your Finance or Business Intelligence teams and learn how data-driven decision making works at a global scale. I've attached my CV for your review.

Thank you for your time. I look forward to your response.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },

  // ══════════════════════════════════════════════════════
  // STRATEGIA 2: GLOBAL HUBS
  // ══════════════════════════════════════════════════════
  {
    id: "robeco",
    name: "Robeco",
    city: "Rotterdam, Netherlands",
    country: "NL",
    coords: [51.9244, 4.4777],
    sector: "Asset Management / Quantitative Investing",
    size: "Large",
    employees: "~1,200",
    strategy: "Global",
    category: "Finance",
    rating: 4.2,
    contactEmail: "careers@robeco.com",
    careersUrl: "https://www.robeco.com/en-int/careers",
    description: "Robeco is one of Europe's most respected asset managers with a strong focus on quantitative investing, sustainable investing (ESG), and systematic strategies. Founded in Rotterdam in 1929, they manage ~€175 billion in AUM. Their quant research team is one of the strongest in Europe and is known for rigorous factor investing research.",
    culture: "Research-driven, intellectual environment. Dutch directness. Strong internal learning culture. Excellent intern program with real research involvement. English is the working language. Known for promoting data-driven thinking at all levels.",
    pros: ["One of the top quant investment shops in Europe", "World-class learning environment", "Real exposure to systematic investment strategies", "Strong intern program with structured feedback", "Rotterdam is ~2h from Maastricht"],
    cons: ["Competitive admission process", "Rotterdam relocation needed (2h from Maastricht)", "Quant roles may require stronger statistical background"],
    openPositions: [
      {
        title: "Investment Research Analyst Intern",
        type: "Internship (3-6 months)",
        skills_required: ["Python", "Statistics", "Financial Markets Knowledge", "Excel"],
        skills_nice: ["R", "Machine Learning", "Bloomberg", "Factor Modeling"],
        your_fit: 70,
        note: "Check robeco.com/en-int/careers for current openings. Apply early — they recruit ahead of time."
      }
    ],
    skillGaps: ["Statistics deeper knowledge → CFI FMVA ($497) or IBM Data Science ($49/mo)", "Bloomberg → BMC (FREE via university)", "Factor Models → Robeco publishes many free research papers on their site"],
    emailSubject: "Erasmus+ Funded Internship: Economics & Data student (Jan 2027)",
    emailTemplate: `Hi Robeco Recruitment Team,

My name is Haroun, and I'm a third-year student in "Digital Economics and Business" at UNIVPM (Italy). I'm very interested in quantitative research and portfolio analytics, and I wanted to check if there are internship openings in your Rotterdam office starting in January 2027.

The internship is fully funded by my university through the Erasmus+ Traineeship scheme, so my stipend is covered — no salary cost for Robeco. I also have a housing base in Maastricht, which makes relocating to Rotterdam much easier for me.

My background is a mix of IT and economics: I completed an IT high school diploma before my bachelor's degree. To apply my programming skills to finance, I recently built an automated portfolio data pipeline in Python. It pulls ETF prices into PostgreSQL, runs basic Markowitz optimization, and simulates 10,000 Monte Carlo paths (GBM) for risk forecasting. The entire flow is orchestrated with Apache Airflow and runs in Docker: github.com/RealHarounJ/quant-data-pipeline

I'm also currently working through the Bloomberg Market Concepts (BMC) certificate and the CFI free financial modeling courses — the industry-standard resources used by the professionals I'm hoping to learn from.

I would love to support your investment or research teams while learning from your quantitative analysts. I've attached my CV for details.

I look forward to hearing from you.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "adyen",
    name: "Adyen",
    city: "Amsterdam, Netherlands",
    country: "NL",
    coords: [52.3676, 4.9041],
    sector: "FinTech / Payments",
    size: "Large",
    employees: "~4,000",
    strategy: "Global",
    category: "Data",
    rating: 4.5,
    contactEmail: "careers@adyen.com",
    careersUrl: "https://www.adyen.com/careers",
    description: "Adyen is the most prestigious European FinTech company, providing payment infrastructure to companies like Meta, Microsoft, Spotify, Uber, and H&M. Listed on Euronext Amsterdam (AMS), they are renowned for their engineering culture, high-calibre team, and exceptional intern compensation (among the highest in Europe).",
    culture: "Engineering-first, no-nonsense, high ownership. Interns are treated as full employees and given real projects. Very flat hierarchy. English-speaking workplace. Known for being intellectually demanding but highly rewarding. One of the best places in Europe to launch a tech/data career.",
    pros: ["Highest intern compensation in EU FinTech", "Real projects with massive scale (billions in transactions)", "Incredible engineering culture and brand", "English-first workplace", "Fast career growth post-internship"],
    cons: ["Highly competitive — elite candidates only", "Engineering-heavy culture may prefer CS backgrounds", "Amsterdam living costs are very high"],
    openPositions: [
      {
        title: "Business Analyst / Data Analyst Intern",
        type: "Paid Internship (€1,500-2,000+/month)",
        skills_required: ["SQL", "Python", "Data Analysis", "Excel", "Analytical Thinking"],
        skills_nice: ["Product Analytics", "A/B Testing", "Looker/Tableau"],
        your_fit: 72,
        note: "Very competitive. Check adyen.com/careers → Filter by 'Internship'. Apply 3-6 months in advance."
      }
    ],
    skillGaps: ["Product analytics mindset → Read Adyen's public blog and case studies", "A/B Testing basics → FREE via Google Analytics Academy", "Looker/Tableau → Tableau Public FREE training"],
    emailSubject: "Internship Application: Digital Economics & Data Student (Jan 2027)",
    emailTemplate: `Dear Adyen Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027 in a data analytics or business analytics role, and I would love to join Adyen.

I came across Adyen because of the incredibly engineered payment infrastructure you've built — the scale at which you process global transactions for companies like Spotify and Microsoft is exactly the kind of data-driven environment I want to learn in.

My background is a mix of IT and economics. I finished an IT high school diploma before starting my economics degree. I recently built an automated financial data pipeline in Python: it pulls ETF prices into PostgreSQL, runs a Markowitz portfolio optimizer, and executes 10,000 Monte Carlo simulations — all orchestrated via Apache Airflow in Docker: github.com/RealHarounJ/quant-data-pipeline

I'm currently working through the Google Data Analytics Professional Certificate (Coursera) and the Bloomberg Market Concepts credential, which have been deepening my SQL and data analysis skills significantly.

My placement is co-funded by the Erasmus+ Traineeship program, which contributes a monthly stipend toward my costs. I'm also comfortable relocating to Amsterdam.

I've attached my CV for details. I would love the chance to contribute to Adyen's data teams.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "flowtraders",
    name: "Flow Traders",
    city: "Amsterdam, Netherlands",
    country: "NL",
    coords: [52.3800, 4.9100],
    sector: "Proprietary Trading / Market Making",
    size: "Medium",
    employees: "~700",
    strategy: "Global",
    category: "Finance",
    rating: 4.1,
    contactEmail: "internship@flowtraders.com",
    careersUrl: "https://www.flowtraders.com/careers",
    description: "Flow Traders is one of the world's leading ETP market makers. They provide liquidity in ETPs across global exchanges using proprietary algorithms and risk models. A very high-performance, meritocratic environment where quantitative thinking is everything. Intern compensation is extremely high.",
    culture: "Fast-paced, high-intensity, meritocratic. Very data-driven. Long hours but exceptional learning. Interns are evaluated on analytical sharpness and problem-solving ability. Informal dress code, very flat hierarchy. English-speaking. Regular knowledge-sharing sessions.",
    pros: ["Elite brand in EU quantitative finance", "Extremely high intern compensation", "Direct exposure to live market data and trading systems", "Very flat, meritocratic structure", "World-class learning environment"],
    cons: ["Very high-intensity work environment", "Requires strong quantitative and programming aptitude", "Highly competitive admission (brainteaser interviews)", "Not a good fit if you prefer slower-paced environments"],
    openPositions: [
      {
        title: "Technology / Data Trainee",
        type: "Paid Internship (~€2,500/month)",
        skills_required: ["Python", "Statistics", "Problem Solving", "Algorithmic Thinking"],
        skills_nice: ["C++", "Low-latency systems", "Market microstructure"],
        your_fit: 62,
        note: "Highly competitive. Strong CS/math background preferred. Prepare for quantitative interview questions."
      }
    ],
    skillGaps: ["Statistics & probability (deeper) → IBM Data Science ($49/mo)", "Algorithmic thinking → LeetCode (FREE)", "Market microstructure → Flow Traders publishes educational content on their site"],
    emailSubject: "Traineeship inquiry: Economics & IT student looking for a Quantitative/Data role (Jan 2027)",
    emailTemplate: `Dear Flow Traders Recruitment Team,

My name is Haroun, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027 in a quantitative trading or data-focused role.

Before studying economics, I completed an IT high school diploma. To bridge coding with finance, I recently designed and built an automated portfolio data pipeline. It extracts market data into PostgreSQL, runs a Markowitz optimization solver, and executes 10,000 Monte Carlo simulations (GBM) to forecast Value-at-Risk. I orchestrated the workflow using Apache Airflow and packaged it in Docker: github.com/RealHarounJ/quant-data-pipeline

I'm currently working through the Bloomberg Market Concepts (BMC) certification and the IBM Data Science Professional Certificate on Coursera to deepen my quantitative and statistical analysis skills — the same tools used by the professionals I'm hoping to learn from.

My placement is funded by the Erasmus+ Traineeship program (stipend covered), and I can relocate to Amsterdam without any housing issues.

I've always been fascinated by ETP market making and systematic trading. I would love to support your data or trading teams. My CV is attached.

Would you be open to a brief chat next week?

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876`
  },
  {
    id: "asml",
    name: "ASML",
    city: "Eindhoven, Netherlands",
    country: "NL",
    coords: [51.4416, 5.4697],
    sector: "High-Tech / Semiconductor Equipment",
    size: "Very Large",
    employees: "~42,000",
    strategy: "Global",
    category: "Data",
    rating: 4.4,
    contactEmail: "student.programs@asml.com",
    careersUrl: "https://www.asml.com/en/careers",
    description: "ASML is the world's only manufacturer of EUV lithography machines — the critical equipment used to produce every advanced semiconductor chip. Without ASML's machines, there are no chips in iPhones, AI servers, or cars. They are the most important tech company in Europe and one of the largest companies on Euronext. Intern program is exceptional.",
    culture: "Highly innovative, collaborative, and international (100+ nationalities). Extremely well-structured intern program with a dedicated buddy and mentor. English is the working language. Regular talks from top scientists and engineers. Known as one of the best companies to intern at in Europe.",
    pros: ["Most important tech company in Europe — elite CV brand", "Outstanding structured intern program", "Paid internship with good compensation", "English-first, massively international environment", "Eindhoven is 1h from Maastricht by train"],
    cons: ["Engineering-heavy — less pure finance", "Eindhoven requires daily commute from Maastricht", "Very large organization — can feel impersonal"],
    openPositions: [
      {
        title: "Business / Finance Analyst Intern",
        type: "Paid Internship (~€600-1,000/month)",
        skills_required: ["Excel", "Data Analysis", "Analytical Thinking", "Presentation Skills"],
        skills_nice: ["Python", "Power BI", "SAP", "SQL"],
        your_fit: 78,
        note: "Apply via ASML careers portal: asml.com/en/careers. Filter by Student / Graduate. Apply early."
      }
    ],
    skillGaps: ["Power BI → FREE Microsoft Learn", "SAP basics → not required for most intern roles"],
    emailSubject: "Business Analytics Internship Inquiry — Erasmus+ Funded Student (Jan 2027)",
    emailTemplate: `Dear ASML Student Programs Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm writing to enquire about Business Analytics or Finance internship opportunities at your Eindhoven headquarters starting in January 2027.

My placement is fully funded by my university through the Erasmus+ Traineeship program (stipend and insurance covered). I also have accommodation in Maastricht, which makes commuting to Eindhoven straightforward.

My background combines economics, statistics, and corporate finance with a strong IT foundation (IT high school diploma). I'm comfortable using Python and SQL for data analysis, and I recently built an automated data pipeline that ingests financial data into PostgreSQL, runs portfolio optimization, and simulates risk scenarios — all containerized in Docker with Apache Airflow: github.com/RealHarounJ/quant-data-pipeline

I'm also currently completing the Microsoft Power BI learning path and the Google Data Analytics Professional Certificate — the resources recommended by leading analysts across the industry.

ASML's position at the heart of the global semiconductor supply chain is exactly the kind of complex, data-driven environment I want to contribute to and learn from. I've attached my CV for your review.

Thank you for your consideration. I look forward to your response.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "ing",
    name: "ING Bank",
    city: "Amsterdam, Netherlands",
    country: "NL",
    coords: [52.3467, 4.8926],
    sector: "Banking / FinTech",
    size: "Very Large",
    employees: "~57,000",
    strategy: "Global",
    category: "Finance",
    rating: 3.8,
    contactEmail: "ing.recruitment@ing.nl",
    careersUrl: "https://www.ing.jobs/netherlands/",
    description: "ING is the largest Dutch bank and one of Europe's most digitally advanced financial institutions. Their Amsterdam HQ hosts large data science, AI, risk analytics, and wholesale banking teams. ING is known for being a 'bank that thinks like a FinTech' and investing heavily in data-driven products and services.",
    culture: "Modern, agile, informal for a big bank. Flat hierarchy in tech and data teams. English widely spoken. Good intern program with real project ownership. Known for its progressive culture and sustainability focus.",
    pros: ["Largest Dutch bank — strong brand", "Highly digital and data-driven culture", "Real intern project ownership", "English-speaking tech teams", "Very broad range of intern roles available"],
    cons: ["Very large organization", "Some bureaucracy in traditional banking divisions", "Competitive process for popular roles"],
    openPositions: [
      {
        title: "Data Analyst / Analytics Intern",
        type: "Paid Internship",
        skills_required: ["Python", "SQL", "Data Analysis", "Statistics"],
        skills_nice: ["Power BI", "Machine Learning", "Banking knowledge"],
        your_fit: 76,
        note: "Apply via ing.jobs/netherlands/. Filter by Student / Intern. Multiple positions available year-round."
      }
    ],
    skillGaps: ["Banking regulations basics → FREE ING Open Courses on their learning portal"],
    emailSubject: "Data Analytics Internship Inquiry — Erasmus+ Funded Student (Jan 2027)",
    emailTemplate: `Dear ING Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027 in a data analytics or business analytics role, and I'm very interested in joining ING's teams in Amsterdam.

My placement is fully funded by my university through the Erasmus+ Traineeship program, so there are no salary costs for ING. I can also relocate to Amsterdam without any housing constraints.

My academic background covers corporate finance, statistics, and macroeconomics, complemented by solid programming skills (IT high school diploma). I work regularly with Python and SQL, and I recently built an automated ETL pipeline that ingests market data into PostgreSQL, runs Markowitz portfolio optimization, and executes Monte Carlo simulations — containerized in Docker and scheduled with Apache Airflow: github.com/RealHarounJ/quant-data-pipeline

I'm currently working through the Bloomberg Market Concepts (BMC) certificate and the Google Data Analytics Professional Certificate on Coursera — the same credentials used by data analysts in the industry.

I'm excited by ING's reputation for thinking like a FinTech inside a traditional bank. I would love to support your data teams and learn how ING uses data science to serve millions of customers. My CV is attached.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "blackrock",
    name: "BlackRock EMEA",
    city: "London, United Kingdom",
    country: "UK",
    coords: [51.5074, -0.1278],
    sector: "Asset Management",
    size: "Very Large",
    employees: "~20,000",
    strategy: "Global",
    category: "Finance",
    rating: 4.2,
    contactEmail: "blackrock.recruitment@blackrock.com",
    careersUrl: "https://careers.blackrock.com/",
    description: "BlackRock is the world's largest asset manager with over $10 trillion AUM. Their EMEA hub in London is one of the most prestigious places in global finance. They are the creators of Aladdin, the world's most powerful investment risk management platform. Intern programs are exceptionally well-structured and very competitive.",
    culture: "High-performance, professional, globally diverse. Very structured intern program with senior mentors. English-first. Known for strong internal culture of intellectual curiosity and data-driven thinking. Aladdin gives interns exposure to technology and finance simultaneously.",
    pros: ["World's largest asset manager — elite brand", "Exceptional structured intern program", "Aladdin platform experience is globally valued", "London = global finance capital", "Strong intern-to-analyst conversion rate"],
    cons: ["Extremely competitive — top-tier only", "London cost of living is very high", "Requires relocation to London", "Formal and demanding environment"],
    openPositions: [
      {
        title: "Analyst Internship — Aladdin / Technology or Analytics",
        type: "Summer Internship (10 weeks, paid ~£3,000/month)",
        skills_required: ["Analytical Skills", "Excel", "Python basics", "Finance Knowledge"],
        skills_nice: ["Programming", "Risk Management", "Statistics"],
        your_fit: 65,
        note: "Apply via careers.blackrock.com well in advance (6-9 months before start). Very competitive."
      }
    ],
    skillGaps: ["Financial markets fundamentals → Bloomberg BMC (FREE via university)", "Python (more advanced) → PCAP ($295)", "Risk management basics → CFA Investment Foundations ($79 students)"],
    emailSubject: "Traineeship inquiry: Economics & Data student (Jan 2027) – Erasmus+ Funded",
    emailTemplate: `Dear BlackRock Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm writing to enquire about off-cycle or short-term internship opportunities within your analytics or risk management teams in London starting after January 2027.

The internship would be fully sponsored by my university's Erasmus+ Traineeship scheme, covering my stipend and insurance — so there is no salary cost for BlackRock.

My academic background combines economics, statistics, and corporate finance, complemented by strong technical skills. I recently built a Python-based quantitative portfolio pipeline that automates ETF price ingestion into PostgreSQL, runs basic Markowitz Mean-Variance optimization, and projects 1-year portfolio value using 10,000 Monte Carlo paths. The system runs in Docker and is scheduled via Apache Airflow: github.com/RealHarounJ/quant-data-pipeline

I'm also currently completing the Bloomberg Market Concepts (BMC) certificate — the standard credential recognized across the industry — alongside the CFA Investment Foundations and the Google Data Analytics Professional Certificate on Coursera.

I'm highly interested in BlackRock because of how Aladdin integrates technology and data science into investment processes at an unprecedented scale. I would love to assist your data teams. My CV is attached.

Thank you for your time. I look forward to your response.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "deloitte_nl",
    name: "Deloitte Netherlands",
    city: "Amsterdam, Netherlands",
    country: "NL",
    coords: [52.3387, 4.8716],
    sector: "Consulting / Financial Advisory",
    size: "Very Large",
    employees: "~7,000 (NL)",
    strategy: "Global",
    category: "Finance",
    rating: 3.9,
    contactEmail: "nl_campus@deloitte.nl",
    careersUrl: "https://www2.deloitte.com/nl/en/pages/careers/articles/students.html",
    description: "Deloitte Netherlands is one of the Big 4 accounting and consulting firms with extensive practices in Financial Advisory, Risk Advisory, Technology Consulting, and Data Analytics. Their Amsterdam office is a major European hub. They offer the broadest range of student internships of any firm in the Netherlands, with structured programs across all service lines.",
    culture: "Professional services culture — structured, client-oriented. Smart casual dress. Strong intern learning academy with formal training days. English widely used in cross-border projects. Known for very active student communities and good social culture for interns.",
    pros: ["Broadest range of intern opportunities in NL (finance, tech, data, audit, consulting)", "Structured intern learning program", "Big 4 brand = universally recognized CV", "English-speaking client projects", "Strong social culture for interns"],
    cons: ["Client-service industry = can be long hours during peak seasons", "Large firm — personal attention varies by team", "Competitive admission process"],
    openPositions: [
      {
        title: "Financial Advisory / Data Analytics Intern",
        type: "Paid Internship (~€800-1,200/month)",
        skills_required: ["Excel", "Analytical Thinking", "Presentation Skills", "Attention to Detail"],
        skills_nice: ["Python", "SQL", "Power BI", "Finance Knowledge"],
        your_fit: 80,
        note: "Apply via Deloitte NL careers portal. They run rolling internship programs — multiple openings available year-round."
      }
    ],
    skillGaps: ["Financial modeling → CFI free courses (FREE) or FMVA ($497)", "Power BI → FREE Microsoft Learn"],
    emailSubject: "Financial Advisory / Data Analytics Internship — Erasmus+ Student (Jan 2027)",
    emailTemplate: `Dear Deloitte Netherlands Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027 in a Financial Advisory or Data Analytics role, and I'm very interested in joining Deloitte Netherlands.

My placement is fully funded by my university through the Erasmus+ Traineeship program — no salary cost to Deloitte. I can also relocate to Amsterdam without any housing issues.

My academic coursework covers corporate finance, accounting, and macroeconomics, which I complement with strong IT skills (IT high school diploma). I work regularly with Python and SQL, and I recently built an automated data pipeline that ingests market data into PostgreSQL, runs portfolio optimization, and executes Monte Carlo risk simulations in Docker: github.com/RealHarounJ/quant-data-pipeline

I'm currently completing the Bloomberg Market Concepts certificate and CFI's financial modeling courses — the same credentials used by the financial analysts I'm hoping to work alongside.

I believe my dual background in economic analysis and data tools would let me contribute meaningfully to Deloitte's Financial Advisory or Risk Analytics teams. I've attached my CV for your review.

I would appreciate the chance to discuss any available positions.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "pwc_nl",
    name: "PwC Netherlands",
    city: "Amsterdam, Netherlands",
    country: "NL",
    coords: [52.3550, 4.8970],
    sector: "Consulting / Audit / Financial Advisory",
    size: "Very Large",
    employees: "~6,000 (NL)",
    strategy: "Global",
    category: "Finance",
    rating: 3.9,
    contactEmail: "recruitment@pwc.nl",
    careersUrl: "https://www.pwc.nl/nl/carriere/studenten.html",
    description: "PwC Netherlands is one of the four largest professional services firms in the country, with major practices in Deals (M&A), Tax, Audit, and Digital/Data consulting. Their Experience Center in Amsterdam is a leading hub for data-driven business transformation projects. They actively recruit Digital Economics and Business students.",
    culture: "Professional, collaborative, and increasingly tech-forward. PwC has been investing heavily in data analytics and digital transformation capabilities. Interns get real client exposure. Good social events and intern community. English used on international projects.",
    pros: ["Big 4 brand — globally recognized", "PwC Digital/Data practice is growing rapidly", "Real client exposure from day 1", "Strong intern community and social events", "Deals team experience for finance-focused interns"],
    cons: ["Audit roles may be less relevant for data-focused profiles", "Formal application process — online portal required", "Large firm dynamics"],
    openPositions: [
      {
        title: "Deals / Digital & Data Analytics Intern",
        type: "Paid Internship (~€800-1,200/month)",
        skills_required: ["Excel", "PowerPoint", "Analytical Thinking", "Communication"],
        skills_nice: ["Python", "SQL", "Power BI", "Financial Modeling"],
        your_fit: 78,
        note: "Apply via pwc.nl/nl/carriere. Deals and Digital practices have the most relevant positions."
      }
    ],
    skillGaps: ["Financial modeling → CFI free courses (FREE)", "M&A basics → WSP Excel Crash Course ($39)"],
    emailSubject: "Digital & Data Analytics Internship Inquiry — Erasmus+ Student (Jan 2027)",
    emailTemplate: `Dear PwC Netherlands Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year "Digital Economics and Business" student at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027 in a Digital Analytics or Deals role, and I'm very interested in joining PwC Netherlands.

My placement is fully funded by my university through the Erasmus+ Traineeship program — no salary or administrative costs for PwC. I can also relocate to Amsterdam.

My academic background covers corporate finance, statistics, and macroeconomics, alongside strong IT skills (IT high school diploma before university). I recently built a financial data pipeline in Python that ingests market data, runs portfolio optimization, and simulates risk scenarios using Monte Carlo methods: github.com/RealHarounJ/quant-data-pipeline

I'm currently completing the Google Data Analytics Professional Certificate (Coursera), the Bloomberg Market Concepts certificate, and Microsoft's Power BI learning path — credentials that align directly with PwC's digital and data consulting work.

I believe my combination of economic analysis, data programming, and eagerness to learn would be a good fit for PwC's Experience Center or Deals team. I've attached my CV.

Thank you for your time.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "berenberg",
    name: "Berenberg Bank",
    city: "London, United Kingdom",
    country: "UK",
    coords: [51.5130, -0.0920],
    sector: "Investment Banking / Equity Research",
    size: "Medium",
    employees: "~1,800",
    strategy: "Global",
    category: "Finance",
    rating: 4.0,
    contactEmail: "graduates@berenberg.com",
    careersUrl: "https://www.berenberg.de/en/careers/graduates-and-students/",
    description: "Berenberg is Germany's oldest private bank (founded 1590) and a leading European investment bank with a strong London presence. Known for their high-quality equity research and investment banking advisory for mid-cap European companies. A prestigious boutique that offers interns real deal and research exposure.",
    culture: "Traditional European banking culture but with a strong meritocratic and intellectual edge. Excellent equity research mentorship. English is the primary language in London. Interns work closely with senior analysts and bankers — high expectations but excellent learning.",
    pros: ["Oldest private bank in Germany — prestigious brand", "Real equity research and IB deal exposure", "Excellent learning and mentorship from senior bankers", "Mid-cap European focus = broader responsibility than bulge brackets", "London placement"],
    cons: ["Traditional banking culture — formal environment", "High pressure in IB and Research divisions", "Competitive admission for IB roles"],
    openPositions: [
      {
        title: "Equity Research / Economic Analysis Intern",
        type: "Internship",
        skills_required: ["Excel", "Financial Modeling basics", "Sector Research", "Report Writing"],
        skills_nice: ["Bloomberg", "Python", "CFA Investment Foundations"],
        your_fit: 70,
        note: "Apply via berenberg.de/en/careers/graduates-and-students/. Internships run across multiple service lines."
      }
    ],
    skillGaps: ["Bloomberg → BMC cert (FREE via university)", "Financial Modeling → CFI FMVA ($497) or WSP ($499)", "Equity Research writing → Read Berenberg's published research on their site"],
    emailSubject: "Internship Application: Equity Research / Economic Analysis (Jan 2027)",
    emailTemplate: `Dear Berenberg Recruitment Team,

I hope you're doing well.

My name is Haroun Jaafar, and I'm a third-year Economics student at UNIVPM (Italy). I'm looking for a 2-month internship starting in January 2027, and I'm very interested in joining your equity research or economic analysis teams in London.

My placement is funded by my university through the Erasmus+ Traineeship program, so there are no salary or administrative costs for Berenberg.

My coursework covers corporate finance, macroeconomics, and statistics, which I complement with a solid IT background (IT high school diploma before my degree). I'm comfortable using Python and SQL to clean and analyze financial data. Recently, I built an automated data pipeline that pulls ETF prices, stores them in PostgreSQL, and runs portfolio optimization and Monte Carlo simulations: github.com/RealHarounJ/quant-data-pipeline

I'm currently studying for the Bloomberg Market Concepts (BMC) certificate and working through CFI's financial modeling courses — the same credentials and resources used by the research analysts I'm hoping to work alongside.

I closely follow macroeconomic developments and European equity markets, and I believe my combination of economic analysis and data skills allows me to translate numbers into clear investment stories. I'd love to help your analysts research sectors and compile market reports.

I've attached my CV for your review.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  },
  {
    id: "pictet",
    name: "Pictet Asset Management",
    city: "Geneva, Switzerland",
    country: "CH",
    coords: [46.2044, 6.1432],
    sector: "Wealth & Asset Management",
    size: "Large",
    employees: "~4,600",
    strategy: "Global",
    category: "Finance",
    rating: 4.3,
    contactEmail: "careers@pictet.com",
    careersUrl: "https://www.group.pictet/careers",
    description: "Pictet is one of Europe's most prestigious private wealth and asset management groups, headquartered in Geneva since 1805. Known for a research-driven, long-term investment philosophy and a highly selective internship program. Strong in thematic investing and ESG. A name that carries enormous weight in European and global wealth management circles.",
    culture: "Refined, intellectual, and discreet — characteristic of top Swiss private banking. Very high standards. Interns are expected to be analytical, rigorous, and self-directed. English and French are the working languages. Exceptional long-term career prestige for those who pass through.",
    pros: ["One of the most prestigious names in European private banking", "Long-term research-driven philosophy (great learning)", "Geneva = international finance hub", "ESG and thematic investing leadership", "Career prestige is exceptional"],
    cons: ["Very selective — high competition", "Formal and reserved culture", "Geneva is expensive to live in", "French language is an advantage"],
    openPositions: [
      {
        title: "Portfolio Analytics / Investment Research Intern",
        type: "Internship",
        skills_required: ["Excel", "Financial Analysis", "Analytical Rigor", "Attention to Detail"],
        skills_nice: ["Python", "Bloomberg", "CFA knowledge", "French language"],
        your_fit: 60,
        note: "Very selective. Apply via group.pictet/careers. Demonstrating investment research interest is essential."
      }
    ],
    skillGaps: ["Portfolio analytics → CFI FMVA ($497)", "Bloomberg → BMC (FREE)", "Investment research → Read Pictet's public research reports on their website"],
    emailSubject: "Funded Internship Inquiry: Portfolio Analytics / Research (Jan 2027)",
    emailTemplate: `Dear Pictet Recruitment Team,

My name is Haroun Jaafar, and I'm a third-year student in "Digital Economics and Business" at UNIVPM (Italy). I'm writing to see if you have any internship opportunities in your portfolio analytics or investment research teams in Geneva starting after January 2027.

The internship is fully funded by the Erasmus+ Traineeship program through my university — no salary or administrative costs for Pictet, just a standard Host Agreement to sign.

I am highly interested in Pictet because of your long-term, research-driven approach to wealth and asset management. On the technical side, I work regularly with Python and SQL. I recently built a quantitative pipeline that automates financial data ingestion into PostgreSQL, runs basic Markowitz optimization, and runs 10,000 Monte Carlo paths for risk forecasting — containerized in Docker with Apache Airflow: github.com/RealHarounJ/quant-data-pipeline

I'm currently working through the Bloomberg Market Concepts (BMC) certificate and the CFA Investment Foundations — the same credentials used by the analysts I am hoping to learn from.

I would love to support your analysts and learn how Pictet designs and manages portfolios over the long term. I've attached my CV for details.

Thank you for your consideration. I look forward to hearing from you.

Best regards,
Haroun Jaafar
haroun.jaafar@studenti.univpm.it | +39 3515246876
github.com/RealHarounJ`
  }
];
