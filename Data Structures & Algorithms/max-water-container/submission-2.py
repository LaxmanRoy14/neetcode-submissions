class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        wc = 0
        while left < right:
            water = min(heights[left], heights[right])
            width = right - left
            wc = max(water * width, wc)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return wc