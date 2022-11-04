'''
    118 Pascal's Triangle - Easy

    Given a random number 
    Create a nested array 
        a. if the number is 1 then return [[1]]
        b. if the number is 2 then return [[1]. [1,1]]
        c. any number greater than 2, we will need to return the next inner array with first add second number and place it right in between first and second number
        d. the first and last number will always remind 1 and 1 
    
    approach: nested loop
        1. cover the edge cases when the number is 1 or 2 then return the expected output
        2. create a variable with value of [[1], [1,1]]
        3. loop through the arg number starting from 1:
            a. since we start from 1, so we will subtract the numRows by 1 so we won't get the extra list in the output
        4. create a variale with value of [1]
        5. to get the previous inner array by accessing base[i] to get  [1, 1]
        6. loop througth the inner array and add the first and second element 
        7. insert the result of the sum to the inner variable
        8. after the loop, we will add additional 1 to the inner variable 
        9. insert the inner variable to the output nested array
        10. return the output nested array

'''


from ast import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1], [1, 1]]

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        i = 1 
        while i < numRows - 1:
            inner_list = [1]
            j = 0

            while j < len(output[i - 1]) - 1:
                sum = output[i-1][j] + output[i-1][j+1]
                inner_list.append(sum)

                j += 1
            inner_list.append(1)
            i += 1

            output.append(inner_list)
        return output
