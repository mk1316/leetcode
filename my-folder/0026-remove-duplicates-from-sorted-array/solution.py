class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = -101
        for num in nums[:]:
            if num == prev_num:
                nums.remove(num)
                prev_num = num
            else:
                prev_num = num
        
        

