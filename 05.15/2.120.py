a = input().split()
b = len(a)
for i in range(b-1):
    if i < b-2:
        a[i] = a[i] + ','
    else:
        a[i] = a[i] + ' и'
print(*a)

#яблоко кофе маинез лимонад
#яблоко, кофе, маинез и лимонад