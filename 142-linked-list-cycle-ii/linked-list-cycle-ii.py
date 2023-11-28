# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head #initialize the position for the slow and fast pointers
        while fast and fast.next != None: #if the fast pointer reaches end of linkedlist
            slow = slow.next #move the slow node interval of 1
            fast = fast.next.next #move the fast node interval of 2
            if slow == fast: #when slow = fast then a cycle
                break #end the loop and jump to calcualting the pointer position when it happened
        else: 
            return None #there is no cycle

        p1 = head #initialize p1 to head node
        p2 = slow #initialize p2 to slow node

        while p1 != p2: #while we have not found the interval where the cycle began
            p1 = p1.next #move p1 next step
            p2 = p2.next #move p2 next step

        return p1 #return value of p1 gotten



        