"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
"""

def containsDuplicate(nums):
     # Approach: Hash Table
     # Time Complexity: O(n)
     # Space Complexity: O(n)
     
     numDict = {}
     for num in nums:
          if num in numDict:
               return True
          else:
               numDict[num] = 1
     return False

