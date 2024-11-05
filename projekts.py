import itertools
import datetime
from datetime import time

class Laukums:
    
    Platums_gridai = 0
    Garums_gridai = 0
     


    id_iter= itertools.count()
    def __init__(self,plat_g=None,gar_g=None):
        self.gridasId=next(self.id_iter)+1
        self.Platums_gridai = plat_g
        self.Garums_gridai = gar_g
    
    def aprekinasana(self):
        Laukuma= self.Platums_gridai * self.Garums_gridai
        return Laukuma
        
    
    def Laukuma_info(self):
        return [
            self.Platums_gridai,self.Garums_gridai
        ]
    
    def Laukuma_info_print(self):
        print("Paltums gridai: "+ str(self.Platums_gridai))
        print("Garums gridai: " + str(self.Garums_gridai))
        
    
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

    '''def Klienta_info(self):
        print("Klienta vards:"+ self.Klienta_vaards)
        print("Klienta uzvards:"+self.Klienta_uzvaards)
        print("Klienta personas kods:"+self.Klienta_PK)
        print("Klienta telefona numurs:"+self.Klienta_tel_numurs)'''

    def Klientu_info_print(self):
        print("Klienta vārds: "+ str(self.Klienta_vaards))
        print("Klienta uzvārds: " + str(self.Klienta_uzvaards))
        print("Klienta personas kods : "+ str(self.Klienta_PK))
        print("Klienta Tel. numurs : " + str(self.Klienta_tel_numurs)) 

class Izmantosana:
    Pakalpojuma_saakuma_laiks= 0
    Pakalpojuma_beigu_laiks=0
    Pakalpojuma_datums=0
    Izmantosdana_cena_stunda=10
    id_pakalpojums=0
    id_klients=0
    Izmantosana_id=0

    id_iter_izmantosana= itertools.count()

    def Cena_kopa(self):
        kopeja_cena=self.Izmantosdana_cena_stunda*(((self.Pakalpojuma_beigu_laiks - self.Pakalpojuma_saakuma_laiks)))
        return kopeja_cena
    
    def Izmantosana_info_print(self):
        print("Pakalpojuma sakuma laiks:"+ str(self.Pakalpojuma_saakuma_laiks))
        print("Pakalpojuma beigu laiks:"+ str(self.Pakalpojuma_beigu_laiks))
        print("Pakalpojums id:"+ str(self.id_pakalpojums))
        print("Klients id:"+ str(self.id_klients))
        print("Pakalpojuma cena stunda, EUR:"+str(self.Izmantosdana_cena_stunda)+"\n")
s1=Laukums(5,10)
s1.aprekinasana()
s1.Laukuma_info_print()
'''Klient=[]
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
    #kli1.Klienta_info()
            kli1.Klientu_info_print()   
            
            fail.write(f"Klienta vards: {CilvekaVards} Klienta uzvards: {CilvekaUzards} Klienta personas kods: {PersonKod} Klienta telefona numurs:{TelNr}"+"\n")  
            
            #for klienti in Klient:
                #fail.write(klienti + "\n")
        else:
            print("Paldies par uzmanibu!")
            break
    '''