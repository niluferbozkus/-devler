x = input("4 haneli bir şifre belirleyiniz: ")

#Girdi olarak alınan değerin 4 haneli ve sadece rakamlardan oluşan bir şifre olduğunun kontrolü   
while len(x)!=4 or x.isdigit() != 1 :
    print("Lütfen girdiğiniz şifrenin 4 haneli olduğundan ve sadece rakamlardan oluştuğundan emin olun!")
    x = input("4 haneli bir şifre belirleyiniz: ")

print("Yeni şifreniz",x, "olarak kaydedilimiştir.")
