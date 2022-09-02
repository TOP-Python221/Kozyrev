number = int(input())
a = str()
while number % 7 == 0:
    a += str(number) + ' ' 
    number = int(input())
print(a + str(number)) 