"""
class Solution(object):
    def isPalindrome(self, s):
        
        :type s: str
        :rtype: bool
"""

def isPalindrome(s):
     # approach: with array
     # time complexity: O(n)
     # space complexity: O(n)

     chars=[]
     # getting only the characters
     for char in s:
          if ord(char.lower()) >= 97 and ord(char.lower()) <= 122 or ord(char) >= 48 and ord(char) <= 57:
               chars.append(char.lower())    
     # checking if the characters are palindrome
     if len(chars) == 0 and len(s) != 0:
          return True
     
     for i in range(len(chars)//2):
          if chars[i] != chars[len(chars)-1-i]:
               return False
     return True

def isPalindrome(s):

     # approach: with two pointers
     # time complexity: O(n)
     # space complexity: O(1)

     left = 0
     right = len(s)-1

     while left < right:
          while left < right and not s[left].isalnum():
               left += 1
          while left < right and not s[right].isalnum():
               right -= 1

          if s[left].lower() != s[right].lower():
               return False
          
          left += 1
          right -= 1
     
     return True



     


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
