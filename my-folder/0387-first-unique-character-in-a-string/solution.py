class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # make an empty hash map
        count = {}

        # for each char in string:
        for char in s:
        #     if char not in hash:
            if char not in count:
        #         set value to 0
                count[char] = 0
        #     inc count by 1
            count[char] += 1


        # for each index, char in string:
        for i in range(len(s)):
        #     if value of char in hash == 1
            if count[s[i]] == 1:
        #         return index
                return i
        return -1

