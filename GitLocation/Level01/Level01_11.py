# Dictionary와 json은 근본적으로 다름
# 둘 모두 자료를 Key와 Value 쌍으로 저장하지만,
# json은 자바스크립트로 작성된 일종의 데이터 형식을 의미하고
# Dictionary는 자료구조를 의미함

# Dictionary는 Key와 Value의 대응관계를 갖는 자료구조, 해시테이블 기반으로 동작하여 매우 빠르고 가변적임
# 자주 사용하는 함수들 : get, values, keys

# 생성하는 방법은 명시적인 방법과 묵시적인 방법이 있음
# 명시적인 방법 : dict({key : value, ...})
# 묵시적인 방법 : {key : value, ...}

# 시퀀스형 페어(튜플을 사용)로도 사용가능
# {(1, 'num1'), (2, 'num2'), ...}

# key 조합을 다양하게 설정 가능
# d = {'name' : 'Lee', 1 : [4, 5, 6]}

d = {'a' : 17, 'b' : 114, 'c' : 247, 'd' : 362, 'e' : 220, 'f' : 728, 'g' : -283, 'h' : 922}

# 1번째 방법
sum1 = 0
for i in d:
    sum1 += d[i]
print(sum1)

# 2번째 방법
print(sum(d.values()))

# 3번째 방법
print(sum([d[key] for key in d]))