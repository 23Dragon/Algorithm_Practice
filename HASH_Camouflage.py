from collections import defaultdict

def solution(clothes):    
    answer = 0

    df = defaultdict(list)
    N = len(clothes)

    # key, value insert
    for value, key in clothes:
        df[key].append(value)
    
    # counting each key
    count = []
    for cloth in df:
        count.append(len(df[cloth]))
    
    # +1 for not choice
    total = 1    
    for cnt in count:
        total *= (cnt+1)
    
    # -1 for not at all
    answer = total - 1
    
    return answer


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))