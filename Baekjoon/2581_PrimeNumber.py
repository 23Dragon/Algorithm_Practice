import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    
    if x == 1:
        return False
    
    return True

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    
    min_prime = 10001
    sum_prime = 0
    
    for i in range(M, N+1):
        if isPrime(i):
            sum_prime += i
            min_prime = min(min_prime, i)
    
    if sum_prime == 0:
        print(-1)
    else:
        print(sum_prime)
        print(min_prime)
        