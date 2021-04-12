N = int(input())
arr = list()
for i in range(N):
    arr.append(int(input()))

n_arr = sorted(arr)
for i in n_arr:
    print(i)