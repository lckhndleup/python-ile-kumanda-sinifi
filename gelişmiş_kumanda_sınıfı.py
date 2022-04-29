"""
Proje 1
Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın.
"""

import random
import time

class Kumanda():
    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["","trt"],kanal="trt",kanal_sil=[],ebeveyn_mod="kapalı",parlaklık=0,mod_durumu="seçilmedi",zoom_durumu=5,kanal_numarası=[]):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        self.kanal_sil=kanal_sil
        self.ebeveyn_mod=ebeveyn_mod
        self.parlaklık=parlaklık
        self.mod_durumu=mod_durumu
        self.zoom_durumu=zoom_durumu
        self.kanal_numarası=kanal_numarası
    def tv_ac(self):
        if self.tv_durum=="kapalı":
            self.tv_durum="açık"
            print("televizyon açılıyor...")
        elif self.tv_durum=="açık":
            print("televizyon zaten açık...")
    def tv_kapat(self):
        if self.tv_durum=="kapalı":
            print("televizyon zaten kapalı..")
        else:
            print("televizyon kapanıyor...")
            self.tv_durum="kapalı"
    def kanal_silme(self):
        a=0
        for i in self.kanal_listesi:
            print(a,"nci kanal=",i)
            a+=1
        sil_kanal=int(input("silmek istediğiniz kanalı numarasını giriniz:"))
        print("kanal siliniyor...")
        time.sleep(1)
        self.kanal_listesi.pop(sil_kanal)
        self.kanal_sil.append(sil_kanal)
        print("kanal silindi...")
    def kanalno_degis(self):
        a=0
        kanallistesi=[]
        for i in self.kanal_listesi:
            print(a,"nci kanal=",i)
            kanallistesi.append(i)
            a+=1

        kanalno=input("değiştirmek istediğiniz iki kanalın numarasını aralarında ',' koyarak giriniz:")
        liste_kanal=kanalno.split(',')
        liste_kanal[0]=int(liste_kanal[0])
        liste_kanal[1]=int(liste_kanal[1])
        print("kanallar güncelleniyor...")
        time.sleep(0.5)
        yeni=self.kanal_listesi[liste_kanal[0]]
        #yeni1=self.kanal_listesi[liste_kanal[1]]
        #self.kanal_listesi[liste_kanal[0]]==self.kanal_listesi[liste_kanal[1]]
        #self.kanal_listesi[liste_kanal[1]]==self.kanal_listesi[liste_kanal[0]]
        self.kanal_listesi[liste_kanal[0]]=self.kanal_listesi[liste_kanal[1]]
        self.kanal_listesi[liste_kanal[1]]=yeni
        print("güncellenmiş kanal listesi:")
        b=0
        for i in self.kanal_listesi:
            print(b,"nci kanal:",i)
            b+=1


    def parlaklık_ayar(self):
        while True:
            deger=input("parlaklık değerini artırmak için:'>'\nazaltmak için:'<'çıkış için 'çıkış' yazınız...")

            if deger==">":
                if deger!=29:
                    self.parlaklık+=1
            elif deger=="<":
                if deger!=0:
                    self.parlaklık-=1
            else:
                print("çıkış yapılıyor..")
                break


    def mod_degis(self):
        print("Şu anki mod durumu=",self.mod_durumu)
        mod_listesi=["genel","sinema","spor","haber","nostalji","modern","belgesel"]
        a=0
        for i in mod_listesi:
            print(a,")","Mod seçenekleri:\n",i)
            a+=1
        mod_sec=int(input("istediğiniz modun numarasını giriniz:"))
        print("mod değiştiriiliyor..")
        time.sleep(0.5)
        self.mod_durumu=mod_listesi[mod_sec]
        print("mod durumu=",self.mod_durumu)


    def zoom_degis(self):

        while True:
            print("şu anki zoom durumu:",self.zoom_durumu)
            zoom_ayar=input("zoom artırmak için :'>' tuşuna azaltmak için :'<' tuşuna çıkış için:'çıkış'yazın")
            if zoom_ayar=="<":
                if self.zoom_durumu!=-11:
                    self.zoom_durumu-=1
            elif zoom_ayar==">":
                if self.zoom_durumu!=11:
                    self.zoom_durumu+=1
            else:
                print("zoom durumu güncellendi\nŞu anki zoom değeri:",self.zoom_durumu)
                print("çıkış yapılıyor...")
                break



    def ebeveyn_kontrol(self,şifre=270219):
        while True:
            password = int(input("ebeveyn ayarları için şifreyi giriniz:"))
            hak = 3
            if password == şifre:
                cevap=input("şifre doğru.Ebeveyn modunu açmak için 'açık' kapatmak için 'kapat' yazın:")
                if cevap=="açık":
                    self.ebeveyn_mod="açık"
                else:
                    self.ebeveyn_mod="kapalı"
                break


            elif password != şifre:
                print("yanlış giriş..")

                hak -= 1
                print("kalan hakkınız:",hak)
                if hak==0:
                    print("birçok kez yanlış giriş yapıldı..çıkış yapılıyor..")
                    break



    def ses_ayarları(self):
        while True:
            ses=input("sesi azaltmak için '<'\nsesi artırmak için '>'\nÇıkmak için 'çıkış' yazınız..")
            if ses=="<":
                if (self.tv_ses!=0):
                    self.tv_ses-=1
                print("ses:",self.tv_ses)
            elif ses==">":
                if self.tv_ses!=31:
                    self.tv_ses+=1
                print("ses:",self.tv_ses)
            else:
                print("Ses güncellendi:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor...")
        self.kanal_listesi.append(kanal_ismi)
        time.sleep(1)
        print("kanal eklendi..")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        print("şu anki kanal:",self.kanal_listesi[rastgele])
        self.kanal=self.kanal_listesi[rastgele]

    def __len__(self):
        return len(self.kanal_listesi)


    def __str__(self):
        return "tv durum:{}\ntv ses:{}\nKanal listesi:{}\nŞu anki Kanal:{}\nEbeveyn modu:{}\nMod durumu:{}\nzoom durumu:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal,self.ebeveyn_mod,self.mod_durumu,self.zoom_durumu)

