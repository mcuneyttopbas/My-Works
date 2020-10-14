SadikHesap = {
    'ad':'Sadik Turan',
    'hesapNo':'13434323',
    'bakiye':3000,
    'ekHesap':2000
}
AliHesap = {
    'ad':'Ali Turan',
    'hesapNo':'12434323',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    bakiyeSorgula(SadikHesap)

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranizi Alabilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if (toplam >= miktar):

            ekHesapKullanimi = input("ek hesap kullanilsin mi (e/h)")

            if ekHesapKullanimi == "e":

                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar

                print("paranizi alabilirsiniz")
                bakiyeSorgula(SadikHesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
        else:
            print(f"Uzgunuz Bakiye Yetersiz")
            bakiyeSorgula(SadikHesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir. Ek Hesapinizda ise {hesap['ekHesap']} bulunmaktadir.")


paraCek(SadikHesap,3000)

paraCek(SadikHesap,1500)

paraCek(SadikHesap,1000)
