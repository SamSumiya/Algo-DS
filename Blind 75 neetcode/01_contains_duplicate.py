'''
    Subset of Arrays and Hashing

    https://leetcode.com/problems/contains-duplicate/submissions/

    approach: hashmap
        create a empty hashmap
        populate hashmap with each number as key and value will be incremented as encouter
        if at any point the value is greater that 0
        we know that there must be more than one same element
        so we can return True
        or return False at the end
'''


def containsDuplicate_hashmap(nums):
    hashmap = {}

    for el in nums:
        if el not in hashmap:
            hashmap[el] = 0
        else:
            hashmap[el] += 1
        if hashmap[el] > 0:
            return True
    return False


def containsDuplicate_hashset(nums):
    hash_set = set()

    for el in nums:
        if el in hash_set:
            return True

        hash_set.add(el)

    return False


def containsDuplicate_sort(nums):
    sorted_num = sorted(nums)
    i = 0

    while i < len(sorted_num) - 1:
        j = i + 1

        if sorted_num[i] == sorted_num[j]:
            print(sorted_num[i], sorted_num[j])
            return True

        i += 1
    return False


# Won't pass leetcode - slow code
def containsDuplicate_bf(nums):
    idx = 0
    for el_1 in nums:
        for el_2 in nums[idx+1:]:
            if el_1 == el_2:
                print(el_1, el_2)
                return True
        idx += 1
    return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
r = containsDuplicate_bf(nums)
print(r)
