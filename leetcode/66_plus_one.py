'''
66. Plus One

Check if the last digit
    if the sum of it and 1 is greater than 9
        we will assign 1 = carry
    else 
        we will just update it with 1
    then we can move on to the rest of the digits
        if otehr digit + carry(1) is going to be greater than 9 
            then we will keep the carry and make the current digit to 0 
            until digit + carry is less than 10 
        
    then at the end, we will need to chack if the carry is still 1 or not
    if it is we will add it to the last index and reverse the list


'''

class Solution(object):
    def plusOne(self, digits, carry=0):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        output = []
        i = len(digits) - 1

        while i >= 0:
            if i == len(digits) - 1:
                last_num = digits[i] + 1
                if last_num > 9:
                    digits[i] = 0
                    carry = 1
                else:
                    if carry == 0:
                        digits[i] += 1
            else:
                sum_two = digits[i] + carry
                if sum_two > 9:
                    digits[i] = 0
                    carry = 1
                else:
                    carry = 0
                    digits[i] = sum_two

            output.append(digits[i])

            i -= 1
        if carry == 1:
            output.append(carry)
        return output[::-1]
