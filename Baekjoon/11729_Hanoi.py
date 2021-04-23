def recursion(n, start, end, other):
    # f(ABC, 1, 3)
    # => f(AB, 1, 2) + f(C, 1, 3) + f(AB, 2, 3)
    global cnt
    cnt += 1

    if n == 1:
        #print(start, end)
        result.append((start, end))
        return
    else:
        recursion(n-1, start, other, end)
        #print(start, end)
        result.append((start, end))
        recursion(n-1, other, end, start)
    
    


def solution(N):    
    recursion(N, 1, 3, 2)    
    print(cnt)
    [print(i[0], i[1]) for i in result]    
    
    


if __name__ == "__main__":
    cnt = 0
    result = list()
    N = int(input())
    solution(N)
    