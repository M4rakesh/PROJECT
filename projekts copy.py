import itertools
import datetime
from datetime import time

class Klients:
    Klienta_vaards=""
    Klienta_uzvaards=""
    Klienta_PK=""
    Klienta_tel_numurs=""
    
    id_iter_kl = itertools.count()

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

Klient=[]
with open("Klienti.txt","a",encoding="utf-8") as fail:
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
            break
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
    def Material_info_print():
        
a=int(input("Ievadiet garumu: "))
b=int(input("Ievadit platumu: "))
s1=Laukums(b,a)
s1.aprekinasana()
s1.Laukuma_info_print()
    

#https://github.com/M4rakesh/uzd/blob/main/mechta.py