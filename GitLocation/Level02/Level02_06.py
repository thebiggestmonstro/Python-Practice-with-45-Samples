import os

def makeFileWithSequence(filepath, filenames, contents):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    for name in filenames:
        with open(filepath + name + '.txt', 'w') as f:
                f.write(f"{contents[0:]} ")

n = ["A", "B", "C", "D", "F", "G"]
c = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

makeFileWithSequence("ret/", n, c)