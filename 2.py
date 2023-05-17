value = 0

def fibonacci(n):
    if(n==1):
       return 0
    elif(n==2):
       return 2;
    else:
       return 4*fibonacci(n-1) + fibonacci(n-2)
   

sum1 = 0
for i in range(1,13):
    sum1 = sum1 + fibonacci(i)
    
print(sum1)

    