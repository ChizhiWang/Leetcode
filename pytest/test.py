from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digitflag = 0
        node1 = l1
        node2 = l2
        hnode = ListNode(0, None)
        lnode = hnode
        while (node1 != None and node2 != None):
            if (node1.val + node2.val + digitflag >= 10):
                digitflag = 1
                newnode = ListNode(node1.val + node2.val + digitflag - 10, None)
            else:
                digitflag = 0
                newnode = ListNode(node1.val + node2.val + digitflag, None)
            node1 = node1.next
            node2 = node2.next
            lnode.next = newnode
            lnode = lnode.next
        while (node1 != None):
            newnode = ListNode(node1.val + digitflag, None)
            if(digitflag == 1):
                digitflag = 0
            lnode.next = newnode
            lnode = lnode.next
        while (node2 != None):
            newnode = ListNode(node2.val + digitflag, None)
            if(digitflag == 1):
                digitflag = 0
            lnode.next = newnode
            lnode = lnode.next
        return hnode.next


l1 = [2,4,3]
l2 = [5,6,4]
l = Solution.addTwoNumbers(Solution, l1, l2)
print(l)