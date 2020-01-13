#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        i = 0
        while i in range (len(text)):
            print(text[i], end ='')
            if text[i] in ['.','?',':']:
                if i != len(text) - 1:
                    print()
                    print()
                i+=1;
            i+=1
