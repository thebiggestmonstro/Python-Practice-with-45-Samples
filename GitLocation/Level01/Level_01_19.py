
# step3
a = 100
def test2():
    global a
    print(a)

    a = 55
    return a

print(a)        # 100
print()
print(test2())  # 100 55
print()
print(a)        # 55