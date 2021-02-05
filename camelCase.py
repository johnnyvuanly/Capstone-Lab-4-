def camelcase(sentence):
    """Convert sentence to camelCase, for example, "Display all books" 
    is converted to "displayAllBooks" """

    title_case = sentence.title() # title makes this first letter into a capital
    sentenceList = title_case.split( )
    sentenceList2 = ("".join(sentenceList))
    return sentenceList2[0:1].lower() + sentenceList2[1:] # fixed bug where it was originally sentence[0:1].lower() to sentenceList2. It originally made the first letter disapear 

def banner():
    """Display welcome banner"""
    message = "CAMELCASE PROGRAM!"
    stars = '*' * len(message)
    print(f'{stars}\n{message}\n{stars}')

def instructions():
    """Print instruction message"""
    print('Enter a sentence to convert to camelcase')

def main():
    banner()
    instructions() # Always remember to call your functions
    sentence = input('Enter a sentence here: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()