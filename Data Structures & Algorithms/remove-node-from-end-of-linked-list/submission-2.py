# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        fast = head
        slow = head
        m = 0
        while m < n and fast.next:
            fast = fast.next
            m += 1
        
        if not fast.next and n > m:
            head = head.next
            return head

        while fast.next:
            fast = fast.next
            slow = slow.next

        
        slow.next = slow.next.next

        return head