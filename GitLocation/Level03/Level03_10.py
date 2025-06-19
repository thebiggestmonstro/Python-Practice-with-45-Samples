import json


def list_phonebook():

    f = open('Target.json', 'r')
    d = json.load(f)

    for pid in d:
        print('\nPID:', int(pid) + 1)
        for p_info in d[pid]:
            print(p_info + ':', d[pid][p_info])

    f.close()


def add_member():
    print("\nEnter the information of the member")

    name = input('Name: ')
    phone = input('Phone: ')

    name_check = False

    f = open('Target.json', 'r')
    d = json.load(f)

    f.close()

    for pid in d:
        if name == d[pid].get('Name'):
            name_check = True

    if name_check is True:
        print('\n# The member is already in the phone book')
    else:
        with open('Target.json', 'w') as f:
            d[len(d)] = {'Name': name, 'Phone': phone}

            json_obj = json.dumps(d, indent=4)

            f.write(json_obj)

            print('\n# The phone number has been written to the phone book')

    return d


def delete_member():

    print("\nEnter the name")
    name = input('name: ')

    f = open('Target.json', 'r')
    d = json.load(f)

    f.close()

    for pid in d:
        if name == d[pid].get('Name'):
            with open('Target.json', 'w') as f:
                del d[pid]

                json_obj = json.dumps(d, indent=4)

                f.write(json_obj)

                print('\n# The member has been deleted')

                return d

    print('\n# The member is not in the phone book')


def mainmenu():
    while True:
        menu = input("""
----MAIN MENU----
1: List phonebook
2: Add a new member
3: Delete a member
4: Program exit 
Please enter your choice: """)

        if menu == '1':
            list_phonebook()
        elif menu == '2':
            add_member()
        elif menu == '3':
            delete_member()
        elif menu == '4':
            print('# Exit!')
            return False  # break
        else:
            print('\n Menu cannot be found')


mainmenu()