def function1(n):
    n = (n - 1) / 2
    return 2 * n * (8 * n * n + 15 * n + 13) / 3 + 1

print(function1(1001))

# the sum of diagonals is (1, 3, 13, 31, ...)
# (1, 5, 17, 37, ...)
# (1, 7, 21, 43, ...)
# (1, 9, 25, 49, ...)
# sum of all these terms 
# S = 1 + 3+ 13 + 31 + ... Tn
# S =     1 + 3 + 13 + 31 + ... Tn 
# Tn = 1 + (2 + 10 + 18 + ...)
# Tn1 = 1 + (n-1)(4n-6)
# Tn2 = 1 + (n-1)(4n-4)
# Tn3 = 1 + (n-1)(4n-2) 
# Tn2 = 1 + (n-1)(4n)
# Sum = \sum [4 + (n-1)(16n-12)]
# Sum = \sum 16n^2 + 28*n + 16
# Sum = 16*n*(n+1)*(2*n+1)/6 - 28*n*(n+1)/2 + 16*n
# where n = (n' + 1)/2
# Answer is Sum - 3 as 1 is counted 4 times 
n = 501
Sum = 16*n*(n+1)*(2*n+1)/6 - 28*n*(n+1)/2 + 16*n
print(Sum - 3)

'''from PIL import Image

with Image.open('IMAGE PATH') as img:
    img.show()'''
