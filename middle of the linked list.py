# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        tmp=len(stack)//2+1
        return stack[tmp-1]    