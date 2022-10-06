"""
    Compress a string and get the number of consecutive substrings for prefix

    Example: 
    aaa -> 3a
    cc -> 2c

    Edge case: 
    t -> t (no need to have a number prefix)

    Strategy
    1. Use two pointers starting from 0 
    2. Move one pointer alone the string and compare to another pointer
    3. If there the elements on the two index match, we will just move the pointer to the next index
    4. Else, get the substring starting from pointer1 to pointer2 - 1
    5. If the substring length equals to 1, we will just add element on point 1 to the output
    6. Else, added the length of the substring as prefix and get the element on pointer 1
    7. Since pointer 2 always moves on to the next element, we just need to update pointer 1 to equal pointer 2 after every loop
    8. Finally, return the output

    Gotchat: 
    Since we need to compare the element at previos index and the current index, so the last substring will get ignored.
    So we can added some additional symbol to avoid this issue.

"""


def compress(string): 
    i = j = 0 
    output = ''
    string += '!'
    length = len(string)

    while j < length:
        if string[i] == string[j]: 
            j += 1 
        else: 
            if len(string[i:j]) == 1: 
                output += string[i]
            else: 
                output += str(len(string[i:j])) + string[i]
            
            i = j

    return output


string = 'aaabbceff'
r = compress(string)
print(r)