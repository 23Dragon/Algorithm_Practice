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

            # �ϴ� ��������
            rt = dfs(value, pt)

            # ���� �ִٸ� ���� �Ǿ��� ��
            if rt:
                return rt
            
            # ���� ���ٸ� �ٽ� �־�����
            routes[key].insert(idx, value)
    
    # ���ĺ� �켱���� ����
    routes = init_path()
    for r in routes:
        routes[r].sort()
    
    N = len(tickets)    
    answer = dfs('ICN', ['ICN'])

    
    return answer

# start from ICN
tickets = [["ICN", "BBB"], ["ICN", "AAA"], ["BBB", "ICN"]]
solution(tickets)


