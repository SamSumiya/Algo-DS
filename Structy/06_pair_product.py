'''
    Pair Product

    Almost identical to the previos pair sum challenge

    Omit the approaches
'''

import enum


def pair_product_bf(numbers, target_product): 
    dict = {} 
    i = 0 
    size = len(numbers)

    while i < size: 
        el = numbers[i]

        diff = target_product / el
        if diff in dict: 
            return(i, dict[diff])

        dict[el] = i
        i += 1


def pair_product(numbers, target_product): 
    dict = {} 

    for idx, num in enumerate(numbers): 
        
        diff = target_product / num 
        if diff in dict: 
            return(dict[diff], idx)

        dict[num] = idx