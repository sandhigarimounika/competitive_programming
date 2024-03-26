# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        temp1 = head
        len = 0

        while temp1 is not None :
            len += 1
            temp1 = temp1.next

        k %= len
        if k == 0:
            return head

        slow = head
        fast = head

        for i in range(k):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        tmp = slow.next
        slow.next = None
        fast.next = head
        head = tmp

        return head