class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()
        l, r = 0, len(s) - 1

        while l <= r:
            print(lowered[l], lowered[r])
            if not lowered[l].isalnum():
                l += 1
            elif not lowered[r].isalnum():
                r -= 1
            elif lowered[l] != lowered[r]:
                return False
            else:
                l += 1
                r -= 1
        return True


                

