def solve(level):
    if level == M:        
        print(' '.join(map(str, result)))
    else:
        for i in range(N):
            if check[i] == 0:
                result[level] = arr[i]
                check[i] = 1
                solve(level+1)
                check[i] = 0
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [int(x) for x in range(1, N+1)]
    result = [0] * M
    check = [0] * N
    
    solve(0)
  
'''
3 1
4 2
'''
'''
1
2
3
'''

