class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        not_in = []
        set_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                not_in.append(i)
        return not_in
