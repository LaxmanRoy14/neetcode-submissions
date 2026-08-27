class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if not f[right].isalnum():
                right -= 1
            elif not f[left].isalnum():
                left += 1
            elif f[right].isalnum() and f[left].isalnum():
                if f[right] == f[left]:
                    left += 1
                    right -= 1
                else:
                    return False
        return True