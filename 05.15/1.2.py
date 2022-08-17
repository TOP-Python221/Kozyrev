s = input()
sm = ""
for i in s:    
    if i != " ":
        sm += i
    else: continue    
sm = len(sm)
print(f"{(sm * 80)//100} руб. {(sm * 80)%100} коп.")     
       
#грузите апельсины бочках братья карамазовы
#30 руб. 40 коп.
    

