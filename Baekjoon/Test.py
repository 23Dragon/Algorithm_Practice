N = int(input())

for i in range(1, 1000000001):
    result = 3*i**2 -(9*i) + 9
    if result >= N:
        print(i-1)
        break


