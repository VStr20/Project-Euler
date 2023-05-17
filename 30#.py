def sum_of_digits(n, a):
   sum=0
   for x in str(n):
       sum += int(x)**a 
   return sum

answer=0
for b in range(1,10):
    for i in range(2,35*(10**b-1)):
        if(i == sum_of_digits(i, b)):
            answer += i
            print("for exponent b =" ,b ,"-", i)
    b += 1



#upper bound
#9**5=59049
#5*59049=295245
#6*59049=354294
#7*59049=413343

#upperbound is 354294

# for exponent b = 1 - 2
# for exponent b = 1 - 3
# for exponent b = 1 - 4
# for exponent b = 1 - 5
# for exponent b = 1 - 6
# for exponent b = 1 - 7
# for exponent b = 1 - 8
# for exponent b = 1 - 9
# for exponent b = 3 - 153
# for exponent b = 3 - 370
# for exponent b = 3 - 371
# for exponent b = 3 - 407
# for exponent b = 4 - 1634
# for exponent b = 4 - 8208
# for exponent b = 4 - 9474
# for exponent b = 5 - 4150
# for exponent b = 5 - 4151
# for exponent b = 5 - 54748
# for exponent b = 5 - 92727
# for exponent b = 5 - 93084
# for exponent b = 5 - 194979
# for exponent b = 6 - 548834
# for exponent b = 7 - 1741725
# for exponent b = 7 - 4210818
# for exponent b = 7 - 9800817
# for exponent b = 7 - 9926315
# for exponent b = 7 - 14459929
# for exponent b = 8 - 24678050
# for exponent b = 8 - 24678051
# for exponent b = 8 - 88593477