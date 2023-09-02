"""
Linked List Cycle

Input: head = [3, 2, 0 , -4], position = 1  // a linked list
Output: True
Explaination: There is a cycle in the linked list, 
              where the tail connects to the 1st node (0-indexed).

Input: head = [1, 2], position = 0  // a linked list
Output: True
Explaination: There is a cycle in the linked list,
              where tail connects to the 0th node.
"""

# * Definition for singly linked list
# * class ListNode(object):
# *     def __init__(self, x)
# *         self.val = x
# *         self.next = None

class Solution(object):

    def hasCycle(self, head):
        """
        :type: head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                return True
        return False