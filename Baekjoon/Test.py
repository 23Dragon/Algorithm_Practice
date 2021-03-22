n = int(input())
_inputs = []
for i in range(n):
    _inputs.append(input())


answer = 0
for i in _inputs:    
    tmp = []
    for idx, value in enumerate(i):
        if value not in tmp:
            tmp.append(value)
        else:
            if i[idx-1] == value:
                tmp.append(value)
                if idx == len(i)-1:
                    print(idx, value)
                    answer += 1
            else:
                break
        

print(answer)




        