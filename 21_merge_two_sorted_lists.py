# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()  # Dummy node to start the merged list
        tail = merged #

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # If the any of the list is not empty yet, add them in the merged 
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return merged.next  

#Time Complexity: O(m+n)
#Space Complexitity: O(1)