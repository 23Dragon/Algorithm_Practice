
def solve(n, array):
    rank_list = list()
    
    for i in array:
        rank = 1       

        for j in array:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        
        print(rank, end=' ')
        
        
    
                

if __name__ == "__main__":
    N = int(input())
    arr = list()    
    for i in range(N):
        w, h = map(int, input().split())
        arr.append((w, h))
    
    solve(N, arr)
    

'''
5
55 185
58 183
88 186
60 175
46 155
'''

'''
2 2 1 2 5
'''