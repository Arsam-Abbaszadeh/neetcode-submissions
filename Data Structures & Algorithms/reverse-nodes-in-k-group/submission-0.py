# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverseSubList(prev, start, final):
            # print(start.val)
            # print(final.val)
            # print()
            after = final.next
            prev = prev # try not to touch prev directly
            # get both of these in place to prevent going out too far
            sub_prev = start
            sub_head = start.next
            while sub_head != after: # while we are still in our sublist
                # change head pointer to prev while being able to move head to the next and prev to the current head
                temp = sub_head.next
                sub_head.next = sub_prev
                sub_prev = sub_head
                sub_head = temp
            
            if prev:
                prev.next = final
            start.next = after


        start = head
        final = head
        prev = None
        first_iter = True

        while final:
            count = 1
            while count < k and final:
                final = final.next
                count += 1
            if final:
                reverseSubList(prev, start, final)
                # start and finish should be in reverse order
                if first_iter:
                    head = final
                    first_iter = False
                prev = start
                final = start.next
                start = start.next

        return head