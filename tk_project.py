import sqlite3
import tkinter as tk
from tkinter import messagebox
from Klienti1 import klientu_logs
from Laukums_grida1 import laukums_logs
from materials1 import materials_logs
from allinfo1 import info_logs
from info1 import pasutijuma_logs


#galvenais logs ar pogam
def izveidot_galveno_logu():
    def klienti_poga():
        klientu_logs()

    def laukumi_poga():
        laukums_logs()

    def materiali_poga():
        materials_logs()

    def info_poga():
        info_logs()
    
    def pasutijuma_poga():
        pasutijuma_logs()
        #Tas ir pogas, kuras atver jaunu logu ar izveleto darbibu(klients,gridas laukums vai materials)
    
    logs = tk.Tk()
    logs.title("GLR")
    logs.geometry(f"300x300+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-150}")
    logs.configure(bg="#6F5100")
    Klients_btn = tk.Button(logs, text="Klienti", command=klienti_poga, width=20, height=2, bg="#FFE86E",activebackground="yellow")
    Klients_btn.pack(pady=10)#poga aktivize klienta logu

    treneri_btn = tk.Button(logs, text="Laukumi", command=laukumi_poga, width=20, height=2, bg="#FFE86E",activebackground="yellow")
    treneri_btn.pack(pady=10)#poga aktivize gridas laukuma logu

    apmeklejumi_btn = tk.Button(logs, text="Materiali", command=materiali_poga, width=20, height=2, bg="#FFE86E",activebackground="yellow")
    apmeklejumi_btn.pack(pady=10)#poga aktivize materiala logu

    info_btn = tk.Button(logs, text="Visa informacija", command=info_poga, width=20, height=2, bg="#FFE86E",activebackground="yellow")
    info_btn.pack(pady=10)#poga aktivize informacijas logu

    pasutijums_btn=tk.Button(logs, text="Pasutijums", command=pasutijuma_poga, width=20, height=2, bg="#FFE86E",activebackground="yellow")
    pasutijums_btn.pack(pady=10)#poga aktivize pasutijuma logu
    logs.mainloop()


if __name__ == "__main__":
    izveidot_galveno_logu()
    
#https://github.com/M4rakesh/PROJECT