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

# {"group1" : 'name' : 'Han', 'age' : '22', 'gender' : 'Male', 'married' : 'No'}
# "type" : {'f' : 'engineer'}

# 첫 번째 방법
#d['group1'].append({'name' : 'Han', 'age' : '22', 'gender' : 'Male', 'married' : 'No'})
#d['type']['f'] = 'engineer'
#print(d)

# 두 번째 방법
#d.get('group1').append({'name' : 'Han', 'age' : '22', 'gender' : 'Male', 'married' : 'No'})
#d.get('type')['f'] = 'engineer'
#print(d)

# 세 번째 방법
d.get('group1').append({'name' : 'Han', 'age' : '22', 'gender' : 'Male', 'married' : 'No'})
d.get('type').update({'f' : 'engineer'})
print(d)