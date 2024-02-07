"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

"""
def lengthOfLongestSubstring(s):
     # Brute Force
     # Time Complexity: O(n^2)
     # Space Complexity: O(n^2)
    
    hashtable = {0: 0}

    if len(s) == 0:
        return 0

    for i in range(len(s)):
          if not len(s[i:i + max(hashtable.values())]) < len(set(s[i:i + max(hashtable.values())])):
          
               for j in range(i + 1, len(s) + 1):
                    substr = s[i:j]

                    if len(substr) == len(set(substr)):
                         hashtable[substr] = len(substr)

                    max_value = max(hashtable.values(), default=0)

    return max_value

def lengthOfLongestSubstring(s):
     # Sliding Window
     # Time Complexity: O(n)
     # Space Complexity: O(n)

     charSet = set()
     left = 0
     result = 0

     for right in range(len(s)):
          while s[right] in charSet:
               charSet.remove(s[left])
               left += 1
          charSet.add(s[right])
          result = max(result,right - left + 1)
     
     return result
