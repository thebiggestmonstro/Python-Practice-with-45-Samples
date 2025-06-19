d = {'USA' : 36, 'Germany' : 17, 'France' : 32, 'Australia' : 77, 'South Africa' : 99, 'India' : 108, 'South Korea' : 200}

def findWithKey():
    dict = {key.upper(): data for key, data in d.items()}
    word = input()

    if word.upper() in dict.keys():
        print(dict[word.upper()])
    else:
        print('No results were found for your serch')

findWithKey()
