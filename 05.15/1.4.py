a = input()
b = list(map(int, a))  
if sum(b[:3]) == sum(b[3:]): print("Да")
else:print("Нет")
    
#183534
#Да