'''
424. Longest Repeating Character Replacement

'''

class Solution(object):
    def characterReplacement_bf(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = j = 0
        hashmap = {} 
        count = 0
        max_count = 0
        size = len(s)

        while i < size: 
            
            while j < size:
                if s[j] not in hashmap: 
                    hashmap[s[j]] = 1
                else: 
                    hashmap[s[j]] += 1 
                if len(s[i:j+1]) - max(hashmap.values()) <= k:
                    count += 1
                else: 
                    hashmap[s[i]] -= 1
                    i += 1
                max_count = max(count, max_count)
                j += 1
        
            i += 1
        
        return max_count

    def characterReplacement(self, s, k):
        count = {} 
        res = 0
        l = 0 

        for i in range(len(s)): 
            count[s[i]] = 1 + count.get(s[i], 0)
            if (i - l + 1) - max(count.values()) > k: 
                count[s[l]] -= 1
                l += 1
        res = max(res, i - l + 1) 

        return res

input = 'KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF'
so = Solution()
r_1 = so.characterReplacement(input, 4)
r_2 = so.characterReplacement_bf(input, 4)
print(r_1, r_2)