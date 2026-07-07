class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # Add the current character to our frequency map
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Track the maximum frequency of any single character seen so far in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # If the current window is invalid, shrink it from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Update the maximum length found
            max_length = max(max_length, right - left + 1)
            
        return max_length