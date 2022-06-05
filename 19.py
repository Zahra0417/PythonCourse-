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
a = 1, 2, 3, 4, 5, 6, 7, 8 
a 
(1, 2, 3, 4, 5, 6, 7, 8) 
s=-,-,*s,-,-= a
s = tuple(s)
print(tuple(s))

Exercises 6
answer :
a = 1, 2, 3, 4, 5, 6, 7, 8 
a 
(1, 2, 3, 4, 5, 6, 7, 8) 
s = a[3:7] 
s = tuple(s) 
print(tuple(s))

Exercises 7
answer :
a=7, 10, -3, 18, 6, 10
a
(7, 10, -3, 18, 6, 10)
s = x,y = t[0],t[5]
s = tuple(s)
print(tuple(s))

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
d['Fred'] = 44

Exercise 13
answer:
If the key within the square brackets does not 
exist in the dictionary, the statement adds the key and pairs it with the value on the right of the assignment 
operator. If the key already exists in the dictionary, the statement replaces the value previously associated 
with the key with the new value on the right of the assignment operator.
Or The get method retrieves a value from the dictionary. Returns the default value if there is no requested value

Exercise 14
answer:
must be a valid key in dictionary , or the program will raise an exception. A valid key is a key that 
is present in the dictionary.  We see the interpreter’s reaction when we attempt to use an invalid key: the interpreter an generates 
KeyError exception.

Exercise 15
answer:
immutable

Exercise 16
answer:
(a){3: 0, 5: 1, 10: 1, 8: 2, 15: 4}

(b) 3
    5
    10
    8
    15

(c) 3
    5
    10
    8
    15

(d) 0
    1
    1
    2
    4

Exercise 17
answer:
unordered

Exercise 18
answer:
from tkinter import Tk, Canvas
from tkinter.ttk import Button,Frame


def press_black():
    color = 'black'
    if color=='black':
        canvas.itemconfigure(yellow_lamp,fill='black')
def press_yellow():
    color = 'yellow'
    if color=='yellow':
        canvas.itemconfigure(yellow_lamp,fill='yellow')

root=Tk()
root.title('traffic light')
frame = Frame(root)
frame.pack()
canvas = Canvas(frame , width=80,height=80)
yellow_lamp = canvas.create_oval(10,30,60,80,fill='black')
button = Button(frame,text='On',command=press_yellow)
button2 = Button(frame,text='OFF',command=press_black)
button.grid(row=0,column=0)
button2.grid(row=1,column=0)
canvas.grid(row=0,column=1)
root.mainloop()

