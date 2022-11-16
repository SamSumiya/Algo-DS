class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        size = len(palindrome)
        li = list(palindrome)
        ascii_a = ord('a')

        if size == 1: return '' 

        for i in range(0, size//2):
            if ord(li[i]) > ascii_a:
                li[i] = 'a'
                return ''.join(li)
        print(li[-1])
        li[-1] = 'b'
        return ''.join(li)

pa = 'aabaa'
so = Solution()

r = so.breakPalindrome(pa)
print(r)