def combi(level, begin):
    if level == r:
        print(result)
    else:
        for i in range(begin, n):
            result[level] = arr[i]
            combi(level+1, i+1)

if __name__ == "__main__":
    n, r = 4, 2
    arr = [(x+1) for x in range(n)]
    result = [0] * r

    combi(0, 0)