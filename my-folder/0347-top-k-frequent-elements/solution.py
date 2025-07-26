class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count all the elements in the array 
        count = {}
        freq = [[] for i in range(len(nums) + 1)]


        for num in nums:
            count[num] = 1 + count.get(num, 0)



        # then bucket sort
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # then return the top k in return order
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # nums = [1,1,1,2,2,3], k = 2

        # count = {
        #     1 : 3
        #     2 : 2
        #     1 : 1
        # }

        # bucket sort

        # 0 | 1 | 2 | 3 | .. | len(k)
        #     3   2   1

        #     returns [1, 2]

