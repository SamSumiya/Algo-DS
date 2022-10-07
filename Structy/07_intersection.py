'''
    Intersect

    given 2 sets of lists, a and b. 
    return a list containing only the common elements in a and b


    approach: brute force
    0. create a new variable with empty list
    1. iterate through one list 
    2. check if another list has the same element
    3. if it does, then we can append the element to the output list

    Time Complexity: O(n*m)
    Space Complexity: O(min(n, m))




    approach: use set [Constant Time loopup] O(1) to cut down time complexity
    pretty much the same approch but just convert a list to a set

    Time Complexity: O(n+m)
    Space Complexity: O(min(n, m))

'''

def intersection_bf(a, b):
    output = []
    b = set(b)
    for el in a:
        if el in b: 
            output.append(el)
    
    return output