class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers 
        # l and r pointer
        l = 0 
        r = len(numbers) - 1 

        # while l < r
        while l < r:
        # if l + r > target
        #     r - 1
        # elif
        #     l + 1
        # else equal
        #     return [ l + 1, r + 1]
            total = numbers[l] + numbers[r]

            if total > target:
                r -= 1
            elif total < target:
                l += 1 
            else:
                return [l + 1, r + 1]


