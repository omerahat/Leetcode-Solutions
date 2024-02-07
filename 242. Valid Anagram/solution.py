"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
"""

def isAnagram(s, t):
     # Time Complexity: O(n)
     # Space Complexity: O(n)
     
     dictChars = {}

     if len(s) != len(t):
          return False
     
     for add in s:
          if add not in dictChars.keys():
               dictChars[add] = 1
          else:
               dictChars[add] += 1
     
     for delete in t:
          if delete not in dictChars.keys():
               return False

          dictChars[delete] -= 1

     if min(dictChars.values()) == max(dictChars.values()) == 0:
          return True
     
     return False
      
