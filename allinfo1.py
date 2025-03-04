import sqlite3
import tkinter as tk
from tkinter import messagebox
#from kalendar import kalendar_logs

conn = sqlite3.connect('grida.db')
cursor = conn.cursor()

def kalendars():
    def show_infoo():
        id_info =id_info_entry.get()
        if id_info:
            cursor.execute("SELECT * FROM Info INNER JOIN Klients ON Klients.id_klients= Info.id_klients INNER JOIN Laukums ON Laukums.id_lauk= Info.id_lauk INNER JOIN Material ON Info.id_mater= Material.id_mater WHERE Info.id_info LIKE ? ", (f"%{id_info}%",) )    
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
                    tk.Label(logs, text=f"Rezultāti\n Vārds:{r[0]} \n Klients: {r[1]}\n Laukums: {r[2]}\n Materials:{r[3]}\n").pack()
            else:
                messagebox.showinfo("Rezultāti", f"Netika atrasts neviens klients ar id {id_info}.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet korektu klienta id!")
    logs = tk.Toplevel()
    logs.title("Klienta informācija")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text=" kalendars",bg="#6F5100").pack()
    id_info_entry = tk.Entry(logs)
    id_info_entry.pack()
    
    tk.Label(logs, text=" id:",bg="#6F5100").pack()
    id_info_entry = tk.Entry(logs)
    id_info_entry.pack()
    meklēt_btn = tk.Button(logs, text="Meklēt", command=show_infoo,overrelief="ridge",bg="yellow")
    meklēt_btn.pack(pady=10)

def info_logs():
    info_logs = tk.Toplevel()
    info_logs.title("Klientu pārvaldība")
    info_logs.geometry(f"300x250+{int((info_logs.winfo_screenwidth())/2)-150}+{int((info_logs.winfo_screenheight())/2)-125}")
    info_logs.configure(bg="#6F5100")

    radit_btn = tk.Button(info_logs, text="Atrast info", command=kalendars, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    radit_btn.pack(pady=10)