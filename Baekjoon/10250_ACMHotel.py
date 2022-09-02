if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        h, w, n = map(int, input().split())
        
        if n % h == 0:
            y = h * 100
            x = n // h
        else:
            y = (n % h) * 100
            x = (n // h) + 1
            
        print(y+x)
