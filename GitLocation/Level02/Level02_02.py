text = '''The adjective "deep" in deep learning refers to the use of multiple layers in the network. 
Early work showed that a linear perceptron cannot be a universal classifier,but 
that a network with a nonpolynomial activation function with one hidden layer of unbounded width can. 
Deep learning is a modern variation which is concerned with an unbounded number of layers of bounded size,which
permits practical application and optimized implementation,while retaining theoretical'''

w1 = "Have no mercy,you"
w2 = "Have no mercy, you"
w3 = " Have no mercy,  You"

# 방법 1
def parse(str):
    ret = 0
    for i in str.replace(",", " ").split(" "):
        if i == " " or i == '':
           continue
        ret = ret + 1

    return ret

# 방법 2
import re

def parse2(str):
    ret = 0
    for i in re.split(" |,", str):
        if i == " " or i == '':
            continue
        ret = ret + 1

    return ret


# 예제 1
print(parse(text))
print(parse2(text))
print(parse(w1))
print(parse2(w1))
print(parse(w2))
print(parse2(w2))
print(parse(w3))
print(parse2(w3))