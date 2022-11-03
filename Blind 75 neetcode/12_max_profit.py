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

arr = [7,1,5,3,6,4]
s = Solution()
r = s.maxProfit_bf(arr)

print(r)