from typing import List


class Solution:
    def maxProfit_bf(self, prices: List[int]) -> int:
        profit = 0 
        i = 0
        size = len(prices) - 1 
        
        while i < size: 
            purchasing_price = prices[i]
            
            for selling_price in prices[i:]:
                if prices[i] > selling_price: 
                    continue
                else:
                    profit_margin = selling_price - purchasing_price
                    profit = max(profit_margin, profit)
            
            i += 1 
            
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0 
        j = 1 
        
        while j < len(prices): 
            if prices[i] > prices[j]: 
                i = j       
            else:
                max_profit = max(prices[j] - prices[i], max_profit)
            j += 1 

        return max_profit

arr = [7,1,5,3,6,4]
s = Solution()
a = s.maxProfit_bf(arr)
b = s.maxProfit(arr)

print(a,b)