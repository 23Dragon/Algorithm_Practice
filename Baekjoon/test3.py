# 전체 행렬 입력 받은 후 계산

total = 0
index = 0

N = int(input('N by N 행렬. input N : '))

matrix = list()

for i in range(N):
    line = input('행렬을 입력하세요 : ').split()
    if len(line) != N:
        print('행과 열의 개수가 같지 않습니다.')
        break
    matrix.append(line)

for line in matrix:
    total += int(line[index])
    index += 1

print('대각합 : ', total)
