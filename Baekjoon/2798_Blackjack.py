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

def combi(r_idx, begin):
    if r_idx == 3:
        sum_ = sum(result)
        print(result, sum_)
    else:
        for i in range(begin, N):
            result[r_idx] = arr[i]
            combi(r_idx+1, i+1)




if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [int(x) for x in input().split()]
    result = [0] * 3
    
    combi(0, 0)