class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        val = 0
        for item in s[::-1]:
            if item != " ":
                val += 1
            elif item == " ":
                if val != 0:
                    return val
        return val



