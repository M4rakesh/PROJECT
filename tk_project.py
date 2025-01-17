import sqlite3
import tkinter as tk
from tkinter import messagebox
from Klienti1 import klientu_logs
from Laukums_grida1 import laukums_logs

def izveidot_galveno_logu():
    def klienti_poga():
        klientu_logs()

    def laukumi_poga():
        laukums_logs()

    def materiali_poga():
        materials_logs()
        messagebox.showinfo("Apmeklējumi", "Atvērta apmeklējumu pārvaldība.")

    logs = tk.Tk()
    logs.title("GLR")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="violet")
    Klients_btn = tk.Button(logs, text="Klienti", command=klienti_poga, width=20, height=2, bg="lightblue")
    Klients_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Laukumi", command=laukumi_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Materiali", command=materiali_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()


if __name__ == "__main__":
    izveidot_galveno_logu()