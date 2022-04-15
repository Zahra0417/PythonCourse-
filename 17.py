while(1):
    i=int(input("Enter number of disk:"))
    def hanoi(desk=1,start= 'a' ,temp= 'b' ,finish= 'c' ):
        if desk==1:
            print(start + " go to " + finish)
        else:
            hanoi(desk-1,start,finish,temp)
            print(start + " go to " + finish)
            hanoi(desk-1,temp,start,finish)
        
    hanoi(i,'a','b','c')
