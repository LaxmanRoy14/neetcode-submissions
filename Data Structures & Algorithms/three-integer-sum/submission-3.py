class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        r = []
        
        for i in range(len(n)):
            # Bug Fix 2: Skip duplicates for the first element
            if i > 0 and n[i] == n[i - 1]:
                continue
                
            target = -n[i]
            k = i + 1
            j = len(n) - 1
            
            while k < j:
                if n[k] + n[j] < target:
                    k += 1
                elif n[k] + n[j] > target:
                    j -= 1
                else:
                    r.append([n[i], n[k], n[j]]) # Keeps the order n[i], n[k], n[j]
                    
                    # Bug Fix 1: Instead of breaking, update pointers
                    k += 1
                    j -= 1
                    
                    # Additional Optimization: Skip duplicates for the second element
                    while k < j and n[k] == n[k - 1]:
                        k += 1
                        
        return r