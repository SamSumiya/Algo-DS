'''
    Fibonacci

    Approach: iterative
        cover two case when the num is 1 and 2
        then we will need to keep decerementing the number
        we will then add the idx 0 and next index to create a new number and then push it back to the list
        finally, we will get the last element from the list and return the value

    approach: recursion
        base cases are when num is 1 and 2
        then we will respectively return 1 and 1
        then we will just need to recursively call the funciton with - 1 and - 2

    approach: memoization
        use a memo dict to get the result
        key is the number and value is the return value 
        such as memo[3] = fib_memo(3 - 1) + fib_memo(3 - 2)
        we will always check if the memo exits: 
            if it does we will return that value
        if not we will add the result from the recursive call to the memo


'''



from cmath import rect


def fib_iter(num): 
    if num == 1: return 1
    if num == 2: return 1
    output = 0 
    l = [1, 1]
    i = 0 
    while num > 2: 
        output = l[i] + l[i+1]
        l.append(output)      
        i += 1 
        num -= 1

    return l[-1]

# result = fib_iter(9)
# print(result)

def fib_recur(num): 
    if num == 1: return 1
    if num == 2: return 1

    return fib_recur(num - 1) + fib_recur(num - 2)

# result = fib_recur(50)
# print(result)


def fib_memo(num,memo = {}):
    if num in memo: 
        return memo[num]
    else:
        if num <= 2: return 1 
        memo[num] = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)
        return memo[num]
    
result = fib_memo(50)
print(result)



