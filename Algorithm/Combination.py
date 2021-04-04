def combi(level, start):
    if level == r:
        print(result)
    else:
        for i in range(start, n):
            result[level] = arr[i]
            combi(level+1, i+1)

if __name__ == "__main__":
    n, r = 3, 2
    arr = [x for x in range(n)]
    result = [0] * r
    combi(0, 0) # level, start