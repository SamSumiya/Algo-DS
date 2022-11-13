'''
3. Longest Substring Without Repeating Characters


'''


class Solution(object):
    def lengthOfLongestSubstring_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        i = 0
        j = 1
        count = 1
        max_count = 0

        while j < len(s):
            if s[j] not in s[i:j]:
                count += 1
                j += 1
            else:
                i += 1
                j = i + 1
                count = 1
            max_count = max(count, max_count)

        return max_count

    def length_of_longest_substring_2(self, s):
        temp_holder = []
        max_count = 0

        for val in s:
            if val not in temp_holder:
                temp_holder.append(val)
            else:
                idx = temp_holder.index(val)
                temp_holder = temp_holder[idx+1:]
                temp_holder.append(val)
            max_count = max(max_count, len(temp_holder))
        return max_count

    def lengthOfLongestSubstring_3(self, s):
        sets = set()
        i = 0
        max_len = 0

        for val in s:
            while val in sets:
                sets.remove(s[i])
                i += 1
            sets.add(val)

            max_len = max(max_len, len(sets))

        return max_len


string = "pwwkew"

su = Solution()
r = su.length_of_longest_substring(string)

print(r)


'''
abc    

'''