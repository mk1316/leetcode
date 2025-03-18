class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while sl[left].isalnum() != True and left < right:
                left += 1
            while sl[right].isalnum() != True and left < right:
                right -= 1
            if sl[left] != sl[right]:
                print(sl[left], sl[right])
                return False
            left += 1
            right -= 1
        return True 


