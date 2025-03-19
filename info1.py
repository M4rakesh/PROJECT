import sqlite3
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox,ttk


conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def savieno_informaciju():
    def list_mater():
        global telefon
        conn= sqlite3.connect('grida.db')
        cursor=conn.cursor()
        cursor.execute("SELECT tel_nr FROM Klients")
        telefon = []
        tel_all=cursor.fetchall()
        for tel in tel_all:
            telefon.append(tel[0])
        print(telefon)
        cursor.execute("SELECT id_klients FROM Klients")
        kliientu=[]
        klie_all=cursor.fetchall()
        for klie in klie_all:
            kliientu.append(klie[0])
        print(kliientu)
        conn.close()
        conn.close()
        
    def saglabat_informaciju():
        #id_mater = id_mater_combobox.get()
        #id_klients = id_klients_combobox.get()
        #id_lauk = id_lauk_combobox.get()
        #mater_daudzums = mater_daudzums_combobox.get()
        #kopcena = kopcena_combobox.get()
        tel_nr = tel_nr_combobox.get()
        #datums = datums_combobox.get()
    

        if tel_nr:
            cursor.execute(
                "INSERT INTO Klients (tel_nr) VALUES (?)",
                (tel_nr))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "pasutijuma pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot pasutijumu")
    logs.geometry(f"300x300+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-150}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Id_meteriala:",bg="#6F5100").pack()
   # id_mater_combobox = ttk.Combobox(logs,width=20,state="readonly",value=materials)
   #id_mater_combobox.pack()
    list_mater()
    tk.Label(logs, text="telefon:",bg="#6F5100").pack()
    tel_nr_combobox = ttk.Combobox(logs,width=20,state="readonly",value=telefon)
    tel_nr_combobox.pack()

    tk.Label(logs, text="vārds:",bg="#6F5100").pack()
    id_klients_combobox = ttk.Combobox(logs,width=20,state="readonly",)
    id_klients_combobox.pack()

    tk.Label(logs, text="uzvārds",bg="#6F5100").pack()
    id_lauk_combobox = ttk.Combobox(logs,width=20,state="readonly",)
    id_lauk_combobox.pack()

    tk.Label(logs, text="materiala_daudzums",bg="#6F5100").pack()
    mater_daudzums_combobox = ttk.Combobox(logs,width=20,state="readonly",)
    mater_daudzums_combobox.pack()

    tk.Label(logs, text="kopcena",bg="#6F5100").pack()
    kopcena_combobox = ttk.Combobox(logs,width=20,state="readonly",)
    kopcena_combobox.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_informaciju,bg="yellow")
    saglabat_btn.pack(pady=10)
    
def pasutijuma_logs():
    pasutijuma_logs = tk.Toplevel()
    pasutijuma_logs.title("Klientu pārvaldība")
    pasutijuma_logs.geometry(f"300x300+{int((pasutijuma_logs.winfo_screenwidth())/2)-150}+{int((pasutijuma_logs.winfo_screenheight())/2)-150}")
    pasutijuma_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(pasutijuma_logs, text="Pievienot materialu", command=savieno_informaciju, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)

    '''meklēt_btn = tk.Button(pasutijuma_logs, text="Meklēt materialu", command=meklēt_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(pasutijuma_logs, text="Dzēst materialu", command=dzēst_materialu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    dzēst_btn.pack(pady=10)'''

    iziet_btn = tk.Button(pasutijuma_logs, text="Iziet", command=pasutijuma_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)