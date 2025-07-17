class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = []
        
        for char in s:
            if char.isalnum():
                filtered_chars.append(char.lower())

        if filtered_chars == filtered_chars[::-1]:
            return True
        return False



