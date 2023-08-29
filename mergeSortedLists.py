# Remember, to make an empty ListNode declare it as ListNode(0), you cannot append a single node, just move the entire linked list to the new pointer and keep changing the next,
# If you want to append the entire list, no need to iterate through just use next.



class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        
        merged = curr = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2

        return merged.next