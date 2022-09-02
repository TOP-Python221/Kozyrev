a = input().lower().split()
b = ''
for i in a:
    if i[0] in 'eaiou':
        i += 'way '
        b += i
    else:
        for j in i:
            if j in 'eaiou':
                n = i.index(j)
                i = i[n:] + i[:n] + 'ay '
                b += i
                break
print(b)

#helloy my friend how are yoy
#elloyhay iendfray owhay areway oyyay
