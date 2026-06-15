# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=daily-question&envId=2026-06-15

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head

        slow=fast=dummy
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        slow.next=slow.next.next
        return dummy.next
        