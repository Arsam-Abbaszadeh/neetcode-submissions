# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        carry = 0
        flag = True
        p = l1
        while l2 and flag:
            if l1:
                total = l1.val + l2.val
                effective = total % 10
                carry = total // 10
                l1.val = effective

                if not l1.next and l2.next:
                    l1.next = l2.next
                    flag = False
                if not l1.next and not l2.next and carry > 0:
                    l1.next = ListNode()

                l1 = l1.next
                l2 = l2.next

                if carry > 0:
                    p1 = l1

                    while carry > 0:
                        total = carry + p1.val
                        effective = total % 10
                        carry = total // 10
                        p1.val = effective
                        if carry > 0 and not p1.next:
                            p1.next = ListNode()
                        p1 = p1.next
        return p


            
