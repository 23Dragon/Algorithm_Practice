import math

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:        
        n = int(input())
        if n == 0:
            break
        
        count = 0
        # for i in range(n+1, 2*n+1):
            
        #     for j in range(2, i):
        #         if i % j == 0:
                    
            
            
        print(count)
        