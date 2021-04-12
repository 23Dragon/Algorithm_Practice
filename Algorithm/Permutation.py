def permu(level):
    if level == r:
        print(result)
    else:
        for i in range(n):
            if check[i] == 0:
                result[level] = arr[i]
                check[i] = 1
                permu(level+1)
                check[i] = 0

if __name__ == "__main__":
    n, r = 4, 2
    arr = [int(x) for x in range(n)]
    result = [0] * r
    check = [0] * n

    permu(0)

    