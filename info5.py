import sqlite3
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox,ttk


conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def savieno_informaciju():
    def list_mater():
        global telefon1,laukums1,platums1, garums1, materials1, materials2, materials3
        conn= sqlite3.connect('grida.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Klients")
        telefon1 = []
        tel_all=cursor.fetchall()
        print("tel",tel_all)
        for tel in tel_all:
            telefon1.append(tel[3])
            print(tel[3])
        print(telefon1)
        cursor.execute("SELECT * FROM Laukums")
        laukums1=[]
        platums1=[]
        garums1=[]
        lauk_all=cursor.fetchall()
        for lauk in lauk_all:
            platums1.append(lauk[1])
            garums1.append(lauk[2])
            laukums1.append(lauk[3])
        print(lauk_all)
        cursor.execute("SELECT * FROM Material")
        materials1=[]
        materials2=[]
        materials3=[]
        mater_all=cursor.fetchall()
        
        for mater in mater_all:
            materials1.append(mater[1])
            materials2.append(mater[2])
            materials3.append(mater[3])

        conn.close()

    def saglabat_info():
        try:
            tel_nr = tel_nr_combobox.get()
            platums=platums_combobox.get()
            garums=garums_combobox.get()
            materials=materials_combobox.get()
            if  not tel_nr:
                messagebox.showwarning("Brīdinājums, lūdzu izvēlēties telefona numuru!")
                return

            global telefon,laukums
            conn= sqlite3.connect('grida.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM Klients WHERE tel_nr = ?",(tel_nr,))
            tel_all=cursor.fetchone()
            cursor.execute("SELECT * FROM Laukums WHERE platums = ? ",(platums,))
            tel_all=cursor.fetchone()
            cursor.execute("SELECT * FROM Laukums WHERE garums = ?",(garums,))
            mater_all=cursor.fetchone()
            cursor.execute("SELECT * FROM Material WHERE mater_veids = ?",(materials,))
            mater_all=cursor.fetchone()

            conn.close()
            

            if tel_nr:
                    print("tel",tel_all)
                    text=ttk.Label(logs,text=f"Vārds:{mater_all[1]}\nUzvārds{mater_all[2]}\nPlatums:{tel_all[1]} Garums{tel_all[2]}")
                    text.place(x=960,y=540)
            else:
                messagebox.showwarning("Brīdinājums, lūdzu izvēlēties telefona numuru!")

            conn= sqlite3.connect('grida.db')
            cursor=conn.cursor()

            conn.close()

            if mater_all:
                    text=ttk.Label(logs,text=f"Platums:{mater_all[2]} Garums{mater_all[3]}")
                    text.place(x=150,y=150)
            else:
                messagebox.showwarning("Brīdinājums, lūdzu izvēlēties telefona numuru!")

        except Exception as e:
            messagebox.showerror("Kļūda", f"Neizdevās parādīt informāciju: {e}")


    logs = tk.Toplevel()
    logs.title("Pievienot pasutijumu")
    logs.geometry(f"300x300+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-150}")
    logs.configure(bg="#6F5100")

    list_mater()
    tk.Label(logs, text="telefon:",bg="#6F5100").pack()
    tel_nr_combobox = ttk.Combobox(logs,width=20,state="readonly",value=telefon1)
    tel_nr_combobox.pack()

    tk.Label(logs, text="platums:",bg="#6F5100").pack()
    platums_combobox = ttk.Combobox(logs,width=20,state="readonly",value=platums1)
    platums_combobox.pack()

    tk.Label(logs, text="garums:",bg="#6F5100").pack()
    garums_combobox = ttk.Combobox(logs,width=20,state="readonly",value=garums1)
    garums_combobox.pack()

    tk.Label(logs, text="materials:",bg="#6F5100").pack()
    materials_combobox = ttk.Combobox(logs,width=20,state="readonly",value=materials1)
    materials_combobox.pack()
    
    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_info,bg="yellow")
    saglabat_btn.pack(pady=10)
    
def pasutijuma_logs():
    pasutijuma_logs = tk.Toplevel()
    pasutijuma_logs.title("Klientu pārvaldība")
    pasutijuma_logs.geometry(f"300x300+{int((pasutijuma_logs.winfo_screenwidth())/2)-150}+{int((pasutijuma_logs.winfo_screenheight())/2)-150}")
    pasutijuma_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(pasutijuma_logs, text="Pievienot materialu", command=savieno_informaciju, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)

    iziet_btn = tk.Button(pasutijuma_logs, text="Iziet", command=pasutijuma_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)