Exercise 19
answer:
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root=Tk()
root.title("Tic Tac Toe")
#add Buttons
bu1=ttk.Button(root,text=' ')
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda: ButtonClick(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda: ButtonClick(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda: ButtonClick(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda: ButtonClick(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda: ButtonClick(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda: ButtonClick(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda: ButtonClick(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda: ButtonClick(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda: ButtonClick(9))

playerturn=ttk.Label(root,text="   Player 1 turn!  ")
playerturn.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)

playerdetails=ttk.Label(root,text="    Player 1 is X\n\n    Player 2 is O")
playerdetails.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)

res=ttk.Button(root,text='Restart')
res.grid(row=3,column=1,sticky='snew',ipadx=40,ipady=40)
res.config(command=lambda: restartbutton())

a=1
b=0
c=0
def restartbutton():
    global a,b,c
    a=1
    b=0
    c=0
    playerturn['text']="   Player 1 turn!   "
    bu1['text']=' '
    bu2['text']=' '
    bu3['text']=' '
    bu4['text']=' '
    bu5['text']=' '
    bu6['text']=' '
    bu7['text']=' '
    bu8['text']=' '
    bu9['text']=' '
    bu1.state(['!disabled'])
    bu2.state(['!disabled'])
    bu3.state(['!disabled'])
    bu4.state(['!disabled'])
    bu5.state(['!disabled'])
    bu6.state(['!disabled'])
    bu7.state(['!disabled'])
    bu8.state(['!disabled'])
    bu9.state(['!disabled'])
    
#after getting result(win or loss or draw) disable button
def disableButton():
    bu1.state(['disabled'])
    bu2.state(['disabled'])
    bu3.state(['disabled'])
    bu4.state(['disabled'])
    bu5.state(['disabled'])
    bu6.state(['disabled'])
    bu7.state(['disabled'])
    bu8.state(['disabled'])
    bu9.state(['disabled'])


def ButtonClick(id):
    global a,b,c
    print("ID:{}".format(id))

    #for player 1 turn
    if id==1 and bu1['text']==' ' and a==1:
        bu1['text']="X"
        a=0
        b+=1
    if id==2 and bu2['text']==' ' and a==1:
        bu2['text']="X"
        a=0
        b+=1
    if id==3 and bu3['text']==' ' and a==1:
        bu3['text']="X"
        a=0
        b+=1
    if id==4 and bu4['text']==' ' and a==1:
        bu4['text']="X"
        a=0
        b+=1
    if id==5 and bu5['text']==' ' and a==1:
        bu5['text']="X"
        a=0
        b+=1
    if id==6 and bu6['text']==' ' and a==1:
        bu6['text']="X"
        a=0
        b+=1
    if id==7 and bu7['text']==' ' and a==1:
        bu7['text']="X"
        a=0
        b+=1
    if id==8 and bu8['text']==' ' and a==1:
        bu8['text']="X"
        a=0
        b+=1
    if id==9 and bu9['text']==' ' and a==1:
        bu9['text']="X"
        a=0
        b+=1
    #for player 2 turn
    if id==1 and bu1['text']==' ' and a==0:
        bu1['text']="O"
        a=1
        b+=1
    if id==2 and bu2['text']==' ' and a==0:
        bu2['text']="O"
        a=1
        b+=1
    if id==3 and bu3['text']==' ' and a==0:
        bu3['text']="O"
        a=1
        b+=1
    if id==4 and bu4['text']==' ' and a==0:
        bu4['text']="O"
        a=1
        b+=1
    if id==5 and bu5['text']==' ' and a==0:
        bu5['text']="O"
        a=1
        b+=1
    if id==6 and bu6['text']==' ' and a==0:
        bu6['text']="O"
        a=1
        b+=1
    if id==7 and bu7['text']==' ' and a==0:
        bu7['text']="O"
        a=1
        b+=1
    if id==8 and bu8['text']==' ' and a==0:
        bu8['text']="O"
        a=1
        b+=1
    if id==9 and bu9['text']==' ' and a==0:
        bu9['text']="O"
        a=1
        b+=1
        
    #checking for winner   
    if( bu1['text']=='X' and bu2['text']=='X' and bu3['text']=='X' or
        bu4['text']=='X' and bu5['text']=='X' and bu6['text']=='X' or
        bu7['text']=='X' and bu8['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu4['text']=='X' and bu7['text']=='X' or
        bu2['text']=='X' and bu5['text']=='X' and bu8['text']=='X' or
        bu3['text']=='X' and bu6['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu5['text']=='X' and bu9['text']=='X' or
        bu3['text']=='X' and bu5['text']=='X' and bu7['text']=='X'):
            disableButton()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 1")
    elif( bu1['text']=='O' and bu2['text']=='O' and bu3['text']=='O' or
        bu4['text']=='O' and bu5['text']=='O' and bu6['text']=='O' or
        bu7['text']=='O' and bu8['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu4['text']=='O' and bu7['text']=='O' or
        bu2['text']=='O' and bu5['text']=='O' and bu8['text']=='O' or
        bu3['text']=='O' and bu6['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu5['text']=='O' and bu9['text']=='O' or
        bu3['text']=='O' and bu5['text']=='O' and bu7['text']=='O'):
            disableButton()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 2")
    elif b==9:
            disableButton()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Match is Draw.")

    if a==1 and c==0:
        playerturn['text']="   Player 1 turn!   "
    elif a==0 and c==0:
        playerturn['text']="   Player 2 turn!   "
            
root.mainloop()


Exercise 20
answer:
the expression {} does not
 represent the empty set. In order to use the curly braces for a set, the set must contain at least one element.
The expression set() produces a set with no elements, and thus represents the empty set.

Exercise 21
answer:
A=set()

Exercise 22
answer:
immutable

Exercise 23
answer:
(a):A = {20, 19, 2, 10, 7}
(b):20 in A = True 
(c):20 not in A = False 
(d):A&B = {10,7}
(e):A|B = {20,19,2,10,7,4,5,9}
(f):C < A = True 
(g):C <= A = True 
(h):C <= B = False
(i):A <= A = True 
(j):A < A = False 
(K):len(A) = 5
(l):{x + 2 for x in range(10)} = {2,3,4,5,6,7,8,9,10,11}
(m): {x - 2 for x in A} = {0,5,8,17,18}
(n):{x - 2 for x in A if x < 10} = {0,5}




12.12 Exercises
Exercise 1
answer:
if a solution expressed illustrates the concept of look before you leap,
usually abbreviated as LBYL in the Python community. This programming idiom checks code that may
misbehave before executing it.

Exercise 2
answer:
An alternative to LBYL is EAFP, which stands for easier to ask for forgiveness than permission. The
 EAFP approach attempts to execute the potentially 
problematic code within a try statement. If the code
 raises an exception, the program’s execution does not necessarily terminate; instead,
the program’s execution jumps imeidately to a different block within the try statement.

Exercise 3
answer:


























