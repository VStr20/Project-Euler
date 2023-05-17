import time

start =time.time()
def palindrome(n): #boolean function
    # temp = n      #This piece of code does not give the number 585585
    # rev = 0
    # while(n > 0):
    #     dig=n % 10
    #     rev = rev*10 + dig
    #     n = int(n/10)
    # if(temp == rev ):
    #     return True
    # return False
    num = str(n)
    if(num == num[::-1]):
        return True
    return False


def binary(a): #returns the binary value of the number 
    # p = int(bin(a).replace("0b", ""))
    q = (format(a, 'b'))
    p = int(q)
    return p

sum1 = 0
for k in range(0,1000001):
    m = binary(k)
    if(palindrome(k)):
        if(palindrome(m)):
           print(k)
           sum1 = sum1 + k

print("Sum =", sum1)

end = time.time()

print(end - start)


# def is_palindrome(n):
#     """returns True if palindrome, False otherwise."""
#     to_str = str(n)
#     if to_str == to_str[::-1]:
#         return True
#     return False


# def find_palindromes(n):
#     """generates all numbers if palindrome in both bases 2, 10 in range n. """
#     decimal_binary = {decimal: bin(decimal)[2:] for decimal in range(1, n) if is_palindrome(decimal)}
#     for decimal, binary in decimal_binary.items():
#         if is_palindrome(binary) and not binary[0] == 0:
#             yield decimal


# if __name__ == '__main__':
#     print(sum(list(find_palindromes(1000000))))