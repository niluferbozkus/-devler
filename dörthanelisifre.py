x = input("4 haneli bir şifre belirleyiniz: ")
    
while len(x)!=4 or x.isdigit() != 1 :
    print("Lütfen girdiğiniz şifrenin 4 haneli ve rakamlardan oluşaan bir şifre olduğundan emin olun!")
    x = str(input("4 haneli bir şifre belirleyiniz: "))

print("Yeni şifreniz",x, "olarak kaydedilimiştir.")



    

