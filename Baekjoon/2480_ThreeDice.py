a, b, c = map(int, input().split())

res = 0
if a == b and b == c:
    res = 10000+a*1000
elif a == b and b != c:
    res = 1000+a*100
elif b == c and c != a:
    res = 1000+b*100    
elif c == a and a != b:
    res = 1000+c*100
elif a != b and b != c and c != a:
    res = max(a, b, c)*100
    
print(res) 