# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head #set the slow pointer to head of node
        f = head #set the fast pointer to head of node

        while f and f.next: # ensure that f is not NONE and that f.next exists to not get NonetypeError
            s = s.next #next step the slow pointer takes
            f = f.next.next #next two steps that the fast pointer takes
            if s == f: #check when they are equal (cyclical linkedlist)
                return True
        return False #else non-cyclical: FALSE

        