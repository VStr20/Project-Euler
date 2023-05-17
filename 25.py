fibo = [1,1]
def fibonacci(m):
        fibo.append(fibo[m-2]+fibo[m-1])

for i in range(2,12000):
    fibonacci(i)

for i in range(len(fibo)):
    num = 0
    for a in str(fibo[i]):
        num = num + 1
    if(num>=1000):
        print(i+1) # As counting in fibo starts from 0
        break