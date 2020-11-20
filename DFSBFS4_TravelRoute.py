# coding=UTF-8
from collections import defaultdict
def solution(tickets):
    def init_path():
        rt = defaultdict(list)
        for key, value in tickets:
            rt[key].append(value)
        return rt

    def dfs(key, path):
        if N + 1 == len(path):
            return path

        for idx, value in enumerate(routes[key]):
            routes[key].pop(idx)

            pt = path[:]
            pt.append(value)

            # 일단 보내보자
            rt = dfs(value, pt)

            # 길이 있다면 리턴 되었을 것
            if rt:
                return rt
            
            # 길이 없다면 다시 넣어주자
            routes[key].insert(idx, value)
    
    # 알파벳 우선순위 정렬
    routes = init_path()
    for r in routes:
        routes[r].sort()
    
    N = len(tickets)    
    answer = dfs('ICN', ['ICN'])

    
    return answer

# start from ICN
tickets = [["ICN", "BBB"], ["ICN", "AAA"], ["BBB", "ICN"]]
solution(tickets)


