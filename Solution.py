from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # edge cases
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1

        # general solution
        this, that = list1, list2
        val1, val2 = this.val, that.val
        if val1 > val2:
            that, this = this, that
        result = this
        while this and that:
            nxt_that = that.next
            nxt_this = this.next

            if not nxt_this:
                this.next = that
                break

            if that.val <= nxt_this.val:
                that.next = nxt_this
                this.next = that
                that = nxt_that

            this = this.next
        return result
