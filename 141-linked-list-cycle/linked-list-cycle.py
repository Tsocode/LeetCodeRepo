# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head #initialize the position for the slow and fast pointers
        while fast and fast.next != None: #if the fast pointer reaches end of linkedlist
            slow = slow.next #move the slow node interval of 1
            fast = fast.next.next #move the fast node interval of 2
            if slow == fast: #when slow = fast then a cycle
                return True #show that it is a cycle
        return False #not a cycle

        