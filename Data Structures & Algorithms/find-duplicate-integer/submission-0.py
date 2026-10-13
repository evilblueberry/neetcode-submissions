class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Input: nums = [1,2,3,2,2]
        # Output: 2

        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)


        return 0