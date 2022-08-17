count = 0
numbers = [int(number) for number in input().split()]
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        count += 1                                         
print(f'Кол-во элементов списка, больших предедущих {count}')

#4 5 6 3 2 1 65 43 2 7
#Кол-во элементов списка, больших предедущих 4