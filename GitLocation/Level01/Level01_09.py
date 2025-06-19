# 1) map + range + lambda 사용
ex = list(map(lambda x: str(x * 10), range(1, 16)))
print(ex)

# 2) 리스트 컴프리헨션 사용
ex2 = [str(n * 10) for n in range(1, 16)]
print(ex2)