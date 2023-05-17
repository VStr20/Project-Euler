import math
y=math.factorial(100) 

print(y)

'''n= 0
for i in str(y):
    n+=int(i)
print(n)'''

n=0
def factorial(n):
    fac=1
    for i in range(1,n):
        fac=fac*i
    return fac 
    
print(factorial(100))

for i in str(factorial(100)):
    n+=int(i)
print(n)

#typecast string factorial into integer 