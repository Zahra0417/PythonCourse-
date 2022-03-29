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
