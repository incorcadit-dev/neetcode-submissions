class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maximum = 0

        while r > l:
            maximum = max(maximum, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1

            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maximum


            
        