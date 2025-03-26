import sqlite3
import tkinter as tk
from tkinter import messagebox
import re

conn = sqlite3.connect('grida.db')
cursor = conn.cursor()
#logs kur var pievinot klientu

def pievienot_klientu():
    def saglabat_klientu():
        try:
            vards = vards_entry.get()
            uzvards = uzvards_entry.get()             
            tel_nr = tel_nr_entry.get()

            pattern = r'^[A-ZĀ-Ž][a-zā-ž]+$|^[A-ZĀ-Ž][a-zā-ž]+\s+[A-ZĀ-Ž]{1}[a-zā-ž]+$'
            pattern2 = r'^[A-ZĀ-Ž][a-zā-ž]+$|^[A-ZĀ-Ž][a-zā-ž]+\s+[A-ZĀ-Ž]{1}[a-zā-ž]+$'
            
            if not re.match(pattern, vards):
                messagebox.showinfo("Rezultāts", "Vards nav derīga!")
            if not re.match(pattern2, uzvards):
                messagebox.showinfo("Rezultāts", "Uzards nav derīga!")
            else:
            
                
                if vards and uzvards and tel_nr.isdigit():
                        if vards and uzvards:
                            cursor.execute("SELECT vards,uzvards FROM Klients WHERE vards LIKE ? and uzvards LIKE ?", (f"%{vards}%",f"%{uzvards}%"))
                            rezultati = cursor.fetchall()
                            if rezultati:
                                rezultati_str = ""
                                for r in rezultati:
                                    rezultati_str += f"{r[0]}: {r[1]} \n"
                                    messagebox.showinfo("Rezultāts", f"{r[0]} {r[1]}, klientu ekseste sistema!")
                                    
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
        except:
            print("error.")
    logs = tk.Toplevel()
    logs.title("Pievienot Klientu")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Vārds:",bg="#6F5100").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    tk.Label(logs, text="Uzvārds:",bg="#6F5100").pack()
    uzvards_entry = tk.Entry(logs)
    uzvards_entry.pack()

    tk.Label(logs, text="Tālrunis:",bg="#6F5100").pack()
    tel_nr_entry = tk.Entry(logs)
    tel_nr_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_klientu,bg="yellow")
    saglabat_btn.pack(pady=10)

#logs kur var atrast informaciju par klientu
def meklēt_klientu():
    def atrast_klientu():
        try:
            vards = vards_entry.get()

            pattern = r'^[A-ZĀ-Ž][a-zā-ž]+$|^[A-ZĀ-Ž][a-zā-ž]+\s+[A-ZĀ-Ž]{1}[a-zā-ž]+$'

        
            if not re.match(pattern, vards):
                messagebox.showinfo("Rezultāts", "Vards nav derīga!")

            else:
                if vards:
                    cursor.execute("SELECT * FROM Klients WHERE vards LIKE ?", (f"%{vards}%",))
                    rezultati = cursor.fetchall()
                    if rezultati:
                        rezultati_str = ""
                        for r in rezultati:
                            rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
                            messagebox.showinfo("Rezultāti", f"{r[0]}: Vards: {r[1]} Uzvards: {r[2]}, Talrunis: {r[3]}\n")
                    else:
                        messagebox.showinfo("Rezultāti", "Netika atrasts neviens Klients.")
                else:
                    messagebox.showerror("Kļūda", "Lūdzu, ievadiet klienta vārdu!")
        except Exception as e:
            print("error!!!")
    logs = tk.Toplevel()
    logs.title("Meklēt Klientu")
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")

    tk.Label(logs, text="Klienta vārds:",bg="#6F5100").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_klientu,bg="yellow")
    meklēt_btn.pack(pady=10)

#logs kur var nodzēst informaciju par klientu
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
    logs.geometry(f"300x200+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-100}")
    logs.configure(bg="#6F5100")
    tk.Label(logs, text="Klienta ID:",bg="#6F5100").pack()
    id_klientu_entry = tk.Entry(logs)
    id_klientu_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_klientu_no_db,bg="yellow")
    dzēst_btn.pack(pady=10)


def klientu_logs():
    klientu_logs = tk.Toplevel()
    klientu_logs.title("Klientu pārvaldība")
    klientu_logs.geometry(f"300x250+{int((klientu_logs.winfo_screenwidth())/2)-150}+{int((klientu_logs.winfo_screenheight())/2)-125}")
    klientu_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(klientu_logs, text="Pievienot klientu", command=pievienot_klientu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)#poga aktivize pievinot klientu logu

    meklēt_btn = tk.Button(klientu_logs, text="Meklēt klientu", command=meklēt_klientu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    meklēt_btn.pack(pady=10)#poga aktivize mēklet klientu logu

    dzēst_btn = tk.Button(klientu_logs, text="Dzēst klientu", command=dzēst_klientu, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    dzēst_btn.pack(pady=10)#poga aktivize nodzēst klientu logu

    iziet_btn = tk.Button(klientu_logs, text="Iziet", command=klientu_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)#poga iziet no klientu loga