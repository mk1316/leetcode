class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp  = strs[0]

        for s in strs[1::]:
            if len(s) < len(lcp):
                lcp = lcp[:len(s)]
            for i in range(min(len(lcp), len(s))):
                print(lcp, s)
                if s[i] != lcp[i]:
                    if i == 0:
                        return ""
                    lcp = lcp[:i:]
                    break
        return lcp
      


