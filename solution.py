import math

def isSumOfTwo(N):
    if N <= 3:
        return "No"

    if N % 2 == 0:
        return "Yes"
        
    return isPrime(N-2)

def isPrime(N):
    for i in range(2, math.floor(math.sqrt(N)+1)):
        if N % i == 0:
            return "No"
    return "Yes"

N = # pass N
result = isSumOfTwo(N)
print(result)