
'''
    Anagrams

    Compare two string and return true if they have equal elements else return false

    Example
    anagrams('paper', 'reapa') # -> False
    anagrams('elbow', 'below') # -> True

    Approach 1: 
    Turn string into list and compare the two lists
    
    Approach 2: 
    1. loop through a string and create a dict set key as the element and value as the number
    2. if there are matching element, we will increment the number until the end 
    3. loop through another string and check if the element exists or not
    4. if it does exists, then we can subtract 1 from the same key
    5. else, we simply add the new key and value 1 to this dict
    6. lastly, we will need to loop througth the dict and check if there is any value that is greater than 0 
    7. if it does, we know we can prematurely return False
    8. at the end, we can assume that there was no value that is greater than 0 so we can return True

'''


def anagrams(s1, s2):
    dict = {}
    i = j = 0

    size = len(s1)

    while i < size:
        if s1[i] not in dict:
            dict[s1[i]] = 1
        else:
            dict[s1[i]] += 1
        i += 1
    
    while j < len(s2):
        if s2[j] in dict: 
            dict[s2[j]] -= 1
        else: 
            dict[s2[j]] = 1 
        j += 1
        
    for key, val in dict.items():
        if val != 0: return False 
        
    return True
r = anagrams('tax', 'taxi')
print(r)