#Solve the question in two ways
sum_nuumber = 0
average_number = 0
a = float(input("Enter value:"))
minimum_number = a 
maximum_number = a 
for b in range(19):
    a = float(input("Enter value:"))
    sum_nuumber += a 
    if a > maximum_number:
        maximum_number = a
   
    elif a < minimum_number:
        minimum_number = a 


print(sum_nuumber,"sum")
print(sum_nuumber/20,"average")
print(maximum_number)
print(minimum_number)

.
.
.
sum = 0
for i in range(20):
    a = float(input('enter a number: '))
    sum += a

    if(i == 0):
        min = a
        max= a
    else:
        if(a > max):
            max = a
        if(a < min):
            min = a
    

avg = sum / 20
print('avg =',avg,' min =' , min , ' max =' , max)

input()


