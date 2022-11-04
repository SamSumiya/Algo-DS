'''
    Non Constructible Change

    Approach: O(nlogn)

        loop through the sorted coins
        we will add the current coin to the possible_changes
        if at any point the possible changes + 1 is less than the current coin itself
        we know that it is not possible to make that coin
        [1,1,4]
        1 + 1 will only be 2 not 4 
        so 2 + 1 is less than 4 so we will return 3  
        


'''





def nonConstructibleChange_op(coins):
    coins.sort()
    possible_changes = 0 

    for coin in coins: 
        if coin > possible_changes + 1: 
            return possible_changes + 1
        
        possible_changes += coin
    
    return possible_changes + 1

coins = [1,1,2]
r = nonConstructibleChange_op(coins)
print(r)





def nonConstructibleChange(coins):
    if coins == []: return 1 
    if len(coins) == 1: 
        if 1 == coins[0]: 
            return 2 
        else:
            return 1 
    sorted_coins = sorted(coins)
    change = 0
    i = 0 

    while i < len(coins) - 1:
        coin = sorted_coins[i]
        next_coin = sorted_coins[i+1]
        change += coin 

        if change + 1 < next_coin: 
            return change + 1
        
        i += 1 
    return sum(coins) + 1 
