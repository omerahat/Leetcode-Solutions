"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
     
        :type head: ListNode
        :type n: int
        :rtype: ListNode
"""
def removeNthFromEnd(head, n):

     # Time Complexity: O(n)
     # Space Complexity: O(1)
     
     current = head

     lenght = 0

     while current is not None:
          current = current.next
          lenght += 1
     
     if lenght == n:
          tempHead = head.next
          del head
          return tempHead
     
     current = head

     for i in range(lenght - n - 1):
          current = current.next
     
     temp = current.next
     current.next = temp.next
     del temp
     
     return head

def removeNthFromEnd(head, n):

     # Time Complexity: O(n)
     # Space Complexity: O(1)

     slowPtr = head
     fastPtr = head

     for i in range(n):
          if fastPtr.next is None:
               tempHead = head.next
               del head
               return tempHead
          fastPtr = fastPtr.next
     
     while fastPtr.next is not None:
          slowPtr = slowPtr.next
          fastPtr = fastPtr.next

     tempNode = slowPtr.next
     slowPtr.next = tempNode.next
     del tempNode

     return head
     

     
