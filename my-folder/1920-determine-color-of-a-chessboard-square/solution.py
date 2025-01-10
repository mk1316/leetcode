class Solution:
    def squareIsWhite(self, c: str) -> bool:
        return (ord(c[0])-1 + int(c[1])) % 2 == 0
