x = 15
y = 25
print(f"x == y : {x == y}") # false
print(f"x is y : {x is y}") # false

# 파이썬에서 is는 변수의 object(객체)가 같아야 하고
# equal, ==는 변수의 값이 같아야 한다

# 따라서 위의 실행 결과에서
# 선행 코드는 false
# 후행 코드 역시, 값도 다르고 객체도 다르므로 false

a = 15
b = 15
print(f"a == b : {a == b}") # true
print(f"a is b : {a is b}") # true

list1 = ['apple', 'banana', 'kiwi']
list2 = list1
print(f"list1 == list2 : {list1 == list2}")
print(f"list1 is list2 : {list1 is list2}")
print(f"list1 value : {list1}, id : {hex(id(list1))}")
print(f"list2 value : {list2}, id : {hex(id(list2))}")


list3 = ['apple', 'banana', 'kiwi']
list4 = ['apple', 'banana', 'kiwi']
print(f"list3 == list4 : {list3 == list4}")
print(f"list3 is list4 : {list3 is list4}")
print(f"list3 value : {list3}, id : {hex(id(list3))}")
print(f"list4 value : {list4}, id : {hex(id(list4))}")

# 위의 코드에서 list3과 list4는 다른 객체이므로
# 변수를 무분별하게 생성하는 것에 주의해야 한다

# 정리
# is, not is는 참조로 동작하여 객체(object)를 비교
# ==, !=는 값을 비교한다
# 따라서 상황에 맞게 다르게 사용해야 한다

n1 = []      # 빈 배열
n2 = n1      # n2는 n1과 동일하고
n3 = n1 + n2 # n3는 동일하지 않음

print(f"Equal operation Resul is {n1 == n2 == n3}")
print(f"Is operation result is {n1 is n3 is n3}")