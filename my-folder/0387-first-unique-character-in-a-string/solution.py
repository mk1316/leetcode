class Solution:
    def firstUniqChar(self, s: str) -> int:
    # add chars to a hashmap
    # with index as value
    # if not already in hashmap
    # if in hashmap set to -1
        count = {}

        for i, c in enumerate(s):
            if c in count:
                count[c] = -1
            else:
                count[c] = i

    # once done return the lowest of values greater than -1
    # if none > -1 return -1

        lowest_index = [n for n in count.values() if n > -1]
        if lowest_index:
            return lowest_index[0]
        else:
            return -1






