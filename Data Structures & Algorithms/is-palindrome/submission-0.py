class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.replace(" ", "")
        o = re.sub(r'[^a-zA-Z0-9\s]', '', t)
        a = o.lower()
        j = len(a) - 1
        i = 0
        count = 0
        while i < j:
            if a[i] == a[j]:
                count += 1
            i += 1
            j -= 1
        if count == int(len(a)/2):
            return True
        else:
            return False