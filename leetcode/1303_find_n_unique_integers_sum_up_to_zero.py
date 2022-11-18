class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [] 

        if n % 2 == 0: 
            for i in range(1, (n / 2)+1):
                output.append(-i)
                output.append(i)
        else: 
            for i in range(1, (n / 2)+1):
                output.append(-i)
                output.append(i)
            output.append(0)
        return output