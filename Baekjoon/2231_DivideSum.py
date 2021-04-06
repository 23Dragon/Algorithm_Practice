def solve(N):
    '''
    N 245 -> 245 + 2 + 4 + 5 = 256
    245 : creator
    256 : dividesum
    '''

    n = N
    
    
    while n >=1 :
        sub = 1
        N_sub_sum = sum([int(x) for x in str(n-sub)])        
        dividesum = N_sub_sum + (n-sub) # N-sub : creator
        print(n, n-sub)
        if dividesum == N:
            print(n-sub)
        sub += 1
        n -= sub
        




if __name__ == "__main__":
    N = int(input())    # dividesum
    solve(N)
    answer = 0
    min_ = 1000001

    '''
    input 216
    output 198
    '''