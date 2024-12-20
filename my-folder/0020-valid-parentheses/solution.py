class Solution:
    def isValid(self, s: str) -> bool:
        p = 0
        c = 0
        b = 0
        order = []
        for char in s:
            if char == "(":
                p += 1
                order.append(char)
            elif char == ")":
                if p == 0 or "(" != order[-1]:
                    return False
                else:
                    p -= 1
                    order.pop()
            elif char == "{":
                c += 1
                order.append(char)
            elif char == "}":
                if c == 0 or "{" != order[-1]:
                    return False
                else:
                    c -= 1
                    order.pop()
            elif char == "[":
                b += 1
                order.append(char)
            elif char == "]":
                if b == 0 or "[" != order[-1]:
                    return False
                else:
                    b -= 1
                    order.pop()
        if p == 0 and c == 0 and b == 0:
            return True
        else:
            return False

