h, m = [int(x) for x in input().split()]
h_, m_ = h, m
if m >= 45:
    m_ -= 45
else:
    if h == 0:
        h_ = 23
        m_ = 60 - (m-45)
    else:
        m_ -= 45

print(h_, m_)
