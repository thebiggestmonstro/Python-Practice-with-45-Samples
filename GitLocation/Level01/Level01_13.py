d = {'a' : 8, 'b' : 33, 'c' : 15, 'd' : 26, 'e' : 12, 'f' : 120}

# 첫 번째 방법
d1 = {}
for i in d.keys():
    if d[i] > 25:
       d1[i] = d[i]
print(d1)

# 두 번째 방법
d2 = {}
for k, v in d.items():
    if v >= 25:
        d2[k] = v
print(d2)

# 세 번째 방법
d3 = {k: v for k, v in d.items() if v >= 25}
print(d3)

# 네 번째 방법
d4 = dict((k, v) for k, v in d.items() if v >= 25)
print(d4)

# 다섯 번째 방법
d5 = dict(filter(lambda v : v[1] >= 25, d.items()))
print(d5)