# no len function for nodes, return the head not a specific node

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m, n = 0,0
        temp1 = headA
        temp2 = headB

        while temp1:
            m+=1
            temp1 = temp1.next
        while temp2:
            n+=1
            temp2 = temp2.next
    
        while headA and headB:
            if headA == headB:
                return headA
            elif m > n:
                headA = headA.next
                m-=1
            elif m < n :
                headB = headB.next
                n-=1
            
            else:
                headA = headA.next
                headB = headB.next