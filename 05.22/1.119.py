avg_value = []
min_value = []
max_value = []
while a := input():
    avg_value.append(int(a))
        
c = sum(avg_value) // len(avg_value)#деление без остатка для того чтоб числа остовались целыми
for i in avg_value:
     if i <= c: min_value.append(i)
     else: max_value.append(i)         
print(f"Среднее значение введеных данных: {c}\nЗначения ниже среднего(или равные ему): {min_value}\nЗначения выше среднего: {max_value} " )        
# если правильно понял терминологию задания, что вывести списком, то есть в ковадратных скобках(если нет можно было приминить метод .join()) 
'''
4
5
6
7
8
44
5
6
33

Среднее значение введеных данных: 13
Значения ниже среднего(или равные ему): [4, 5, 6, 7, 8, 5, 6]
Значения выше среднего: [44, 33]     
'''
    
    



 