from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # edge case
        if not head or not head.next:
            return False
        ptr_1_step = ptr_2_steps = head
        while ptr_1_step and ptr_2_steps:
            ptr_1_step = ptr_1_step.next
            try:
                ptr_2_steps = ptr_2_steps.next.next
            except Exception:
                return False
            if ptr_1_step is ptr_2_steps:
                return True
            # if ptr_1_step.val == ptr_2_steps.val:
            #     return True
        return False
