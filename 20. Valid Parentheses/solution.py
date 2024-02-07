def isValid(s):
     # Time Complexity: O(n)
     # Space Complexity: O(n)
     
     stack = []
     parentheses = {')': '(', ']': '[', '}': '{'}
     
     if len(s) == 0:
          return True
     
     if len(s) % 2 == 1:
          return False
     
     if s[0] in parentheses.keys():
          return False
     
     for char in s:
          if char in parentheses.values():
               stack.append(char)
          elif char in parentheses.keys():
               if len(stack) == 0:
                    return False
               if stack[-1] == parentheses[char]:
                    stack.pop()
               else:
                    return False
     
     if len(stack) == 0:
          return True
     
     return False
