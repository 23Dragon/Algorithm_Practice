import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False    
    if x == 1:
        return False
    return True

if __name__ == "__main__":
    M, N = map(int, input().split())
    
    for i in range(M, N+1):
        if isPrime(i):
            print(i)