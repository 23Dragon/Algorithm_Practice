def combi(r_idx, begin):
    if r_idx == r:
        print(result)
    else:
        for i in range(begin, n):
            result[r_idx] = arr[i]
            combi(r_idx+1, i+1)

if __name__ == "__main__":
    n, r = 4, 2
    result = [0] * r
    arr = [(x+1) for x in range(n)]
    
    combi(0, 0)