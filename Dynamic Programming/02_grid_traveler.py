'''
    Grid Traveler

    a 2d grid, travel on the top left corner and my goal is to travel to the bottom-right corner. 
    I can only move down or right

    in how many ways can you travel to the goal on a grid with domensions m * n 
'''


def grid_traveler(m, n, memo={}):
    key = str(m) + ',' + str(n)

    if key in memo: 
        return memo[key]

    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    memo[key] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)
    return memo[key]

m = 18
n = 18
r = grid_traveler(m, n)
print(r)


'''
 if grid_traveler(m - 1, n, memo) in memo:
        return memo[grid_traveler(m - 1, n, memo)]
    if grid_traveler(m, n - 1, memo) in memo: 
        return memo[grid_traveler(m, n - 1, memo)]
    else:
        if m == 0 or n == 0: return 0 
        if m == 1 and n == 1: return 1



        return memo[grid_traveler(m - 1, n, memo)] + memo[grid_traveler(m, n - 1, memo)]
'''
