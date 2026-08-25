class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        sbstr = set()
        l = 0

        for r in range(len(s)):
            while s[r] in sbstr:
                sbstr.remove(s[l])
                l += 1
            sbstr.add(s[r])
            res = max(res, r - l + 1)
        return res
        

