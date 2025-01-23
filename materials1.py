import sqlite3
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox

conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def pievienot_materialu():
    def saglabat_materialu():
        materials = materials_entry.get()
        platums = platums_entry.get()
        garums = garums_entry.get()                
        cena = cena_entry.get()


        if platums and garums and cena and materials:
            cursor.execute(
                "INSERT INTO Material (mater_veids,platums,garums,mater_izmers,cena) VALUES (?, ?, ?,?,?)",
                (materials,float(platums),float(garums),str(platums)+"x"+str(garums),float(cena)))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Materials pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot Materalu")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Platums:",bg="#6F5100").pack()
    platums_entry = tk.Entry(logs)
    platums_entry.pack()

    tk.Label(logs, text="Garums:",bg="#6F5100").pack()
    garums_entry = tk.Entry(logs)
    garums_entry.pack()

    tk.Label(logs, text="Materila veids: (flizes,laminats,linolejs)",bg="#6F5100").pack()
    materials_entry = tk.Entry(logs)
    materials_entry.pack()

    tk.Label(logs, text="Cena:",bg="#6F5100").pack()
    cena_entry = tk.Entry(logs)
    cena_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_materialu,bg="yellow")
    saglabat_btn.pack(pady=10)


def meklēt_materialu():
    def atrast_materialu():
        platums = platums_entry.get()
        if platums:
            cursor.execute("SELECT * FROM Material WHERE platums LIKE ?", (f"%{platums}%",))
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
    logs.title("Meklēt Materialu")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Platumu:",bg="#6F5100").pack()
    platums_entry = tk.Entry(logs)
    platums_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_materialu,bg="yellow")
    meklēt_btn.pack(pady=10)


def dzēst_materialu():
    def dzēst_materialu_no_db():
        id_mater = id_mater_entry.get()
        if id_mater.isdigit():
            cursor.execute("DELETE FROM Material WHERE id_mater = ?", (id_mater))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Materilas ar ID {id_mater} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst Materialu")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Laukuma ID:",bg="#6F5100").pack()
    id_mater_entry = tk.Entry(logs)
    id_mater_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_materialu_no_db,bg="yellow")
    dzēst_btn.pack(pady=10)


def materials_logs():
    materials_logs = tk.Toplevel()
    materials_logs.title("Klientu pārvaldība")
    materials_logs.geometry(f"300x250+{int((materials_logs.winfo_screenwidth())/2)-150}+{int((materials_logs.winfo_screenheight())/2)-125}")
    materials_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(materials_logs, text="Pievienot materialu", command=pievienot_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(materials_logs, text="Meklēt materialu", command=meklēt_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(materials_logs, text="Dzēst materialu", command=dzēst_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(materials_logs, text="Iziet", command=materials_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)