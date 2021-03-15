def solution(brown, yellow):
    answer = []

    tot = brown + yellow

    for i in range(2, tot):
        if tot % i == 0:
            x = i           # width
            y = tot // i    # heigh
            
            # width >= heigh
            if x >= y and (x*2 + y*2 -4) == brown:
                answer = [x, y]

    return answer

solution(24,24)
