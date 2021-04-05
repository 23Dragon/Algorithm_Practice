'''
input
# 5 21
# 5 6 7 8 9
output
# 21

ipnut
10 500
93 181 245 214 315 36 185 138 216 295
output
497
'''
def solve(level, begin):
    global min_
    global answer
    if level == 3:
        #print(numbers, end = ' ')
        sum_ = sum(numbers)
        if sum_ <= M:
            if M-sum_ < min_:
                min_ = M-sum_
                answer = sum_
                
        
    else:
        for i in range(begin, N):
            numbers[level] = arr[i]
            solve(level+1, i+1)
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [int(x) for x in input().split()]
    numbers = [0] * 3
    min_ = 987654321
    answer = -1

    solve(0, 0)
    print(answer)

    
