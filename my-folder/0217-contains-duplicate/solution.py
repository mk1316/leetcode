class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # the length of the array nums -> the length of a set(nums)
        if len(nums) == len(set(nums)):
            return False
        return True
