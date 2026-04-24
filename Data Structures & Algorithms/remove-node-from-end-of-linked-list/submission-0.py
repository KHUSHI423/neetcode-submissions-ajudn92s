# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length of ll
        l=0
        h1=head
        while h1 :
            l+=1
            h1=h1.next
        if n==l:
            return head.next
        #remove the node
        x= l-n
        h2=head
        prev=None
        while h2:
            if x==0:
                temp=h2.next
                h2.next=None
                prev.next=temp
                break
            prev=h2
            h2=h2.next
            x-=1
        return head

        