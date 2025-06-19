
l = ["Red", "Green", "Black", "Orange", "Purple"]

print({index: value for index, value in enumerate(l)})
print({index: value for index, value in enumerate(l, start=100)})

print("")
print("")

print(dict(enumerate(l)))
print(dict(enumerate(l, start=100)))