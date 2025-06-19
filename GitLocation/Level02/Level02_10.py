d = {
    "group1" : [
        {'name' : 'Park', 'age' : '32', 'gender' : 'Male'},
        {'name' : 'Cho', 'age' : '30', 'gender' : 'Feale'},
        {'name' : 'Kwon', 'age' : '39', 'gender' : 'Male', 'married' : 'No'}
    ],
    "group2" : [
        {'name' : 'Kang', 'age' : '31', 'gender' : 'Male', 'married' : 'No'},
        {'name' : 'Lee', 'age' : '37', 'gender' : 'Female', 'married' : 'Yes'}
    ],
    "type" : {'a' : 'employee', 'b' : 'officer', 'c' : 'director', 'd' : 'manager', 'e' : 'service provider'}
}

# 원하는 출력 결과 = Name : Kang,  Age : 31, Type : officer
print(f"Name : {d['group2'][0]['name']}, Age : {d['group2'][0]['age']}, type : {d['type']['b']}")

# 인덱스에 직접 접근하는 것은 위험하므로 get 함수를 사용
print(f"Name : {d.get('group2')[0].get('name')}, Age : {d.get('group2')[0].get('age')}, type : {d.get('type').get('b')}")
