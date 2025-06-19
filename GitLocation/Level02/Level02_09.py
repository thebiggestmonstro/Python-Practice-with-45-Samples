x = 10
y = 20
no = 308276567
n = 'Kim'

# 출력 1
ex1 = 'n = %s, no = %d, sum=%d' % (n, no, (x + y))
print(ex1) # Kim(문자열) 125fed57(16진수) 30(10진수)

# 출력 2
ex2 = 'n = {n}, no = {no}, sum={sum}'.format(n=n, no=no, sum=x+y)
print(ex2) # n = Kim, no = 308276567, sum = 30

# 출력 3
ex3 = f'n = {n}, no = {no}, sum = {x + y}'
print(ex3) # n = Kim, no = 308276567, sum = 30

# 결과값이 다른 것은 출력 1
# no가 유일하게 16진수로 출력됨


# % 연산자를 사용한 문자열 출력은 잘 사용하지 않는다
# 문자열.format 방식은 % 연산자보다 최신 기법이다
# f-string을 이용한 문자열 출력은 파이썬 3.6 부터 사용가능하다

# 출력 4 = template 사용
from string import Template
ex4 = 'n = $n, no = $no, sum = $sum'
t = Template(ex4)

print(t.substitute(n = n,no = no, sum = x + y))

# 진수의 출력 : 2진수 = b / 8진수 = o / 16진수 = x|X
k = 77
print(f"2진수 : {k:b}, 8진수 : {k:o}, 16진수 : {k:x}")

# 구분
l = 10000000000
print(f'쉼표로 구분 : {l:,}')

# 정렬 : ^ = 가운데 정렬 / < = 왼쪽 정렬 / > = 오른쪽 정렬
m = 20
print(f'기본적으로 오른쪽 정렬 : {m:10}.')
print(f'가운데 정렬 : {m:^10}.')
print(f'왼쪽 정렬 : {m:<10}.')
print(f'빈칸을 채워 오른쪽 정렬 : {m:$>10}.')