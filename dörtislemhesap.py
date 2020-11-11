islem = [ "+" , "-" , "*" , "/"]
count= 1
islemsayisi=int(input("Kaç işlem yapmak istiyorsunuz?: "))
while count <= islemsayisi:
    sayi1 = int(input("İşlem yaapmak istediğiniz ilk sayıyı girin: "))
    sayi2 = int(input("İşlem yaapmak istediğiniz ikinci sayıyı girin: "))
    op = input("Yapmak istediğiniz işlemi girin(+,-,*,/):" )
    count = count+1

    if op in islem :

        if op =="+" :
            print(sayi1 + sayi2)
        elif op== "-":
       
            print(sayi1 - sayi2)
        elif op=="*":
           
            print(sayi1 * sayi2)
        elif op=="/":
        
            print(sayi1 / sayi2)
    else:
        print("Lütfen geçerli bir operatör girin!")
        
   
