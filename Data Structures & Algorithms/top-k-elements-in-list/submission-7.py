class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        res = []
        nums.sort(reverse=True)
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))  
        for i , num in enumerate(sorted_dict):
            if i < k:
                res.append(num)
        return res