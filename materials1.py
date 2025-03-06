import sqlite3
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox,ttk


conn = sqlite3.connect('grida.db')
cursor = conn.cursor()
#logs kur var pievienot jaunu materialu ar tas datiem(platums,garums u.c.)
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
#logs kur var pievienot materialu
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

#logs kur var atrasts materialu pēc platuma un materiala veida
def meklēt_materialu():
    def mater_list():
        global materials
        conn= sqlite3.connect('grida.db')
        cursor=conn.cursor()
        cursor.execute("SELECT mater_veids FROM Material GROUP BY mater_veids")
        materials = []
        mater_all=cursor.fetchall()
        for mater in mater_all:
            materials.append(mater[0])
        print(materials)
        conn.close()

#logs kur var atrasts materialu pēc platuma un materiala veida
    def atrast_materialu():
        platums = platums_entry.get()
        mater_veids = mater_combobox.get()
        print(mater_veids)
        if platums and mater_veids:
            print(platums)
            conn= sqlite3.connect('grida.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM Material WHERE platums LIKE ? and mater_veids LIKE ?", (f"%{platums}%",f"%{mater_veids}%"))
            print("sa")
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]}, {r[2]}, {r[3]}\n"
                    messagebox.showinfo("Rezultāti", f"{r[0]}: platums: {r[1]} garums: {r[2]}, Laukums: {r[3]}\n")
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens gridas laukums.")
            materi = mater_combobox.get()
            conn = sqlite3.connect('grida.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id_mater FROM Material WHERE mater_veids LIKE ?", (materi,),)
            rezultati = cursor.fetchall()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet platumu!")

    logs = tk.Toplevel()
    logs.title("Meklēt Materialu")#tas ir poga ar kuru izkas funkcija materialu mēklešāna
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Platumu:",bg="#6F5100").pack()#tas ir pēc kura mainīga funkcija mekle materialu
    platums_entry = tk.Entry(logs)
    platums_entry.pack()


    mater_list()

    tk.Label(logs,text="Materials1",bg="#6F5100").pack()#tas ir materiala veidu izvelešana
    mater_combobox = ttk.Combobox(logs,width=20,state="readonly",values= materials)
    mater_combobox.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_materialu,bg="yellow")#tas ir poga kura aktivize visu darbibu un izvada informaciju
    meklēt_btn.pack(pady=10)

#poga ar kuru izkas funkcija pievinot materialu
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

#galvenais logs kurš saists ar materilu
def materials_logs():
    materials_logs = tk.Toplevel()
    materials_logs.title("Klientu pārvaldība")
    materials_logs.geometry(f"300x250+{int((materials_logs.winfo_screenwidth())/2)-150}+{int((materials_logs.winfo_screenheight())/2)-125}")
    materials_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(materials_logs, text="Pievienot materialu", command=pievienot_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)#poga kura pievieno jaunu materialu

    meklēt_btn = tk.Button(materials_logs, text="Meklēt materialu", command=meklēt_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    meklēt_btn.pack(pady=10)#poga kura mēkle materialu

    dzēst_btn = tk.Button(materials_logs, text="Dzēst materialu", command=dzēst_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    dzēst_btn.pack(pady=10)#poga kura nodzēsa materialu

    iziet_btn = tk.Button(materials_logs, text="Iziet", command=materials_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)#poga ar kuru var iziet uz iepriekšejo logu