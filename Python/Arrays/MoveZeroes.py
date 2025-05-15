from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0

        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[j] = nums[i]
                j += 1
        
        for i in range (j, len(nums)):
            nums[i] = 0
        """
        Do not return anything, modify nums in-place instead.
        """
        