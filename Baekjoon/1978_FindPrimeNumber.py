import math

def isPrime(x):
    sqrt_x = int(math.sqrt(x))
    for i in range(2, sqrt_x+1):
        if x % i == 0:
            return False
    
    if x == 1:
        return False
    
    return True


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    for x in arr:
        if isPrime(x):
            count += 1
    print(count)