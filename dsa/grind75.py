from collections import Counter, deque
from typing import Deque, Optional

from _common import ListNode, TreeNode


# https://leetcode.com/problems/maximum-subarray
def max_subarray(nums: list[int]) -> int:
    """
    >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> max_subarray([1])
    1
    >>> max_subarray([5, 4, -1, 7, 8])
    23
    """
    max_ending_here = max_so_far = nums[0]
    for i in range(1, len(nums)):
        max_ending_here = max(max_ending_here + nums[i], nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# https://leetcode.com/problems/flood-fill
def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    """
    >>> flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    >>> flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 0)
    [[0, 0, 0], [0, 0, 0]]
    """
    row, col = len(image), len(image[0])
    visited: list[list[int]] = [[False] * col for _ in range(row)]
    visited[sr][sc] = True
    q: Deque[tuple[int, int]] = deque([(sr, sc)])
    orig = image[sr][sc]
    image[sr][sc] = color
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < row
                and 0 <= nc < col
                and image[nr][nc] == orig
                and not visited[nr][nc]
            ):
                visited[nr][nc] = True
                q.append((nr, nc))
                image[nr][nc] = color
    return image


# https://leetcode.com/problems/binary-search
def search(nums: list[int], target: int) -> int:
    """
    >>> search([-1, 0, 3, 5, 9, 12], 9)
    4
    >>> search([-1, 0, 3, 5, 9, 12], 2)
    -1
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


# https://leetcode.com/problems/valid-anagram
def is_anagram(s: str, t: str) -> bool:
    """
    >>> is_anagram("anagram", "nagaram")
    True
    >>> is_anagram("rat", "car")
    False
    >>> is_anagram("ab", "a")
    False
    """
    scnt = Counter(s)
    tcnt = Counter(t)
    if len(scnt) != len(tcnt):
        return False
    for k, v in tcnt.items():
        if scnt[k] != v:
            return False
    return True


# https://leetcode.com/problems/invert-binary-tree
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    >>> TreeNode.to_list(invert_tree(TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])))
    [4, 7, 2, 9, 6, 3, 1]
    >>> TreeNode.to_list(invert_tree(TreeNode.from_list([2, 1, 3])))
    [2, 3, 1]
    >>> TreeNode.to_list(invert_tree(TreeNode.from_list([])))
    []
    """
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# https://leetcode.com/problems/valid-palindrome
def is_palindrome(s: str) -> bool:
    """
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome(" ")
    True
    """
    start, end = 0, len(s) - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start, end = start + 1, end - 1
    return True


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
def max_profit(prices: list[int]) -> int:
    """
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    >>> max_profit([7, 6, 4, 3, 1])
    0
    """
    min_so_far = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_so_far)
        min_so_far = min(min_so_far, prices[i])
    return max_profit


# https://leetcode.com/problems/merge-two-sorted-lists
def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    >>> ListNode.to_list(merge_two_lists(ListNode.from_list([1, 2, 4]), ListNode.from_list([1, 3, 4])))
    [1, 1, 2, 3, 4, 4]
    >>> ListNode.to_list(merge_two_lists(ListNode.from_list([]), ListNode.from_list([])))
    []
    >>> ListNode.to_list(merge_two_lists(ListNode.from_list([]), ListNode.from_list([0])))
    [0]
    """
    dummy = ListNode()
    ptr = dummy
    while list1 and list2:
        if list1.val < list2.val:
            ptr.next = list1
            list1 = list1.next
        else:
            ptr.next = list2
            list2 = list2.next
        ptr = ptr.next
    if list1:
        ptr.next = list1
    else:
        ptr.next = list2
    return dummy.next


# https://leetcode.com/problems/valid-parentheses
def is_valid(s: str) -> bool:
    """
    >>> is_valid("()")
    True
    >>> is_valid("()[]{}")
    True
    >>> is_valid("(]")
    False
    >>> is_valid("([])")
    True
    >>> is_valid("([))")
    False
    """
    brackets = {")": "(", "}": "{", "]": "["}
    stack: list[str] = []
    for c in s:
        if c in brackets:
            if stack and stack[-1] == brackets[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


# https://leetcode.com/problems/two-sum
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3, 3], 6)
    [0, 1]
    """
    index: dict[int, int] = dict()
    for i, n in enumerate(nums):
        need = target - n
        if need in index:
            return [index[need], i]
        index[n] = i
    raise Exception("no solution found")
