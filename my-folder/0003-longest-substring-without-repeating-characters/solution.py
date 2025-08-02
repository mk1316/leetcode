class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        res = 1
        p1 = 0
        p2 = 1
        chars = {s[p1]}

        while p2 < len(s):

            if s[p2] in chars:
                while s[p2] in chars and p1 < p2:
                    chars.remove(s[p1])
                    p1 += 1

            chars.add(s[p2])
            curr_len = p2 - p1 + 1
            
            res = max(res, curr_len)

            p2 += 1
        return res



