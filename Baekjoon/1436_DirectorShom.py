def solve(N):
    arr = list()
    start = 1      

    while(len(arr) != N):        
        str_num = str(start)        
        if '666' in str_num:
            arr.append(str_num)
        start += 1

    print(arr[-1]) if len(arr) > 0 else print(-1)
    

if __name__ == "__main__":
    N = int(input())
    solve(N)

    
    
'''
input
2
output
1666
'''
'''
666, 1666, 2666, 3666, ...
'''