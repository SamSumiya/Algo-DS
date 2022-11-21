
''''
Ituition: 
We need to get the number of each value from each categories
if we elements from all catetgories, then the total number is going to be 4

then we will need to check if the length of password is longer than 6 or not
if it is longer than 6, we can simply just return the different of the 4 - total uniq characters
else if the input string is less than 6: 
    we will need to check if the difference of the input and the required length which is 6
    when the diffenrence is greater than the different of the characters, we will just return the greater length
    if that means we will need to return the difference of the missing characters


'''

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    numbers_counts = 0 
    lower_case_counts = 0 
    upper_case_counts = 0
    special_character_counts = 0
    
    for val in password: 
        if numbers_counts == 0 and val in numbers: 
            numbers_counts += 1
        if lower_case_counts == 0 and val in lower_case: 
            lower_case_counts += 1
        if upper_case_counts == 0 and val in upper_case: 
            upper_case_counts += 1
        if special_character_counts == 0 and val in special_characters: 
            special_character_counts += 1

    total = sum([numbers_counts,lower_case_counts ,upper_case_counts,special_character_counts])
    diff = 0
    if total < 4: 
        diff = 4 - total
    if n > 5:
        return diff
    else: 
        # if length of the string is less than minimal requirements which is 6
        # then use 6 - the length of the string, if the result is greater than the diff
        # that means we can just return the diff as the result: result length covers the minimal number of each value
        if 6 - n > diff:
            return  6 - n 
        else:  
            return diff

s = '#HackerRank'
r = minimumNumber(len(s), s)

print(r)