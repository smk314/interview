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
