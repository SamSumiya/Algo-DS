'''
    Most Frequent Character

    Given a single string and find a element has most reqeats

    Approach: Iteration 

    1. Loop through the string and store the element as the key and times it appears as value in a dict
    2. after the iteration, we can check the dict to find the key has highest value, to do this
    3. we can set a variable called inital and set it to 0 and output to empty string
    4. during the iteration of the dict, we can update teh inital to the current value if it is higher than the inital as well as updating the key to the output
    5. at the end, we can return the output to get the most frequent character in the string


    ps: structy's approch is that when we compare the what is inside of the dict.
    1. we can create a new variable called best and set it none
    2. initally, we can compare the value by using the key from looping through the string
    3. we can have a conditional asking if best is None or a value comparison
        a. this approach avoids the inital value to be None which is great! 
    4. then we can assign best to the inital char
    5. later, we can keep asking the same question that if dict[current_element] > dict[best] 
    6. if yes, then we replace best to the current_element until the end
    7. final step is to return the best 
'''


def most_frequent_char_1(string):
    size = len(string)
    output = ''
    current = 0
    dict = {}

    for s in string:
        if s not in dict:
            dict[s] = 1
        else:
            dict[s] += 1

    for key, val in dict.items():
        if val > current:
            current = val
            output = key

    return output


def most_frequent_char_2(string):
    dict = {}

    for s in string:
        if s not in dict:
            dict[s] = 1
        else:
            dict[s] += 1

    output = None

    for s in string:
        if output is None or dict[s] > dict[output]:
            output = s

    return output


def most_frequent_char_list(string):
    alps = [0 for _ in range(25)]
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    indice = []
    max_val = 0

    for el in string:
        idx = alphabets.index(el)
        alps[idx] += 1

    max_num = max(alps)

    for idx, val in enumerate(alps):
        if val == max_num:
            indice.append(idx)

    for el in string:
        alp_idx = alphabets.index(el)
        if alp_idx in indice:
            return el
