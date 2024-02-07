"""
class Solution(object):
    def groupAnagrams(self, strs):
        :type strs: List[str]
        :rtype: List[List[str]]
"""
def groupAnagrams(strs):
     # Time Complexity: O(nklogk)
     # Space Complexity: O(nk)
     # n = len(strs)
     # k = max(len(s) for s in strs)
     
     d = {}
     for i in strs:
          sortedWord = "".join(sorted(i))
          if sortedWord not in d:
               d[sortedWord] = [i]
          else:
               d[sortedWord].append(i)
     return d.values()
     

