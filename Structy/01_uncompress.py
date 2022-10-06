'''

    Uncompress

    given a string, starts from a number followed by some alphabets.
    Return a new string that use the number and multiply the following alphabets

    Strategy - Two Pointer approch
    1. set pointer1 and pointer2 to 0 initially
    2. create a number string from 0 - 9
    3. check if the element on pointer 2 is in the numbers or not
    4. if it is, we can move pointer2 to the next index
    5. when it reaches an element that is not in the numbers
    6. we can get the number before it by slice from pointer1 to pointer2
    7. then we can use the slice number range multiply the element on pointer2 and add it to the output
    8. after each the else condition, pointer2 will be on an element that is not a number, so we need to update pointer2 to the next number element
    9. also update pointer1 to pointer 2 so we can start fresh
    10. we can return the output after check the entire string
'''


def uncompass(string):
    i = j = 0
    size = len(string)
    numbers = '0123456789'
    output = ''

    while j < size:
        if string[j] in numbers:
            j += 1
        else:
            range = int(string[i:j])
            output += range * string[j]
            j += 1
            i = j

    return output
