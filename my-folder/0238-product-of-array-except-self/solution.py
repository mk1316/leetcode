class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # # Input: nums = [1,2,3,4]
        length = len(nums)
        res = [1] * length

        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]

        right = nums[-1]

        for i in range(length - 2, -1, -1):
            res[i] *= right
            right *= nums[i]

        
        return res



        # # [24,12,8,6]
