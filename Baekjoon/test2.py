# 한 라인 입력 받을 때마다 계산

total = 0
index = 0

N = int(input('N by N 행렬. input N : '))

while index < N:
    
    line = [int(num) for num in input('행렬을 입력하세요 : ').split()]

    if len(line) != N:
        print('행과 열의 개수가 같지 않습니다.')
        break
    else:
        total += line[index]
        index += 1

print('대각합 : ', total)
    