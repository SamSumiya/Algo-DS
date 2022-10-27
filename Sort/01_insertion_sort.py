'''

    Insertion Sort

    Approach:
        start from the index 1 
        we will have to compare to the element in front the current index
        the way to do is get the base number which is on index i from 1 
        and assign j which is i - 1 
        then we can do if j >= 0 and base is less than the list[j]
        we should change the index of j + 1 to j 
        then we will decrement j to the previous number
        which allows us to traverse back work and keep updating the value of j to j + 1 
        when j is less than 0 which we are keep decrement, so it will happend
        when j is -1, loop will break and 
        we can assign whatever the key to j + 1 [-1 + 1 = 0] at the end of the inner loop
        return the list



'''


def insertion_sort(l): 

    i = 0

    while i < len(l): 
        base = l[i]
        j = i - 1 

        while j >= 0 and base < l[j]: 
            l[j+1] = l[j]
            j -= 1 
        
        l[j+1] = base
        
        i += 1 

    
    return l







l = [3,2,9,1,0]
r = insertion_sort(l)
print(r)