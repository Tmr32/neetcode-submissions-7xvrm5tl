class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        j, k = 0, len(heights)-1
        #area = (j - k) * min(heights[j], heights[k])
        #   j       k   
        #[1,7,2,5,4,7,3,6]
        #we move the pointer that has the smaller height value

        while j < k:
            area = (k - j) * min(heights[j], heights[k])
            mx = max(mx, area)
            
            if heights[j] < heights[k]:
                j += 1
            else:
                k -= 1
                
        return mx