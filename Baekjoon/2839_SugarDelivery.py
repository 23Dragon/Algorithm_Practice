if __name__ == "__main__":
    N = int(input())
    
    count = 5001
    
    min_count = N // 3 + 1
    
    for i in range(min_count):
        for j in range(min_count):            
            if N == 3*i + 5*j:                
                count = min(i+j, count)

    if count == 5001:
        print(-1)
    else:
        print(count)
    