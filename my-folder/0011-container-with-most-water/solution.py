class Solution:
    def maxArea(self, height: List[int]) -> int:
        # l = begining
        l = 0
        # r = end
        r = len(height) - 1
        # area = 0
        area = 0
        # while l < r:
        while l < r:
        #     x = r - l
        #     y = smaller of x or y height 
        #     move smaller pointer 1 over
            x = r - l
            if height[l] <= height[r]:
                y = height[l]
                l += 1
            else:
                y = height[r]
                r -= 1

        #     area = greater of area or x * y
            area = max(area, x * y)

        # return area
        return area





