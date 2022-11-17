'''
121. Best Time to Buy and Sell Stock

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0 
        j = 1
        max_profits = 0 

        while j < len(prices): 
            if prices[i] > prices[j]: 
                i = j
            else:
                max_profits = max(prices[j] - prices[i], max_profits)
            
            j += 1 
        
        return max_profits

        