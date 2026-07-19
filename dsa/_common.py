from __future__ import annotations

from collections import deque
from typing import Deque, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, nums: list[int]) -> Optional[ListNode]:
        if not nums:
            return None
        dummy = cls()
        ptr = dummy
        for n in nums:
            ptr.next = cls(n)
            ptr = ptr.next
        return dummy.next

    @classmethod
    def to_list(cls, list: Optional[ListNode]) -> list[int]:
        nums: list[int] = []
        while list:
            nums.append(list.val)
            list = list.next
        return nums


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, nums: list[Optional[int]]) -> Optional[TreeNode]:
        if not nums or nums[0] is None:
            return None
        root = cls(nums[0])
        q = deque([root])
        i = 1
        while q and i < len(nums):
            node = q.popleft()
            if i < len(nums) and (n := nums[i]) is not None:
                node.left = cls(n)
                q.append(node.left)
            i += 1
            if i < len(nums) and (n := nums[i]) is not None:
                node.right = cls(n)
                q.append(node.right)
            i += 1
        return root

    @classmethod
    def to_list(cls, root: Optional[TreeNode]) -> list[Optional[int]]:
        if root is None:
            return []
        res: list[Optional[int]] = []
        q: Deque[Optional[TreeNode]] = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        while res and res[-1] is None:
            res.pop()
        return res
