cnt = 0

def recursion(n, start, end):
    # f(ABC, 1, 3)
    # => f(AB, 1, 2) + f(C, 1, 3) + f(AB, 2, 3)
    if n == 1:
        print(start, end)
        return
    
    check = {start: 1, end: 1}
    print(check)
    print(check[1])
    c = [x for x in range(1, 4) if x not in check]
    
    
    #recursion(n-1, start, )
    global cnt
    


def solution(N):    
    recursion(N, 2, 3)    



if __name__ == "__main__":
    N = int(input())
    print(solution(N))