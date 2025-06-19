from urllib import request
import json

response = request.urlopen("https://jsonplaceholder.typicode.com/users")
response_json = response.read()

d = json.loads(response_json)

# 일반적인 출력문
print(d)

print("\n")

# pprint를 사용한 출력
from pprint import pprint
pprint(d)

# pprint : Pyhton에서 데이터 구조를 보기 쉽게 출력하기 위해 사용하는 메서드
# 옵션은 다음과 같다 : depth - 중첩 데이터 / indent - 들여쓰기 / width - 줄 길이 조정 / sort_dicts - 키 정렬 / stream - 파일에 출력