class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        
        count = {}
        res = 0
        l = 0
        most = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most = max(most, count[s[r]])

            while (r - l + 1) - most > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, (r - l + 1))

        return res


        # while r < len(s):
        #     print(l, r)
        #     if (r - l + 1) <= most + k:
        #         r += 1
        #         count[s[r]] = 1 + count.get(s[r], 0)
        #         res = max(res, (r - l + 1))
        #         most = max(most, count[s[r]])
                
            
        #     else:
        #         count[s[l]] -= 1
        #         l += 1
        # return res

