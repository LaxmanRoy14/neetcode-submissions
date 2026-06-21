from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for i in strs:
            k = "".join(sorted(i))
            a[k].append(i)
        return list(a.values())