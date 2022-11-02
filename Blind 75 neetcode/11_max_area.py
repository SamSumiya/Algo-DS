'''
    Max Area

'''

from typing import List


class Solution:
    def maxArea_bf(self, height: List[int]) -> int:
        max_area = 0 
        width = len(height)
        i = 0 
        
        while i < width:
            j = i
            
            while j < width:
                smaller_height = min(height[i], height[j])
                current_width = j - 1
                current_area = smaller_height * current_width

                if max_area < current_area: 
                    max_area = current_area

                j += 1
            i += 1 
            
        return max_area