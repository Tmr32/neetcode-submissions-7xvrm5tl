# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, curr1: Optional[ListNode], curr2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head

        while curr1 and curr2:
            if curr1.val < curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
            dummy = dummy.next

        if curr1:
            dummy.next = curr1
        elif curr2:
            dummy.next = curr2

        return head.next
