ex = "Marry had a little lamb"
in_str = "Suppose we have few words that are seperated by spaces"
in_str2 = "aaa bbb cccc "
in_str3 = "aaa bbb cccc"
in_str4 = "aaa bbb cccc  "
in_str5 = " aaa bbb cccc "

def parse(str):
    ret = 0
    for i in str.split(" "):
        if i == " " or i == '':
           continue
        ret = ret + 1

    return ret

# 예제 1
print(parse(ex))
print(parse(in_str))
print(parse(in_str2))
print(parse(in_str3))
print(parse(in_str4))
print(parse(in_str5))