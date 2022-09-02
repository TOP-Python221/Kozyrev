data = []

line = input("Введите целое число(Enter для окончания)")
while line != "":       
    data.append(line)
    line = input("Введите целое число(Enter для окончания)")
    
new_data = list(map(int, data))

for i in new_data:
    if i < 0:
        print(i)
for i in new_data:        
    if i == 0:
        print(i)
for i in new_data:
    if i > 0:
        print(i)    
 
'''
Введите целое число(Enter для окончания)55
Введите целое число(Enter для окончания)40
Введите целое число(Enter для окончания)-1
Введите целое число(Enter для окончания)-25
Введите целое число(Enter для окончания)0
Введите целое число(Enter для окончания)125
Введите целое число(Enter для окончания)
-1
-25
0
55
40
125
'''
  
    
 