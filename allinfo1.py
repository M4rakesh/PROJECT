import sqlite3
import tkinter as tk
import tkinter as ttk
from tkinter import messagebox,ttk


conn = sqlite3.connect('grida.db')
cursor = conn.cursor()
print("123")
#logs kur izvada visu informaciju kur raksits par vārdu,laukumu,materilu
def visa_informacija():
    print("12334")
    global telefon1,laukums1,platums1, garums1, materials1, materials2, materials3
    conn= sqlite3.connect('grida.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Klients")
    telefon1 = []
    tel_all=cursor.fetchall()
    print("tell_all", tel_all)
    for tel in tel_all:
            telefon1.append(tel[3])

    def show_infoo():
        print("12335")
        id_info =mater_combobox.get()
        print("1233")
        if id_info:
            conn= sqlite3.connect('grida.db')
            cursor=conn.cursor()
            #cursor.execute("SELECT * FROM Info INNER JOIN Klients ON Klients.id_klients= Info.id_klients INNER JOIN Laukums ON Laukums.id_lauk= Info.id_lauk INNER JOIN Material ON Info.id_mater= Material.id_mater WHERE Info.id_info LIKE ? ", (f"%{id_info}%",) )    
            cursor.execute("SELECT * FROM Klients WHERE id_klients LIKE ?",(id_info,))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
                    tk.Label(logs, text=f"Rezultāti\n Vārds:{r[0]} \n Klients: {r[1]}\n Laukums: {r[2]}\n Materials:{r[3]}\n").pack()
                    try:        
                        mater_veids = mater_combobox.get()
                        if  not mater_veids:
                            messagebox.showwarning("Brīdinājums, lūdzu izvēlēties telefona numuru!")
                            return

                        global telefon,laukums, tel_all
                        conn= sqlite3.connect('grida.db')
                        cursor=conn.cursor()
                        cursor.execute("SELECT * FROM Klients WHERE tel_nr = ?",(mater_veids,))
                        tel_all=cursor.fetchone()
                        conn.close()
                        if mater_veids:
                                text=ttk.Label(logs,text=f"Vārds:{tel_all[1]}\nUzvārds{tel_all[2]}")
                                text.place(x=150,y=150)
                        else:
                            messagebox.showwarning("Brīdinājums, lūdzu izvēlēties telefona numuru!")
                    except Exception as e:
                        messagebox.showerror("Kļūda", f"Neizdevās parādīt informāciju: {e}")

            else:
                messagebox.showinfo("Rezultāti", f"Netika atrasts neviens klients ar id {id_info}.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet korektu klienta id!")
    logs = tk.Toplevel()
    logs.title("Klienta informācija")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")
    print("vdgrferfjhtyjjtyjtyjyjtyjtyjtyjyefe")

    tk.Label(logs,text="Materials1",bg="#6F5100").pack()#tas ir materiala veidu izvelešana
    mater_combobox = ttk.Combobox(logs,width=20,state="readonly",values= telefon1)
    mater_combobox.pack()
    print("vdgrferfehghghghgfe")

    tk.Label(logs, text=" id:",bg="#6F5100").pack()
    id_info_entry = tk.Entry(logs)
    id_info_entry.pack()
    print("vdgrferfefe")

    meklēt_btn = tk.Button(logs, text="Meklēt", command=show_infoo,overrelief="ridge",bg="yellow")
    meklēt_btn.pack(pady=10)

def info_logs():
    info_logs = tk.Toplevel()
    info_logs.title("Informacija par klientu")
    info_logs.geometry(f"300x250+{int((info_logs.winfo_screenwidth())/2)-150}+{int((info_logs.winfo_screenheight())/2)-125}")
    info_logs.configure(bg="#6F5100")

    radit_btn = tk.Button(info_logs, text="Atrast info", command=visa_informacija, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    radit_btn.pack(pady=10)