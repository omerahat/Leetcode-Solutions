
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
"""

def twoSum(nums,target):
     # Brute Force
     # Time Complexity: O(n^2)
     # Space Complexity: O(1)
     for i in range(len(nums)):
          for j in range(i+1,len(nums)):
               if nums[i]+nums[j]==target:
                    return [i,j]
     return []


def twoSum(nums,target):
     # Two-pass Hash Table
     # Time Complexity: O(n)
     # Space Complexity: O(n)
     d={}
     for i in range(len(nums)):
          if (target-nums[i]) not in d:
               d[nums[i]]=i
          else:
               return [d[target-nums[i]],i]
          

