total = 0
index = 0

print('행렬 입력이 끝나면 . 을 입력하세요')

first__matrix2 = list()

while index < len(first__matrix2):    
    first__matrix = input('행렬을 입력하세요 : ')
    
    first__matrix = first__matrix.split()
    first__matrix2 = list(first__matrix)

    chosen_num = int(first__matrix2[index])
    
    index = index + 1
    total = total + chosen_num

    if first__matrix == '입력 끝':
        break
    
print('대각합 : ', total)



