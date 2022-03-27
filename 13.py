x = 0 
for i in range(10):
    xnew = x - (x * x * x - x * x + 2)/(3 * x *x - 2)
    if abs(xnew - x) < 0.0001 : break
    x = xnew 
print("the root is %f at %d iteration" % (xnew,i))
