from collections import deque

def func_stack():
    stack = []
    stack.append(5)
    stack.append(2)
    stack.append(3)    
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()
    
    print(stack[::-1]) # 최상단 원소부터 출력
    print(stack) # 최하단 원소부터 출력


def func_queue():
    queue = deque()
    
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()
    
    print(queue) # 먼저 들어온 순서대로 출력
    queue.reverse() # 역순으로 바꾸기
    print(queue) # 나중에 들어온 원소부터 출력

if __name__ == "__main__":
    #func_stack()
    func_queue()