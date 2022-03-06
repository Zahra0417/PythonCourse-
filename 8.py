first_number = int(input('first number: '))
second_number = int(input('second number: '))
third_number = int(input('third number: '))
fourth_number = int(input('fourth number: '))
fifth_number = int(input('fifth number: '))
arr = [first_number, second_number, third_number, fourth_number, fifth_number]
duplicate = 0

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            duplicate += 1

if duplicate == 0:
    print("ALL UNIQUE")
else:
    print("DUPLICATES")
