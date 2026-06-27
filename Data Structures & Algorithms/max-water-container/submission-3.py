class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        best_area = 0

        while l < r:
            base = r - l
            h = heights[l] if heights[l] < heights[r] else heights[r]
            area = base * h

            if area > best_area:
                best_area = area

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            elif heights[r - 1] > heights[l + 1]:
                r -= 1
            else:
                l += 1
        return best_area