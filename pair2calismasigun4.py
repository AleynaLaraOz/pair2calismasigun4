def toplama():
    sayi1 = int(input("İlk sayiyi Giriniz.")) 
    sayi2 = int(input("İkinci sayiyi Giriniz."))
    print(sayi1+sayi2)

def cikarma():
    sayi1 = int(input("İlk sayiyi Giriniz.")) 
    sayi2 = int(input("İkinci sayiyi Giriniz."))
    print(sayi1-sayi2) 

def bolme():
    sayi1 = int(input("İlk sayiyi Giriniz.")) 
    sayi2 = int(input("İkinci sayiyi Giriniz."))
    if sayi2 ==0:
        print("Geçersiz sayi girdiniz.")
    else:
        print(sayi1/sayi2) 

def carpma():
    sayi1 = int(input("İlk sayiyi Giriniz.")) 
    sayi2 = int(input("İkinci sayiyi Giriniz."))
    print(sayi1sayi2) 

def modAlma():
    sayi1 = int(input("İlk sayiyi Giriniz.")) 
    sayi2 = int(input("İkinci sayiyi Giriniz."))
    print(sayi1%sayi2) 

a=1

while a==1:
    islem = input("Bir işlem seçiniz:")

    if islem=="q":
        a=0

    elif islem == "+":
        toplama() 

    elif islem == "-":
        cikarma()

    elif islem == "":
        carpma()

    elif islem == "/":
        bolme()



    elif islem == "%":
        modAlma()

    else:
       print("Geçersiz giriş tekrar deneyiniz")