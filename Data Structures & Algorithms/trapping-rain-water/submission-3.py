class Solution:
    def trap(self, height: List[int]) -> int:
        w = 0
        i = 1
        while i < len(height):
            m = min(max(height[:i]), max(height[i:]))
            if m == 0:
                i += 1
            elif m > height[i]:
                w += m - height[i]
                i += 1
            elif m < height[i] or m == height[i]:
                i += 1
        return w