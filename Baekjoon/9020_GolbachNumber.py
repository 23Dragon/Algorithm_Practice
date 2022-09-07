from math import sqrt

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True
        

if __name__ == "__main__":
    T = int(input())
    
    prime_arr = [False] * 10001
    for i in range(2, 10001):
        if isPrime(i):
            prime_arr[i] = True
        else:
            prime_arr[i] = False
    
    for t in range(T):
        n = int(input())
        
        result = []
        for i in range(2, n):            
            if prime_arr[i] and prime_arr[n-i] and i <= n-i:                
                result.append((i, n-i))
    
        min_diff = 99999
        min_a, min_b = 99999, 99999
        for i in result:
            if min_diff > i[1]-i[0]:
                min_a, min_b = i[0], i[1]
                min_diff = i[1]-i[0]
        
        print(min_a, min_b)
            