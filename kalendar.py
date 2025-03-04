import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('Datumi.db')
cursor = conn.cursor()

def calendar_view():
    def print_sel():
        print(cal.selection_get())
        if cal.selection_get():
            cursor.execute("INSERT INTO Datums (datums) VALUES(?)",(f"{cal.selection_get()}",))
            conn.commit()
            messagebox.showinfo("Veiksmīgi","Datums pievienots!")
    
    top = tk.Toplevel(root)
    cal=Calendar(top,
                 font="Arial 14",selectmode='day',
                 cursor="hand1",year=2025,month=2,day=5)
    cal.pack(fill="both",expand=True)
    ttk.Button(top,text="ok",command=print_sel).pack()
root = tk.Tk()
s = ttk.Style(root)
root.geometry('160x160+500+300')
s.theme_use('clam')
ttk.Button(root,text='Calendar',command=calendar_view).pack(padx=10,pady=10)

root.mainloop()

def kalendar_logs():
    kalendar_logs = tk.Toplevel()
    kalendar_logs.title("Klientu pārvaldība")
    kalendar_logs.geometry(f"300x250+{int((kalendar_logs.winfo_screenwidth())/2)-150}+{int((kalendar_logs.winfo_screenheight())/2)-125}")
    kalendar_logs.configure(bg="#6F5100")

    pievienot_btn = tk.Button(kalendar_logs, text="Pievienot materialu", command=calendar_view, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    pievienot_btn.pack(pady=10)


    iziet_btn = tk.Button(kalendar_logs, text="Iziet", command=kalendar_logs.destroy, width=25, height=2, bg="#FFE86E",activebackground="yellow")
    iziet_btn.pack(pady=10)