
x = ["grapes", "mango", "orange", "peach", "apple" , "lime", "banana", "cherry", "tomato", "kiwi", "blueberry" , "watermelon"]

# 방법 1 - 순회
ex1 = []
for i in x:
    if i == "apple" or i == "kiwi":
        ex1.append(i.upper())

print(ex1)

# 방법 2 - lambda와 map
ex2 = list(map(lambda b : b.upper(), filter(lambda a: a == 'apple' or a == 'kiwi', x)))
print(ex2)

# 방법 3 - 리스트 컴프리헨션
ex3 = [a.upper() for a in x if a == 'apple' or a == 'kiwi']
print(ex3)