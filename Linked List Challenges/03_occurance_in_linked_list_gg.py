class Solution:
    def count(self, head, search_for):
        count = 0 
        
        while head: 
            if head.data == search_for: 
                count += 1 
            head = head.next
            
        return count 
            
