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

hesaplar={"gladyo@gmail.com":"merhaba"}


def kayitol():
    def kayityap():
        eposta = keposta.get()
        sifre = ksifre.get()
        hesaplar[eposta] = sifre
        print(hesaplar)
        kpencere.destroy()


    kpencere  = Tk()
    kpencere.geometry("500x500")
    kpencere.title("Kayıt Ol | Karaca SOFTWARE LTD. ŞTİ.")
    kpencere.config(bg="black")

    yazi = Label(kpencere)
    yazi.config(text="KAYİT OL", width=15, height=2, bg="black", fg="white", font=("arial",30))
    yazi.place(x="75",y="50")

    kgyazi = Label(kpencere)
    kgyazi.config(text="eposta", width=15, height=2, bg="black", fg="white")
    kgyazi.place(x="75",y="140")

    keposta = Entry(kpencere)
    keposta.config(width=35)
    keposta.place(x="150",y="150")

    ksyazi = Label(kpencere)
    ksyazi.config(text="sifre", width=15, height=2,bg="black", fg="white")
    ksyazi.place(x="75",y="190")

    ksifre = Entry(kpencere)
    ksifre.config(width=35)
    ksifre.place(x="150",y="200")

    kayit = Button(kpencere)
    kayit.config(text="kayit ol",width=15, height=2, bg="grey" ,command=kayityap)
    kayit.place(x="200",y="250")
    mainloop()

