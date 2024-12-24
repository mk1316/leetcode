class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1
        prev = 0
        for i in range(46):
            if i < n:
                val = curr + prev
                prev = curr
                curr = val
            else:
                return curr
        
