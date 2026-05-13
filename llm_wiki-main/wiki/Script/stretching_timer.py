import tkinter as tk
import winsound

# ─── CONFIGURAZIONE ────────────────────────────────────────────────
BREAK_MINUTES = 45  # Intervallo tra una sessione e l'altra (minuti)
# ───────────────────────────────────────────────────────────────────

class StretchingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biohacking Stretching (Neumann Protocol)")
        self.root.geometry("580x430")
        self.root.configure(bg='#1e1e1e')
        self.root.attributes('-topmost', True)  # Sempre in primo piano durante gli alert

        # Basati sulla Kinesiology of the Musculoskeletal System
        self.exercises = [
            ("Estensione Toracica (Neumann)", "Seduto. Incrocia le mani dietro la testa, inarca la parte alta della schiena all'indietro. Contrasta la postura cifotica da studente.", 45),
            ("Allungamento Cervicale Laterale", "Mantieni la spalla destra bassa. Inclina lentamente la testa verso sinistra aiutandoti con la mano sinistra.", 30),
            ("Allungamento Cervicale Laterale (Cambio)", "Mantieni la spalla sinistra bassa. Inclina lentamente la testa verso destra aiutandoti con la mano destra.", 30),
            ("Allungamento Polsi (Decompressione Tunnel Carpale)", "Braccio teso in avanti. Con l'altra mano, tira delicatamente le dita verso di te per allungare i flessori.", 30),
            ("Squat Isometrico sul Posto", "Alzati dalla sedia. Scendi a metà squat e mantieni la posizione. L'obiettivo è pompare sangue ai glutei e riattivare l'AMPK.", 45)
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
        self.ex_title.pack(pady=10)

        self.ex_desc = tk.Label(root, text="Eviterai la degenerazione dei dischi intervertebrali (Harrison).",
                                fg='#aaaaaa', bg='#1e1e1e', font=('Helvetica', 11),
                                wraplength=490, justify="center")
        self.ex_desc.pack(pady=10)

        self.time_lbl = tk.Label(root, text="00:00", fg='#ff3333', bg='#1e1e1e',
                                 font=('Helvetica', 52, 'bold'))
        self.time_lbl.pack(pady=15)

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
            title, desc, duration = self.exercises[self.current_ex]
            self.ex_title.config(
                text=f"Esercizio {self.current_ex + 1}/{len(self.exercises)}: {title}",
                fg='white')
            self.ex_desc.config(text=desc, fg='#aaaaaa')
            self.time_left = duration
            self.timer_running = True
            self.time_lbl.config(fg='#ff3333')
            self.update_timer()
            self.current_ex += 1
        else:
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
