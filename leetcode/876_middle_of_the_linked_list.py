'''


'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode_2(self, head):
        
        arr = [head]
        print(arr)
        while arr[-1].next: 
            arr.append(arr[-1].next)
        
        x = arr[len(arr) // 2]
        print(repr(x.val), 'dsddsdsds')
        for a in x: 
            print(repr(a.val)) 
    
    def __repr__(self) -> str:
        return repr(self.val)

a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')

a.next = b
b.next = c 
c.next = d
d.next = e


s = Solution()
r = s.middleNode_2(a)
print(r)