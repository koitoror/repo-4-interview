# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# from typing import ListNode
# from __future__ import annotations

# class ListNode:
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ret = curr = ListNode(0)

        carry = 0

        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10
            curr.next = ListNode(val)
            curr = curr.next

        return ret.next