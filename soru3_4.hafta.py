liste=[3,6,4,1,10,12,-1,2,-20]
#liste.sort()

for i in range(0,len(liste)):
    for j in range(i,len(liste)):
        if liste[i] > liste[j]:
            temp=liste[i]
            liste[i]=liste[j]
            liste[j]=temp 
        
        
print("Listemizin küçükten büyüğe sıralanmış hali: ",liste)

