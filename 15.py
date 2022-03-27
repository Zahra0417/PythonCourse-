#sin x with function
import math 
def sin(x,n):
    sine=0
    for i in range(n):
        sign=math.pow(-1,i)
        pi=math.pi 
        a=x*(pi/180)
        sine=sine+(sign*(a**(2.0*i))/math.factorial(2*i+1))
    return sine
    
x=float(input('Enter The value of Degrees:'))
n=int(input('Enter The number of terms:'))
print(sin(x,n))
.
.
.

#sinx with out function 
import math

x = float(input('Enter The value of Degrees:'))
n = int(input('Enter The number of terms:'))

sine = 0
for i in range(n):
    sign = math.pow(-1, i)
    pi = math.pi
    a = x * (pi / 180)
    sine = sine + (sign * (a ** (2.0 * i)) / math.factorial(2 * i + 1))

print(sine)
