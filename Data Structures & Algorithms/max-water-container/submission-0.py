class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: height = [1,7,2,5,4,7,3,6]
        # two pointers
        # l, r 

        # Output: 36
        max = 0
        l, r = 0, len(heights) - 1

        while l < r:
            for i in range(len(heights)):
                height = min(heights[l], heights[r])
                width = r - l
                area = width * height
                print(area)

                if area > max:
                    max = area
                
                if heights[l] > heights[r]:
                    r -= 1
                else:
                    l += 1
            
        return max
                

