import itertools
import datetime
from datetime import time
import sqlite3 as db


    
class Klients:
    Klienta_vaards=""
    Klienta_uzvaards=""
    Klienta_PK=""
    Klienta_tel_numurs=""
    
    id_iter_kl = itertools.count()
    def info():
        with db.connect('grida.db') as con:
            cur=con.cursor()
            cur.execute("""SELECT * FROM Klients""")
            order=cur.fetchall()
            for i in order:
                print(i)

    def __init__(self,_vaards,_uzvaards,_pk,_tel_numurs):
        self.Klienta_id = next(self.id_iter_kl) + 1
        self.Klienta_vaards=_vaards
        self.Klienta_uzvaards=_uzvaards
        self.Klienta_PK=_pk
        self.Klienta_tel_numurs=_tel_numurs

    def Klienta_info(self):
        return [self.Klienta_id,self.Klienta_vaards,self.Klienta_uzvaards,self.Klienta_PK,self.Klienta_tel_numurs]

    def Klientu_info_print(self):
        print("Klienta vārds: "+ str(self.Klienta_vaards))
        print("Klienta uzvārds: " + str(self.Klienta_uzvaards))
        print("Klienta personas kods : "+ str(self.Klienta_PK))
        print("Klienta Tel. numurs : " + str(self.Klienta_tel_numurs)) 
    def Klientt():
        with db.connect('grida.db') as con:
            cur=con.cursor()
            id_klients=int(input("Ievadiet Klienta id: "))
            vards=input("Ievadiet Klienta vardu: ")
            uzvards=input("Ievadiet Klienta uzvardu: ")
            tel_nr=input("Ievadiet Klienta telefona numuru: ")
            cur.execute("""INSERT INTO Klients(id_klients,vards,uzvards,tel_nr) VALUES(?,?,?,?)""",(id_klients,vards,uzvards,tel_nr))
    def delete_data():
        with db.connect('grida.db') as con:
            a=input("Ievadiet ID: ")
            con.execute(f"DELETE from Klients where id_klients={a};")
    def atjaunot_datus():
        with db.connect('grida.db') as con:
            g=input("Ievadiet Klienta ID: ")
            h=input("Ievadiet jaunu telefonu: ")
            con.execute(f"UPDATE Klients set tel_nr={h} where id_klients={g}")
    def atrast():
        with db.connect('grida.db') as con:
            cur=con.cursor()
            while True:
                t=int(input("Ievadiet id,kuru velaties atrast vai 0 ja pardoma"))
                if t != 0 :
                    print(f"Klients ar ID {t} tika atrasta  !")
                    cur.execute(f"SELECT * FROM Klients WHERE id_klients = {t}")
                    con.commit()
                    info=cur.fetchall()
                    for rinda in info:
                        print(rinda)                       
                elif t == 0:
                    print("Jus atsutija atpakaļ!")
                    break
                else:
                    pass
    def join_data():
        with db.connect('grida.db') as con:
            cur=con.cursor()
            cur.execute("SELECT Vards,Uzvards,tel_nr From Klients INNER JOIN Info ON Klients.id_klients == Info.id_klients")
            #c=input("Ievadiet Klienta ID: ")
            order=cur.fetchall()
            for i in order:
                print(i)


Klient=[]
    
'''with open("Klienti.txt","a",encoding="utf-8") as fail:
    while True:
        

        again=input("Vai jūs gribat ivadiet vēl vienu personu: jā/nē ")
        if again =="jā":
            CilvekaVards=(input("Ievadiet savu vardu: "))
            CilvekaUzards=(input("Ievadiet savu uzvardu: "))
            PersonKod=(input("Ievadiet savu personas koda: "))
            TelNr=(input("Ievadiet savu telefonu: "))
            kli1=Klients(CilvekaVards,CilvekaUzards,PersonKod,TelNr)
            print(kli1.Klienta_id)
            kli1.Klientu_info_print()   
            
            fail.write(f"Klienta vards: {CilvekaVards} Klienta uzvards: {CilvekaUzards} Klienta personas kods: {PersonKod} Klienta telefona numurs:{TelNr}"+"\n")  
            
            
        else:
            print("Paldies par uzmanibu!")
            break'''
class Laukums:
    
    Platums_gridai = 0
    Garums_gridai = 0
     


    id_iter= itertools.count()
    def __init__(self,plat_g=None,gar_g=None):
        self.gridasId=next(self.id_iter)+1
        self.Platums_gridai = plat_g
        self.Garums_gridai = gar_g
    
    def aprekinasana(self):
        self.Laukuma= self.Platums_gridai * self.Garums_gridai

        return self.Laukuma
        
        
    
    def Laukuma_info(self):
        return [
            self.Platums_gridai,self.Garums_gridai
        ]
    
    def Laukuma_info_print(self):
        print("Paltums gridai: "+ str(self.Platums_gridai))
        print("Garums gridai: " + str(self.Garums_gridai))
        print("Laukums gridai: "+ str(self.Laukuma))
    def Laukum():
        with db.connect('grida.db') as con:
            cur=con.cursor()
            id_lauk=int(input("Ievadiet Laukuma id: "))
            platums=input("Ievadiet platumu: ")
            garums=input("Ievadiet garumu: ")
            laukums=platums*garums
            cur.execute("""INSERT INTO Laukums(id_lauk,platums,garums,laukums) VALUES(?,?,?,?)""",(id_lauk,platums,garums,laukums))
            con.commit()
    


class Material:
    Laminats=''
    Flize=''
    Linolejs=''
    Garums=0
    Platums=0
    Daudzums=0
    def __init__(self,gar,plat,daudz):
        self.Garums=gar
        self.Platums=plat
        self.Daudzums=daudz
        
    def Material_info(self):
        int(input("Kadu materialu jūs izvelejas: (Linolejs,Frizes,Lamināts)"))
    def Materials():
        with db.connect('grida.db') as con:
            cur=con.cursor()
            id_mater=int(input("materiala id: "))
            mater_veids=input("Ievadiet material veidu: ")
            mater_izmers=input("Ievadiet materiala izmeru: ")
            cur.execute("""INSERT INTO Material(id_mater,mater_veids,mater_izmers) VALUES(?,?,?)""",(id_mater,mater_veids,mater_izmers))
            con.commit()
def main():
    #load_data()
    #find_organization_by_id()
    #count_organizations()
    #organization_exists()
    #list_organition_ids()
    #delete_organization_by_id()
    while (True):
        response=input('(1)Pievieno Klientu (2) Izprinte Klienta datus (3)divas datas (4)dzest datu (5)meklet datus (6)atjaunot datus (7)Iziet ')
        if response=='1':
            Klients.Klientt()
            Laukums.Laukum()
            Material.Materials()
        elif response=='2':
            Klients.info()
        elif response=='3':
            Klients.join_data()
        elif response=='4':
            Klients.delete_data()
        elif response=='5':
            Klients.atrast()
        elif response=='6':
            Klients.atjaunot_datus()
        elif response=='7':
            print('gg,ja livaju tima rakov!')
            exit()
            
        else:
            print('Choose a number between 1 and 7')
            continue
main()

    

#https://github.com/M4rakesh/uzd/blob/main/mechta.py