# 딕셔너리 선언
d = dict(one = list(range(1, 11)), two = list(range(11, 23)), three = list(range(23, 37)))

for k in d.keys():
    print(f'key {k} has values {d[k]} -> total : {len(d[k])}')

for k, v in d.items():
    print(f'key {k} has values {v} -> total : {len(v)}')