class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        for i, val in enumerate(nums):
            need = target - val
            if need in vals:
                return [vals[need], i]
            vals[val] = i

        return 0