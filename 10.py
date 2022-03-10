MAX = 20
n = 1
factor = 1
while n <= MAX:
    print(end=str(n)+':')
    while factor <=n:
        if n % factor == 0:
            print(factor , end = ' ')
            factor += 1 
            print()
    n+=1        
            
print("reached 20")
