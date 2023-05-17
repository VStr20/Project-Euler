import time

start = time.time()

#When first number is 1 digit the second digit and answer has to sum to 8 digits, only possibilty of whuch is both ahve to be each of 4 digits.
# When second number is 2 digits the second digit and answer has to sum to 7 digits, possibility if second number is 3 digit and answer is 4 digit.
# further cases are not possible ar covered here.

number = set('123456789')
product = []
# k = ('0')
for a in [0, 1]:
    b = 3 - a
    for i in range(10**a,10**(a+1)): # 1 digit and 2 digit 
        for j in range(10**b,10**(b+1)): # second number can be of 3 or 4 digits
            s = str(i) + str(j) + str(i*j) # 1 to 9
            if(len(s) > 9): 
                break
            elif(len(s) == 9):
                num = 0
                if((set(s) == (number))): # set removes repeating values in the str, this ensure that he number is pandigital
                    # print(i, "*", j, "=", i*j)
                    product.append(i*j)

print(product)

prod = [*set(product)]
print(prod)

answer = 0
for i in range(len(prod)):
    answer += prod[i]

print(answer)

end = time.time()

print(end - start)