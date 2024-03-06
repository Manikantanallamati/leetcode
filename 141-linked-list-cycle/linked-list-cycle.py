# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpointer = head
        fastpointer = head
        while slowpointer!=None and fastpointer!=None and fastpointer.next != None:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next
            if slowpointer==fastpointer:
                return True
        return False
