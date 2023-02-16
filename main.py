#############################################
#                                           #
#          oturum otomasyon sistemi         #
#                                           #
#           yapımcı bilgileri               #
#           github - gladyotr               #
#           instagram - @gladbey            #
#           gmail - gladyotr123@gmail.com   #
#                                           #
#               berat karaca <3             #
#############################################

from tkinter import *
from modules import *
def girdi():
    eposta = geposta.get()
    sifre = gsifre.get()
    parola = hesaplar[eposta]
    if parola == sifre:
        sucpencere  = Tk()
        sucpencere.geometry("500x500")
        sucpencere.title("Kayıt Ol | Karaca SOFTWARE LTD. ŞTİ.")
        sucpencere.config(bg="black")

        pencere.destroy()

        yazi = Label(sucpencere)
        yazi.config(text="giris basarılı", width=15, height=2, bg="green", fg="white", font=("arial",30))
        """berat karaca"""
        yazi.place(x="75",y="50")
    else:
        print("eposta yada sifre yanlıs")

pencere = Tk()
pencere.title("Giriş Yap | Karaca SOFTWARE LTD. ŞTİ.")
pencere.geometry("500x500")
pencere.config(bg="black")

yazi = Label(pencere)
yazi.config(text="GİRİŞ YAP", width=15, height=2, bg="black", fg="white", font=("arial",30))
yazi.place(x="75",y="50")

gyazi = Label(pencere)
gyazi.config(text="eposta", width=15, height=2, bg="black", fg="white")
gyazi.place(x="75",y="140")

geposta = Entry(pencere)
geposta.config(width=35)
geposta.place(x="150",y="150")

syazi = Label(pencere)
syazi.config(text="sifre", width=15, height=2,bg="black", fg="white")
syazi.place(x="75",y="190")

gsifre = Entry(pencere)
gsifre.config(width=35)
gsifre.place(x="150",y="200")

giris = Button(pencere)
giris.config(text="giris yap",width=15, height=2, bg="grey" ,command=girdi)
giris.place(x="200",y="250")

kayit = Button(pencere)
kayit.config(text="kayit ol",width=15, height=2, bg="black", fg="blue" ,command=kayitol)
kayit.place(x="200",y="350")
mainloop()

