def solve(N):
    global min_ 
    for i in range(N-1, 0, -1):
        sum_numbers = sum([int(x) for x in str(i)[:]])
        if i + sum_numbers == N:
            min_ = min(min_, i)

if __name__ == "__main__":
    N = int(input())    # dividesum    
    min_ = 1000001
    solve(N)
    answer = min_ if min_ != 1000001 else 0
    print(answer)
    


    '''
    input 216
    output 198
    '''