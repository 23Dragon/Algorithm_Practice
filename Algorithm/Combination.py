def main():
    # nCr    
    n, r = 3, 2    
    arr = [x for x in range(n)]
    result = [0] * r    
    
    def combi(level, begin):
        if level == r:
            print(result)
            return
        for i in range(begin, n):
            result[level] = arr[i]
            print('level, i, result : ', level, i, result)
            combi(level+1, i+1)


    combi(0, 0)

    





if __name__ == "__main__":
    main()