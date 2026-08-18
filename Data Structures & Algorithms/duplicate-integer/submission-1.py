class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = set()

        for val in nums:
            if val in dic:
                return True
            dic.add(val)
        
        return False