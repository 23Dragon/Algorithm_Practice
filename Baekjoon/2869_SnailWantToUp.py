if __name__ == "__main__":
    res = 0
    high = 0
    a, b, v = map(int, input().split())
    
    n = 0    
    if (v-b)%(a-b) == 0:
        print(int((v-b)/(a-b)))
    else:
        print(int((v-b)/(a-b)) + 1)
