'''
3. Longest Substring Without Repeating Characters


'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return 0 

        i = 0
        j = 1
        sub_str = '' 
        count = 1
        max_count = 0

        while j < len(s) : 
            if s[j] not in s[i:j]: 
                print(s[i], s[j], count, s[i:j], 'if ')
                print(s[j] not in s[i:j])
                count += 1
                j += 1
            else:
                print(s[j], s[i], count, s[i:j], 'e;se')
                i += 1 
                j = i + 1
                count = 1

            max_count = max(count, max_count)
            
        return max_count
    
string = "dvdf"

su = Solution()
r = su.lengthOfLongestSubstring(string)

print(r)