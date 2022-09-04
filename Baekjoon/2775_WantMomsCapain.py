if __name__ == "__main__":
    
    T = int(input())
    
    for t in range(T):
        k = int(input())
        n = int(input())
        
        arr = [[0]*n for _ in range(k+1)]
        for i in range(n):
            arr[0][i] = i+1
        
        for i in range(k):
            for j in range(n):
                if j != 0:
                    arr[i+1][j] = arr[i][j] + arr[i+1][j-1]
                else:
                    arr[i+1][j] = arr[i][j]
          
        print(arr[k][n-1])
        
        
    