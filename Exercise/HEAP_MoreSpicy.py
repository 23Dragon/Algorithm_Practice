import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    cnt = 0

    while len(scoville) >= 2:        
        # check all scovile >= K           
        if scoville[0] >= K:
            answer = cnt
            break 
                       
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        cnt += 1
        answer = cnt
        
    if scoville[0] < K:
        answer = -1
    
    return answer


s = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(s, K))
