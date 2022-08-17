a = input().split()
while a != "":
    str_number = ""
    n = 0
    str_number = (a[0])
    n += int(a[1])            
    power= 1
    ans = 0    
    for i in str_number[::-1]:        
        ans += int(i)*power
        power *= n
    print(f'В десятичной системе счисления: {ans}')
    a = input().split()
#1101010 2
#В десятичной системе счисления: 106
#1010102 3
#В десятичной системе счисления: 821         