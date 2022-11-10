'''
    Longest Streak

    given a linked list with different values
    return the longest streak of the same values

    approach: iteration
        We will need to track the total count when two elements don't equal to each other and update a array that stores when two nodes values don't match
        or it is the last element in the linked list 
        ** edge case ** 
        return 0 when head is None

        1. we can create a new variable and set it as 0
        2. we then can create a base node and set it as the first value in the linked list
        3. we can loop through the linked list
        4. if the first element equals to the base node then we can increment the output by 1
        5. we also need to consider case that the longest streak is at the end of the linked list
        6. so if the head.next is none, only when that happens
        7. we will add the number to the list
        8. else we need to cover the case that two nodes don't equal to each other
        9. we will have to reset the basecase to the next value on linked list
        10. since we will need to count from 1 for case of one single element
        11. so we will set num to 1
        12. we then move the head to the next node on the linked list
        13. return the largest number in the list
'''


def longest_streak_my_iter(head):
    if head == None:
        return 0
    count = 0
    base_val = head.val
    output = []

    while head:
        if head.val == base_val:
            count += 1
            if head.next == None:
                output.append(count)
        else:
            output.append(count)
            base_val = head.val
            count = 1

        head = head.next
    return max(output)


def longest_streak_iter_2(head):
    max_streak = 0
    current_streak = 0
    prev_val = None

    while head:
        if prev_val == None:
            prev_val = head.val
        if prev_val == head.val:
            current_streak += 1
            if head.next == None:
                if current_streak > max_streak:
                    max_streak = current_streak
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            prev_val = head.val
            current_streak = 1
        head = head.next

    return max_streak


def longest_streak(head):

    max_count = 0
    current_count = 0
    prev_val = None

    while head:
        if head.val == prev_val:
            current_count += 1
        else:
            current_count = 1

        prev_val = head.val

        if current_count > max_count:
            max_count = current_count
        head = head.next

    return max_count


def longest_streak(head, prev_val=None):
    longest_streak = 0
    current_streak = 0

    while head:
        if head.val == prev_val:
            current_streak += 1
        else:
            prev_val = head.val
            current_streak = 1
        if current_streak > longest_streak:
            longest_streak = current_streak

        head = head.next

    return longest_streak
