x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']
print(x[4])                 # 인덱스를 지정하여 값을 반환, Banana
print('Banana' in x)        # in 연산자를 사용하여 자료구조에 있는지 판단, True
print(x.index('Banana'))    # 데이터의 인덱스에서 인자가 위치한 인덱스를 반환, 4
print(x[x.index('Banana')]) # Banana

# 시퀀스 자료형(데이터의 값이 연속적으로 이뤄진 자료구조) : List, Tuple, Str, Range

# 데이터의 인덱스에서 인자가 위치한 인덱스를 반환하되,범위를 지정함
print(x.index('Banana', 0, len(x)))