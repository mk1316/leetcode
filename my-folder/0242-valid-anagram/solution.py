class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check their lens - if not = return false
        if len(s) != len(t):
            return False

        chars = {}

        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char in t:
            if char not in chars:
                return False
            else:
                if chars[char] == 1:
                    del chars[char]
                else:
                    chars[char] -= 1
        
        if chars:
            return False
        return True
