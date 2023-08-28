# Empty list, append values by iterating, convert to int using map and join

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []

        while head:
            lst.append(head.val)
            head = head.next
        
        return int(''.join(map(str, lst)),2)