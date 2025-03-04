import sqlite3
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox,ttk


conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def savienot_informaciju():
    def saglabat_informaciju():
        id_info = id_info.get()
        id_mater = id_mater.get()
        id_klients = id_klients.get()
        id_lauk = id_lauk.get()
        mater_daudzums = mater_daudzums.get()
        kopcena = kopcena.get()
        datums = datums.get()

        if id_mater and id_klients and id_lauk and kopcena:
            cursor.execute(
                "INSERT INTO INFO (id_info,id_mater,id_klients,id_lauk,mater_daudzums,kopcena,datums) VALUES (?, ?, ?,?,?,?,?)",
                (id_info,id_mater,id_klients,id_lauk,mater_daudzums,kopcena,datums))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "pasutijuma pievienots!")
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
    pasutijuma_entry = tk.Entry(logs)
    pasutijuma_entry.pack()

    tk.Label(logs, text="Cena:",bg="#6F5100").pack()
    cena_entry = tk.Entry(logs)
    cena_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_informaciju,bg="yellow")
    saglabat_btn.pack(pady=10)


def meklēt_materialu():
    def mater_list():
        global pasutijuma
        conn= sqlite3.connect('grida.db')
        cursor=conn.cursor()
        cursor.execute("SELECT platums FROM Material")
        pasutijuma = []
        mater_all=cursor.fetchall()
        for mater in mater_all:
            pasutijuma.append(mater[0])
        print(pasutijuma)
        conn.close()



    def atrast_materialu():
        platums = platums_entry.get()
        
        if platums:
            cursor.execute("SELECT * FROM Material WHERE platums and mater_veids LIKE ?", (f"%{platums}%"))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
                    messagebox.showinfo("Rezultāti", f"{r[0]}: platums: {r[1]} garums: {r[2]}, Laukums: {r[3]}\n")
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens gridas laukums.")
            materi = mater_combobox.get()
            conn = sqlite3.connect('grida.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id_mater FROM Material WHERE mater_veids LIKE ?", (materi,),)
            rezultati = cursor.fetchall()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet klienta vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt Materialu")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Platumu:",bg="#6F5100").pack()
    platums_entry = tk.Entry(logs)
    platums_entry.pack()


    mater_list()

    tk.Label(logs,text="pasutijuma1",bg="#6F5100").pack()
    mater_combobox = ttk.Combobox(logs,width=20,state="readonly",values= pasutijuma)
    mater_combobox.pack()

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


def pasutijuma_logs():
    pasutijuma_logs = tk.Toplevel()
    pasutijuma_logs.title("Klientu pārvaldība")
    pasutijuma_logs.geometry(f"300x250+{int((pasutijuma_logs.winfo_screenwidth())/2)-150}+{int((pasutijuma_logs.winfo_screenheight())/2)-125}")
    pasutijuma_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(pasutijuma_logs, text="Pievienot materialu", command=savienot_informaciju, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)

    '''meklēt_btn = tk.Button(pasutijuma_logs, text="Meklēt materialu", command=meklēt_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(pasutijuma_logs, text="Dzēst materialu", command=dzēst_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    dzēst_btn.pack(pady=10)'''

    iziet_btn = tk.Button(pasutijuma_logs, text="Iziet", command=pasutijuma_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)