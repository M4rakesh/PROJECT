import sqlite3
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox,ttk


conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def savieno_informaciju():
    def list_mater():
        global telefon1,laukums1
        conn= sqlite3.connect('grida.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Klients")
        telefon1 = []
        tel_all=cursor.fetchall()
        #print(tel_all)
        for tel in tel_all:
            telefon1.append(tel[3])
            print(tel[3])
        print(telefon1)
        cursor.execute("SELECT * FROM Laukums")
        laukums1=[]
        lauk_all=cursor.fetchall()
        print(lauk_all)
        
        for lauk in lauk_all:
            laukums1.append(lauk[2])
            print(lauk[2])
        print(laukums1)
    
        conn.close()

    def saglabat_info():
        try:
            tel_nr = tel_nr_combobox.get()
            
            if  not tel_nr:
                messagebox.showwarning("Brīdinājums, lūdzu izvēlēties telefona numuru!")
                return

            global telefon,laukums
            
            conn= sqlite3.connect('grida.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM Klients WHERE tel_nr = ?",(tel_nr,))
            tel_all=cursor.fetchone()
            conn.close()
            if tel_nr:
                    text=ttk.Label(logs,text=f"Vārds:{tel_all[1]}\nUzvārds{tel_all[2]}")
                    text.place(x=150,y=150)
            conn= sqlite3.connect('grida.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM Klients INNER JOIN Info ON Info.id_klients= Klients.id_klients INNER JOIN Material ON Info.id_mater= Material.id_mater WHERE tel_nr = ?",(tel_nr,))
            lauk_all=cursor.fetchone()
            print("asd",lauk_all[1],lauk_all[2],lauk_all[3],lauk_all[12])
            conn.close()
            if tel_nr:
                    text=ttk.Label(logs,text=f"Vārds:{lauk_all[1]}\nUzvārds:{lauk_all[2]}\nTelefons:{lauk_all[3]}\nMaterials:{lauk_all[12]}\nplatums:{lauk_all[13]}\ngarums{lauk_all[14]}")
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


    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_info,bg="yellow")
    saglabat_btn.pack(pady=10)
    
def pasutijuma_logs():
    pasutijuma_logs = tk.Toplevel()
    pasutijuma_logs.title("Pasutijums")
    pasutijuma_logs.geometry(f"300x300+{int((pasutijuma_logs.winfo_screenwidth())/2)-150}+{int((pasutijuma_logs.winfo_screenheight())/2)-150}")
    pasutijuma_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(pasutijuma_logs, text="Pievienot materialu", command=savieno_informaciju, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)

    iziet_btn = tk.Button(pasutijuma_logs, text="Iziet", command=pasutijuma_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)