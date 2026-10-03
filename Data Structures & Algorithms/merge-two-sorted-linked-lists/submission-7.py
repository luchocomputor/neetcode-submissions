# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        current = merged
        current1 = list1
        current2 = list2
        while current1 or current2:
            if current1 == None:
                current.next = ListNode(current2.val)
                current2 = current2.next
            elif current2 == None:
                current.next = ListNode(current1.val)
                current1 = current1.next

            else:
                if current1.val <= current2.val:
                    current.next = ListNode(current1.val)
                    current1 = current1.next
                else:
                    current.next = ListNode(current2.val)
                    current2 = current2.next
                
            current = current.next

        return merged.next


        