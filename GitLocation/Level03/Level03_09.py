
filepath = './TargetFolder_03/res.txt'
intro = "Select a menu number : "
file = open(filepath, 'a+')

while True:
    print("--------------------------")
    print("1. read")
    print("2. write")
    print("3. exit")
    print("--------------------------")

    menu = int(input(intro))

    if menu == 1:
        file = open(filepath, 'r')
        print(file.read())

        file = open(filepath, 'a+')

        print()
        print(">> Data read complete. <<")

    elif menu == 2:
        text = input('Write a text : ')
        file.write(text + '\n')

        print()
        print(">> Data write complete <<")

    elif menu == 3:
        file.close()

        print()
        print(">> Program exit. <<")

        break