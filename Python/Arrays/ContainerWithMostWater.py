class Solution:
    def maxArea(self, height: List[int]) -> int:
        areaMax = 0
        left = 0
        right = len(height) - 1

        while(left < right):
            area = (right - left) * min(height[left], height[right])
            areaMax = max(areaMax, area)
            if(height[left] > height[right]):
                right = right - 1
            else:
                left = left + 1
        
        return areaMax
        # Space Complexity = O(1), Time Complexity = O(n)