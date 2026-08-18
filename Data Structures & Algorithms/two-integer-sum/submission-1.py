class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}

        for i, val in enumerate(nums):
            need = target - val
            if need in have:
                return [have[need], i]
            have[val] = i

        return List[int]