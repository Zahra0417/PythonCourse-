"""

Exercise 1
answer:Yes


Exercise 2
answer:with the help of the negative index in Python ,we can access the elements of the list from the bottom.


Exercise 3
answer:list=[45,-3,16,8]


Exercise 4
answer:
(a) lst[0]
(b) lst[3]
(c) 10
(d) 29
(e) -4
(f) 29
(g) 10
(h) illegal


Exercise 5
answer:
(a) 3
(b) 5
(c) 1
(d) 5
(e) 5
(f) 2
(g) 0
(h) 3


Exercise 6
answer: Function len


Exercise 7
answer: a=[]


Exercise 8
answer:
(a) [20,1,-34,40,-8,60,1,3]
(b) [20,1,-34]
(c) [-8,60,1,3]
(d) [-8,60,1,3]
(e) [40,-8]
(f) [20,1,-34]
(g) [-8,60,1,3]
(h) [20,1,-34,40,-8,60,1,3]
(i) [20,1,-34,40]
(j) [1,-34,40,-8]
(k) True
(l) False
(m) 8


Exercise 9
answer:
(a)
(b)
(c)
(d) lst[3:4]=['a','b','c']
(e) lst[ : ]
(f) 
(g) lst[-1: ]
(h) lst[ :3]
(i) lst[2: ]
(j) lst[1:4]=[ ]
(k) lst[1:4]


Exercise 10
answer:
(a) [8,8,8,8]
(b) [2,7,2,7,2,7,2,7,2,7,2,7]
(c) [1,2,3,'a','b','c','d']
(d) [1,2,1,2,1,2,4,2]
(e) [1,2,4,2,1,2,4,2,1,2,4,2]
 

Exercise 11
answer:
(a) [3,5,7,9]
(b) [50,60,70,80,90]
(c) [12,15,18]
(d) [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)]
(e) [(0,0),(0,2),(1,1),(1,3),(2,0),(2,2)]


Exercise 12
answer:
(a) [x**2 for x in range (1,6)]
(b) [x/4 for x in range (1,7)]
(c) [(x,y) for x in ['a','b'] for y in [0,1,2]]


Exercise 13
answer:
x in lst (show existence)
x not in lst (show not existence)


Exercise 14
answer:
reverse()function is used to reverse the order of objects in a list data structure in place.


Exercise 15
answer:

def sumlist(L):
    sum=0
    for n in L:
        if n>0:
            sum+=n
    return sum 
    
L=[]
for i in range (0,4):
    n=int(input("Enter a number of list:"))
    L+=[n]

    
z= sumlist(L) 
print(z,"the sum of positive numbers")
if len(L)==0:
    print("the list is empty")



Exercise 16
answer:



























