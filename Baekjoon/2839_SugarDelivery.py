if __name__ == "__main__":
    N = int(input())
    
    result = 5001
    
    # 5
    if N % 5 == 0:
        result = N / 5
    
    # 3
    if N % 3 == 0:
        result = min(result, N / 3)
    
    # 5 & 3
    n = N / 5
    m = N % 5
    