# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head=tail=None
        h1=list1
        h2=list2
        if h1.val<h2.val:
            head=tail=h1
            h1=h1.next
        else:
            head=tail=h2
            h2=h2.next
        
        while h1 and h2:
            if h1.val<h2.val:
                tail.next=h1
                h1=h1.next
            else:
                tail.next=h2
                h2=h2.next
            tail=tail.next
        if h1 is not None:
            tail.next=h1
        else:
            tail.next=h2
        return head


        

        