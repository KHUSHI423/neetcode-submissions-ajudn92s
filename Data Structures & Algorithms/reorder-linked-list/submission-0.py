# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        # reverse from second
        prev=None
        temp=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        second=prev
        first=head
        while first and second:
            t1=first.next
            t2=second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2
            

            


        