kumanda=Kumanda()

print("""
Televizyon uygulaması:
1)Tv aç
2)Tv kapat
3)Ses ayarları
4)Kanal ekle
5)Kanal sayısını öğrenme
6)Rastgele kanala geçme
7)kanal silme
8)Tv bilgileri
9)kanal numarası değiştirme
10)ebeveyn ayarları
11)parlaklık ayarları
12)mod değiştir
13)zoom ayarları
çıkmak için  'q'ya basınız
""")

while True:
    işlem=input("işlemi giriniz:")
    if işlem=="q":
        print("çıkış yapılıyor..")
        break
    elif işlem=="1":
        kumanda.tv_ac()

    elif işlem=="2":
        kumanda.tv_kapat()
    elif işlem=="3":
        kumanda.ses_ayarları()
    elif işlem=="4":
        eklenecekler=input("Lütfen eklemek istediğiniz kanalları aralarında ',' koyarak yazınız")

        liste=eklenecekler.split(',')

        for i in liste:
            kumanda.kanal_ekle(i)
    elif işlem=="5":
        print("toplam kanal sayısı:",len(kumanda))
    elif işlem=="6":
        kumanda.rastgele_kanal()
    elif işlem=="7":
        kumanda.kanal_silme()
    elif işlem=="8":
        print(kumanda)
    elif işlem=="9":
        kumanda.kanalno_degis()
    elif işlem=="10":
        kumanda.ebeveyn_kontrol()
    elif işlem=="11":
        kumanda.parlaklık_ayar()
    elif işlem=="12":
        kumanda.mod_degis()
    elif işlem=="13":
        kumanda.zoom_degis()
    else:
        time.sleep(1)
        print("yanlış giriş yapıldı...\nÇıkış yapılıyor...")
        break
