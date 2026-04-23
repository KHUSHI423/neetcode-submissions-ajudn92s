# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        temp=None
        prev=None
        while curr: #0 1 2 3
            temp=curr.next #1 2 3
            curr.next=prev#none 0 1
            prev=curr#0 1 2
            curr=temp#1 2 3

        return prev


        