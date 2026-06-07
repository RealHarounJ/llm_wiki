import tkinter as tk
import winsound
import os
from PIL import Image, ImageTk


# ─── CONFIGURAZIONE ────────────────────────────────────────────────
BREAK_MINUTES = 45  # Intervallo tra una sessione e l'altra (minuti)
# ───────────────────────────────────────────────────────────────────

class StretchingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biohacking Stretching (Neumann Protocol)")
        self.root.geometry("580x630")
        self.root.configure(bg='#1e1e1e')
        self.root.attributes('-topmost', True)  # Sempre in primo piano durante gli alert

        # Basati sulla Kinesiology of the Musculoskeletal System
        # Formato: (Titolo, Descrizione, Durata in secondi, Nome file immagine)
        self.exercises = [
            ("Estensione Toracica (Neumann)", "Seduto. Incrocia le mani dietro la testa, inarca la parte alta della schiena all'indietro. Contrasta la postura cifotica da studente.", 45, "thoracic_extension.png"),
            ("Allungamento Cervicale Laterale", "Mantieni la spalla destra bassa. Inclina lentamente la testa verso sinistra aiutandoti con la mano sinistra.", 30, "neck_stretch.png"),
            ("Allungamento Cervicale Laterale (Cambio)", "Mantieni la spalla sinistra bassa. Inclina lentamente la testa verso destra aiutandoti con la mano destra.", 30, "neck_stretch.png"),
            ("Allungamento Polsi (Decompressione Tunnel Carpale)", "Braccio teso in avanti. Con l'altra mano, tira delicatamente le dita verso di te per allungare i flessori.", 30, "wrist_stretch.png"),
            ("Squat Isometrico sul Posto", "Alzati dalla sedia. Scendi a metà squat e mantieni la posizione. L'obiettivo è pompare sangue ai glutei e riattivare l'AMPK.", 45, "isometric_squat.png"),
            ("Allungamento Ischiocrurali (Catena Posteriore)", "In piedi. Fletti il busto in avanti mantenendo le ginocchia leggermente sbloccate (non tese al massimo) per allungare i muscoli posteriori delle cosce.", 40, "hamstring_stretch.png"),
            ("Allungamento Flessori Anca (Psoas)", "Fai un affondo basso portando una gamba indietro. Spingi il bacino in avanti per allungare l'anca. Contrasta l'accorciamento dovuto alla sedia.", 40, "psoas_stretch.png")
        ]

        self.current_ex = 0
        self.time_left = 0
        self.timer_running = False
        self.break_mode = False
        self.session_count = 0
        self._after_id = None

        # ─── UI ────────────────────────────────────────────────────
        self.title_lbl = tk.Label(root, text="Protocollo Kinesiologico — Neumann & Harrison",
                                  fg='#00d2ff', bg='#1e1e1e', font=('Helvetica', 12, 'bold'))
        self.title_lbl.pack(pady=12)

        self.session_lbl = tk.Label(root, text="Sessione: 0 completate",
                                    fg='#555555', bg='#1e1e1e', font=('Helvetica', 9))
        self.session_lbl.pack()

        self.ex_title = tk.Label(root, text="Premi Inizia per sbloccare la colonna",
                                 fg='white', bg='#1e1e1e', font=('Helvetica', 13, 'bold'))
        self.ex_title.pack(pady=8)

        self.ex_desc = tk.Label(root, text="Eviterai la degenerazione dei dischi intervertebrali (Harrison).",
                                fg='#aaaaaa', bg='#1e1e1e', font=('Helvetica', 11),
                                wraplength=490, justify="center")
        self.ex_desc.pack(pady=8)

        # Contenitore per l'immagine illustrativa
        self.img_lbl = tk.Label(root, bg='#1e1e1e')
        self.img_lbl.pack(pady=8)

        self.time_lbl = tk.Label(root, text="00:00", fg='#ff3333', bg='#1e1e1e',
                                 font=('Helvetica', 46, 'bold'))
        self.time_lbl.pack(pady=8)

        self.btn = tk.Button(root, text="INIZIA ROUTINE", command=self.start_routine,
                             bg='#00d2ff', fg='black', font=('Helvetica', 13, 'bold'),
                             relief=tk.FLAT, padx=20, pady=6)
        self.btn.pack(pady=6)

        self.skip_btn = tk.Button(root, text="", command=self.skip_break,
                                  bg='#333333', fg='#aaaaaa', font=('Helvetica', 10),
                                  relief=tk.FLAT, padx=14, pady=4)
        self.skip_btn.pack(pady=2)
        self.skip_btn.pack_forget()  # nascosto inizialmente

    # ─── ROUTINE ───────────────────────────────────────────────────

    def start_routine(self):
        """Avvia (o riavvia) la routine di stretching."""
        if self._after_id:
            self.root.after_cancel(self._after_id)
            self._after_id = None
        self.break_mode = False
        self.current_ex = 0
        self.timer_running = False
        self.skip_btn.pack_forget()
        self.btn.config(state=tk.DISABLED, text="IN CORSO...")
        self.root.attributes('-topmost', True)
        self.next_exercise()

    def next_exercise(self):
        if self.current_ex < len(self.exercises):
            title, desc, duration, img_file = self.exercises[self.current_ex]
            self.ex_title.config(
                text=f"Esercizio {self.current_ex + 1}/{len(self.exercises)}: {title}",
                fg='white')
            self.ex_desc.config(text=desc, fg='#aaaaaa')
            
            # Caricamento e visualizzazione immagine illustrativa tramite Pillow
            img_path = os.path.join(os.path.dirname(__file__), img_file)
            if os.path.exists(img_path):
                try:
                    pil_img = Image.open(img_path)
                    # Ridimensiona l'immagine proporzionalmente a max 180x180 pixel
                    pil_img.thumbnail((180, 180), Image.Resampling.LANCZOS)
                    photo_resized = ImageTk.PhotoImage(pil_img)
                    self.img_lbl.config(image=photo_resized)
                    self.img_lbl.image = photo_resized  # riferimento persistente per evitare garbage collection
                except Exception as e:
                    self.img_lbl.config(image='')
                    print(f"Errore nel caricamento dell'immagine {img_file}: {e}")
            else:
                self.img_lbl.config(image='')

            self.time_left = duration
            self.timer_running = True
            self.time_lbl.config(fg='#ff3333')
            self.update_timer()
            self.current_ex += 1
        else:
            self.img_lbl.config(image='') # cancella l'immagine alla fine
            self._on_routine_complete()

    def update_timer(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.time_lbl.config(text=f"{mins:02d}:{secs:02d}")
            self.time_left -= 1
            self._after_id = self.root.after(1000, self.update_timer)
        else:
            winsound.Beep(880, 400)
            self.time_lbl.config(text="CAMBIO!", fg='yellow')
            self._after_id = self.root.after(1500, self.next_exercise)

    # ─── FINE ROUTINE → PAUSA ──────────────────────────────────────

    def _on_routine_complete(self):
        self.timer_running = False
        self.session_count += 1
        self.session_lbl.config(text=f"Sessione: {self.session_count} completate ✓", fg='#00ffcc')
        winsound.Beep(660, 300)
        winsound.Beep(880, 300)
        winsound.Beep(1100, 500)
        self.ex_title.config(text="✅ Routine Completata! Focus Ripristinato.", fg='#00ffcc')
        self.ex_desc.config(
            text="Hai ristabilito il flusso di ossigeno al cervello e azzerato la tensione del rachide.\n"
                 f"Prossima sessione tra {BREAK_MINUTES} minuti...",
            fg='#888888')
        self.time_lbl.config(text="", fg='#00ffcc')
        self.btn.config(state=tk.NORMAL, text="INIZIA ORA", bg='#00d2ff')
        self.root.attributes('-topmost', False)  # non blocca il lavoro durante la pausa

        # Mostra il tasto "Salta pausa"
        self.skip_btn.config(text=f"Salta pausa — Ricomincia subito")
        self.skip_btn.pack(pady=2)

        # Avvia il conto alla rovescia della pausa
        self.break_mode = True
        self.time_left = BREAK_MINUTES * 60
        self._countdown_break()

    def _countdown_break(self):
        if not self.break_mode:
            return
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.time_lbl.config(text=f"{mins:02d}:{secs:02d}", fg='#444444')
            self.time_left -= 1
            self._after_id = self.root.after(1000, self._countdown_break)
        else:
            self._alert_next_session()

    def _alert_next_session(self):
        """Suona l'alert e riapre la finestra in primo piano per la prossima sessione."""
        self.break_mode = False
        self.root.attributes('-topmost', True)
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        for _ in range(3):
            winsound.Beep(1000, 300)
        self.ex_title.config(text="🔔 È ORA DI FARE STRETCHING!", fg='#ff9900')
        self.ex_desc.config(text="45 minuti di studio completati. Alzati e fai la routine!", fg='#ff9900')
        self.time_lbl.config(text="STRETCH!", fg='#ff9900')
        self.btn.config(text="INIZIA ROUTINE", bg='#ff9900')
        self.skip_btn.pack_forget()

    def skip_break(self):
        """Salta la pausa e riavvia subito la routine."""
        self.start_routine()

# ─── MAIN ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = StretchingApp(root)
    root.mainloop()
