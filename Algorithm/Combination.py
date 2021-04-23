def combi(level, begin):
    if level == r:
        print(result)
    else:
        for i in range(begin, n):
            result[level] = arr[i]
            combi(level+1, i+1)


<<<<<<< HEAD
    combi(0, 0)

    





=======
>>>>>>> 61ffaf8da45e61b31ec31e7ab24e6f46683a5806
if __name__ == "__main__":
    n, r = 4, 2
    arr = [int(x+1) for x in range(n)]
    result = [0] * r

    combi(0, 0)