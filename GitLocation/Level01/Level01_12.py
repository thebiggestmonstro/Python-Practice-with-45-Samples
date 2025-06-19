
# 첫 번째 방법
d = {'a' : 'apple', 'b' : 'banana'}

d['c'] = 'carrot'
d['d'] = 'durian'
print(d)

# 두 번째 방법
d = {'a' : 'apple', 'b' : 'banana'}

d.update({'c' : 'carrot', 'd' : 'durian'})
print(d)