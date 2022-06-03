"""

11.11 Exercise 

Exercises 1
answer :
1.Tuples and lists are two similar sequences with the same programming language, Python. Tuples are immutable, which means they cannot be changed once they are created. While, it is a sequential list that can be changed. Once created, it can be changed and supports other operations. 
2. Shows the literal syntax of tuples by parentheses, while how literally lists are represented by square brackets. 
3.Tuples are heterogeneous while the lists are homogeneous. One has to deal with cases. 
4.Tuples show the structure while the lists show the order.

Exercises 2
answer :
Similar to lists or strings that have indexes for access to their members, we use indexes to access Tupel elements in Python.
To access the nth member, all you have to do is write the name of the tuple and write the index number of the desired house in parentheses ([]).

Exercises 3
answer :
immutable

Exercises 4
answer :
ordered

Exercises 5
answer :
>>> a = 1, 2, 3, 4, 5, 6, 7, 8 
>>> a 
(1, 2, 3, 4, 5, 6, 7, 8) 
>>> *midlist = a 
>>> midlist 
(3, 4, 5, 6)

Exercises 6
answer :
>>> a = 1, 2, 3, 4, 5, 6, 7, 8 
>>> a 
(1, 2, 3, 4, 5, 6, 7, 8) 
>>> s = a[3:7] 
>>> s = tuple(s) 
>>> s 
(4, 5, 6, 7)

Exercises 7
answer :
>>>a=7, 10, -3, 18, 6, 10
>>>a
(7, 10, -3, 18, 6, 10)
>>> x, *rest = a
>>> *start ,y =a
>>>x
7
>>>rest(10,-3,18,6,10)
>>>start(7,10,-3,18,6)
>>>y
10

Exercises 8
answer :
def mul_tuple(tuple) : 
    product = 1
    for i in tuple:
        product = product * i 
    return product 


tuple1 = (11, 12, 4, 3)
print(tuple1) 
print("product:",mul_tuple(tuple1))

Exercises 9
answer:
def zero_sum(num):
    z = 0
    for i in num:
        z += i
    if z == 0 :
        return True
    elif z!= 0 :
        return False
    else:
        return True

num =(4,7,9,10,-1)
x = zero_sum(num)
print(x)

Exercises 10
answer:
A Python dictionary is an associative container which permits access based on a key, rather than an  index. 
Unlike an index, a key is not restricted to an integer expression.
 
Exercises 11
answer:
d = {}

Exercise 12
answer:









