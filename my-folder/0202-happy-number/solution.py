class Solution:
    def isHappy(self, n: int) -> bool:
        found = {}
        while n != 1:
            if n in found:
                return False
            found[n] = 1
            nums = list(str(n))
            n = 0 
            for num in nums:
                num = int(num)
                n += num * num

        return True

        
