'''
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

8

92
'''
def check_in(i, j):
    for k in range(1, 16):
        print(i, j, k)
        if i-k >= 0 and j-k >= 0:
            check[i-k][j-k] = 1
        if i-k >= 0:
            check[i-k][j] = 1
        if i-k >= 0 and j+k <= N:
            check[i-k][j+k] = 1
        if j-k >= 0:
            check[i][j-k] = 1
        if j+k <= N:
            check[i][j+k] = 1
        if i+k <= N and j-k >= 0:
            check[i+k][j-k] = 1
        if i+k <= N:
            check[i+k][j] = 1
        if i+k <= N and j+k <= N:
            check[i+k][j+k] = 1
    
        

def solve(i, j, rem):
    if i >= N and j >= N and rem > 0:
        return
    elif i>= N and j >= N and rem == 0:
        result += 1
        return
    
    # check_in
    check_in(i, j)
    print(check)
    # recursion
    
    # check_out
    


if __name__ == "__main__":
    N = int(input())
    # making board
    board = [[0] * N for _ in range(N)]
    check = [[0] * N for _ in range(N)]
    result = 0
    solve(0, 0, N)

