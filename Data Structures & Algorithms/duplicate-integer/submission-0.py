class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=[]
        for i in nums:
            if i in seen:
                return True
                break;
            else:
                seen.append(i)
        return False