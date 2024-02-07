"""
class Solution(object):
    def search(self, nums, target):
        :type nums: List[int]
        :type target: int
        :rtype: int
        
"""

def search(nums, target):
     # Time Complexity: O(log n)
     # Space Complexity: O(1)

     left = 0
     right = len(nums) - 1

     while left <= right:

          middle = (left + right) // 2

          if target == nums[middle]:
               return middle
          
          # right side
          if nums[left] <= nums[middle]:
               if target > nums[middle] or target < nums[left]:
                    left = middle + 1
               else:
                    right = middle - 1
          # left side
          else:
               if target < nums[middle] or target > nums[right]:
                    right = middle - 1 
               else:
                    left = middle + 1 
                
     return -1 

          



           
                

