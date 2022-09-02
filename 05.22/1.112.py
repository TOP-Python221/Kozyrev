count = list(map(int,input().split()))

if len(count) > 4:
    count.sort()
    new_count = count[:] 
    new_count.pop(0), new_count.pop()    
    print(f'Редактированные данные {new_count}\nВведеные данные {count}')
else:    
    print("Ошибка, мало значений!")

'''
1 2 3 4 5 6 7 8
Редактированные данные [2, 3, 4, 5, 6, 7]
Введеные данные [1, 2, 3, 4, 5, 6, 7, 8]
'''
