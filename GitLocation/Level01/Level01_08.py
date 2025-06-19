# 방법 1
ex1 = []
for i in range(1, 21):
 if i % 2 != 0:
  ex1.append(i * 10)
 else:
  ex1.append(i)

print(ex1)

# 방법 2
ex = [n * 10 if n % 2 != 0 else n for n in range(1, 21)]
print(ex)

