class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue

            l = x + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + nums[x]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else: 
                    ans.append([nums[l], nums[r], nums[x]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return ans

