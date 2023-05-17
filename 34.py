#362880
#upperbound : 7*362880 = 2539160

def factorial(n):
    fac=1
    for a in range(2,n+1):
        fac *= a
    return fac

for i in range(1,2539160):
    sum=0
    for x in str(i):
        sum = sum + factorial(int(x))
    if(sum == i):
        print(i)
        
# 1
# 2
# 145
# 40585