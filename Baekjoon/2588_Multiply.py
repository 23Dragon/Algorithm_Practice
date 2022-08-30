a = int(input())
b = input()

mulFirst = int(b[-1])
mulSecond = int(b[-2:-1])
mulThird = int(b[-3:-2])

first = mulFirst*a
second = mulSecond*a
third = mulThird*a

print(first)
print(second)
print(third)
print(a*int(b))