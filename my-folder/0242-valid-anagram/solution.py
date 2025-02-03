class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashT, hashS = {}, {}
        
        for i in range(len(s)):
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
        return hashT == hashS

        
