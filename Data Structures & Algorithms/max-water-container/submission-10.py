class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        max_a = (n-1)*min(heights[left],heights[right])

        while left<=right:
            print(max_a)
            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1

            max_a = max(max_a,(right-left)*min(heights[left],heights[right]))
        print(left,right) 
        return max_a