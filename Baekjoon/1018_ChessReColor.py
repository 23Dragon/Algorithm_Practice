def check(y, x, c, o):
    cnt = 0
    color = c
    for i in range(y, y+8):
        for j in range(x, x+8):
            if arr[i][j] == color:
                cnt += 1

            color = 'B' if color == 'W' else 'W'
        color = 'B' if color == 'W' else 'W'
        
    return cnt



def solve(n, m, arr):
    min_ = 987654321
    for i in range(0, n+1-8):
        for j in range(0, m+1-8):
            # check start W
            W_color = check(i, j, 'W', 'B')
            min_ = min(W_color, min_)

            # check start B
            B_color = check(i, j, 'B', 'W')
            min_ = min(B_color, min_)

    print(min_)

if __name__ == "__main__":    
    N, M = map(int, input().split())
    arr = list()
    for n in range(N):
        arr.append(input())

    solve(N, M, arr)
    


        