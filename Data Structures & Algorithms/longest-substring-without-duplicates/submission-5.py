class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        m, count = 0, 0
        seen = set()
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                count = (right - left) + 1
                m = max(m, count)
                right += 1
            else:
                while s[right] in seen:
                    seen.discard(s[left])
                    left += 1
        return m
        