import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def pievienot_laukumu():
    def saglabat_laukumu():
        platums = platums_entry.get()
        garums = garums_entry.get()             
        

        if platums and garums.isdigit():
            cursor.execute(
                "INSERT INTO Laukums (platums,garums,laukums) VALUES (?, ?, ?)",
                (float(platums),float(garums), (float(platums)*float(garums)))
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Laukums pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot Laukumu")
    logs.geometry("300x300+700+450")

    tk.Label(logs, text="Platums:").pack()
    platums_entry = tk.Entry(logs)
    platums_entry.pack()

    tk.Label(logs, text="Garums:").pack()
    garums_entry = tk.Entry(logs)
    garums_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_laukumu)
    saglabat_btn.pack(pady=10)


def meklēt_laukumu():
    def atrast_laukumu():
        platums = platums_entry.get()
        if platums:
            cursor.execute("SELECT * FROM Laukums WHERE platums LIKE ?", (f"%{platums}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
                    messagebox.showinfo("Rezultāti", f"{r[0]}: platums: {r[1]} garums: {r[2]}, Laukums: {r[3]}\n")
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens gridas laukums.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet klienta vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt Gridas laukumu")
    logs.geometry("300x200+700+450")

    tk.Label(logs, text="Platumu:").pack()
    platums_entry = tk.Entry(logs)
    platums_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_laukumu)
    meklēt_btn.pack(pady=10)


def dzēst_laukumu():
    def dzēst_laukumu_no_db():
        id_lauk = id_lauk_entry.get()
        if id_lauk.isdigit():
            cursor.execute("DELETE FROM Laukums WHERE id_lauk = ?", (id_lauk))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Laukums ar ID {id_lauk} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst Laukumi")
    logs.geometry("300x150+700+450")

    tk.Label(logs, text="Laukuma ID:").pack()
    id_lauk_entry = tk.Entry(logs)
    id_lauk_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_laukumu_no_db)
    dzēst_btn.pack(pady=10)


def laukums_logs():
    laukums_logs = tk.Toplevel()
    laukums_logs.title("Klientu pārvaldība")
    laukums_logs.geometry("300x250+700+450")

    pievienot_btn = tk.Button(laukums_logs, text="Pievienot gridas laukumu", command=pievienot_laukumu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(laukums_logs, text="Meklēt gridas laukumu", command=meklēt_laukumu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(laukums_logs, text="Dzēst gridas laukumu", command=dzēst_laukumu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(laukums_logs, text="Iziet", command=laukums_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)