class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = 0
        output = []

        for val in candies:
            if max_num < val:
                max_num = val

        for val in candies:
            if val + extraCandies >= max_num:
                output.append(True)
            else:
                output.append(False)

        return output
