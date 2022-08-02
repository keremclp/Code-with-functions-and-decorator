def ekstra(func):
    def can():
        print("Welcome to program....")
        func()
        print("we are waiting for you again....")
    return can

@ekstra
def kerem():
    kullanıcı_ismi = input("Please enter your username(Hint : admin): ")

    if kullanıcı_ismi == "admin":
        başlangıç_değeri = int(input("Enter the initial value: "))
        artış_değeri = int(input("Enter the increment value: "))
        bitiş_değeri = int(input("Enter the end value: "))

        liste = list()
        toplam = 0
        for sayı in range(başlangıç_değeri,bitiş_değeri,artış_değeri):
            liste.append(sayı)
            toplam += sayı
        print(liste)
        print("Sum of numbers in the list: ",toplam)


    elif kullanıcı_ismi == "uye":
        bitiş_değeri = int(input("Enter the end value: "))
        liste= list()
        toplam = 0
        for sayı in range(1,bitiş_değeri,1):
            liste.append(sayı)
            toplam += sayı
        print(liste)
        print("Sum of numbers in the list: ",toplam)

    else:
        print("Please enter a valid username...")

kerem()