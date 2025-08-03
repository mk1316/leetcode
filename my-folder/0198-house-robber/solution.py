class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev = curr_max = 0

        for num in nums:
            temp = max(curr_max, prev + num)
            prev = curr_max
            curr_max = temp

        return curr_max
