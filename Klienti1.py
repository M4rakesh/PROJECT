import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def pievienot_klientu():
    def saglabat_klientu():
        vards = vards_entry.get()
        uzvards = uzvards_entry.get()             
        tel_nr = tel_nr_entry.get()

        if vards and uzvards and tel_nr.isdigit():
                if vards:
                    cursor.execute("SELECT vards FROM Klients WHERE vards LIKE ?", (f"%{vards}%"))
                    rezultati = cursor.fetchall()
                    if rezultati:
                        rezultati_str = ""
                        for r in rezultati:
                            rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
                            messagebox.showinfo("Rezultāti", f"{r[0]}: Vards: {r[1]} Uzvards: {r[2]}, Talrunis: {r[3]}\n")
                            messagebox.showinfo("Veiksmīgi", "klientu ekseste sistema!")
                else:
                    cursor.execute(
                        "INSERT INTO Klients (vards, uzvards, tel_nr) VALUES (?, ?, ?)",
                        (vards, uzvards, tel_nr)
                    )
                    conn.commit()
                    messagebox.showinfo("Veiksmīgi", "klientu pievienots!")
                    logs.destroy()
        else:
                    messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot Klientu")
    logs.geometry("300x300")

    tk.Label(logs, text="Vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    tk.Label(logs, text="Uzvārds:").pack()
    uzvards_entry = tk.Entry(logs)
    uzvards_entry.pack()

    tk.Label(logs, text="Tālrunis:").pack()
    tel_nr_entry = tk.Entry(logs)
    tel_nr_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_klientu)
    saglabat_btn.pack(pady=10)


def meklēt_klientu():
    def atrast_klientu():
        vards = vards_entry.get()
        if vards:
            cursor.execute("SELECT * FROM Klients WHERE vards LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
                    messagebox.showinfo("Rezultāti", f"{r[0]}: Vards: {r[1]} UZvards: {r[2]}, Talrunis: {r[3]}\n")
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens klientu.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet klienta vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt Klientu")
    logs.geometry("300x200")

    tk.Label(logs, text="Klienta vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_klientu)
    meklēt_btn.pack(pady=10)


def dzēst_klientu():
    def dzēst_klientu_no_db():
        id_klientu = id_klientu_entry.get()
        if id_klientu.isdigit():
            cursor.execute("DELETE FROM Klients WHERE id_klients = ?", (id_klientu,))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Klients ar ID {id_klientu} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst Klientu")
    logs.geometry("300x150")

    tk.Label(logs, text="Klienta ID:").pack()
    id_klientu_entry = tk.Entry(logs)
    id_klientu_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_klientu_no_db)
    dzēst_btn.pack(pady=10)


def klientu_logs():
    klientu_logs = tk.Toplevel()
    klientu_logs.title("Klientu pārvaldība")
    klientu_logs.geometry("300x250")

    pievienot_btn = tk.Button(klientu_logs, text="Pievienot klientu", command=pievienot_klientu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(klientu_logs, text="Meklēt klientu", command=meklēt_klientu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(klientu_logs, text="Dzēst klientu", command=dzēst_klientu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(klientu_logs, text="Iziet", command=klientu_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)