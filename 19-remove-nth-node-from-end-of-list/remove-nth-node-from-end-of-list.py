# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        a.pop(-n)
        print(a)
        if len(a)==0:
            return None
        h1 = ListNode(a[0])
        t = h1
        v = 1
        while v < len(a):
            t.next = ListNode(a[v])
            t = t.next
            v+=1
        return h1