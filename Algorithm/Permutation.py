def permu(r_idx):
    if r_idx == r:
        print(result)
    else:
        for i in range(n):
            if check[i] == 0:
                result[r_idx] = arr[i]
                check[i] = 1
                permu(r_idx+1)
                check[i] = 0

if __name__ == "__main__":
    n, r = 4, 2
    arr = [(x+1) for x in range(n)]
    result = [0] * r
    check = [0] * n

    permu(0)