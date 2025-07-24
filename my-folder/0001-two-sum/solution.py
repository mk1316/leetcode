class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Input: nums = [2,7,11,15], target = 9
        # Output: [0,1]
        
        # pairs = {}
        pairs = {}

        # iterate through the array
        for i in range(len(nums)):
        # check pairs for num
        #     return [pairs[num], index of num]
            if nums[i] in pairs:
                return [pairs[nums[i]], i]
        # else
        #     {target - num :  index of num} -> pairs

            else:
                pairs[target - nums[i]] = i

        
        # time -> O(n)
        # space -> O(n)

