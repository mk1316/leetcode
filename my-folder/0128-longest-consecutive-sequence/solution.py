class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # curr_max = 0
        curr_max = 0 
        s_nums = set(nums)
        # set of nums
        #     for num in set:
        for num in nums:
            if num not in s_nums:
                continue
        #         l = num - 1
        #         r = num + 1
        #         cons = 1
            l, r = num - 1, num + 1
            cons = 1
        #         while l in set:
        #             cons += 1
        #             delete l from set
        #             l -= 1
            while l in s_nums:
                cons += 1
                s_nums.remove(l)
                l -= 1

        #         while r in set:
        #             cons += 1
        #             delete r from set
        #             r += 1
            while r in s_nums:
                cons += 1
                s_nums.remove(r)
                r += 1

        #         del num from set
        #         curr_max = max(cons, curr_max)
            s_nums.remove(num)
            curr_max = max(cons, curr_max)
        # return curr_max
        return curr_max
