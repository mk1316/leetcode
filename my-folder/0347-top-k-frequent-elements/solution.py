class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize count and freq and res
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        # count of the elements
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # group them by freq
        for n, c in count.items():
            freq[c].append(n)

        # return the top k
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



