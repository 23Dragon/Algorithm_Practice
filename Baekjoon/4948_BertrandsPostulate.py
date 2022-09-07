import math

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    
    prime_arr = []
    for i in range(2, 123456*2+1):
        if isPrime(i):
            prime_arr.append(i)
    
    while True:        
        n = int(input())
        if n == 0:
            break
        
        count = 0
        for i in range(n, 2*n+1):
            if i in prime_arr:
                count += 1
        
            
            
        print(count)
        