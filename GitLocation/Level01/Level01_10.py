# set(집합 자료형) : 중복읗 허용하지 않음 + 자료간의 순서도 없음
# list / tuple : 중복을 허용 + 자료간의 순서 존재
# OrderdDict : 순서가 있는 Dictionary

ex = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]

# 방법 1 : set으로 사용
ex1 = set(ex)
print(list(ex1))

# 방법 2 : 순서를 유지하면서 중복 제거
from collections import OrderedDict
ex2 = list(OrderedDict.fromkeys((ex)))
print(ex2)

# 방법 3 : 리스트 컴프리헨션
ex3 = []
ex4 = [ex3.append(x) for x in ex if x not in ex3]
print(ex3)