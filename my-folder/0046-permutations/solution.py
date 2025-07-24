class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(curr):
            if curr == len(nums):
                res.append(nums[:])
                return

            for i in range(curr, len(nums)):
                nums[curr], nums[i] = nums[i], nums[curr]
                backtrack(curr + 1)
                nums[curr], nums[i] = nums[i], nums[curr]
        backtrack(0)
        return res

        
        
