# ===============
# Two Pointers
# https://www.hellointerview.com/learn/code/two-pointers/overview
# ===============

# https://www.hellointerview.com/learn/code/two-pointers/3-sum
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    >>> three_sum([-1, 0, 1, 2, -1, -1])
    [[-1, -1, 2], [-1, 0, 1]]
    """
    nums.sort()
    res: list[list[int]] = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        l, r = i + 1, len(nums) - 1  # noqa: E741
        while l < r:
            sum = nums[l] + nums[r]
            if sum < target:
                l += 1  # noqa: E741
            elif sum > target:
                r -= 1
            else:  # sum == target
                res.append([nums[i], nums[l], nums[r]])
                l += 1  # noqa: E741
                while l < r and nums[l] == nums[l - 1]:
                    l += 1  # noqa: E741
                r -= 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    return res


# https://www.hellointerview.com/learn/code/two-pointers/two-sum
def two_sum(nums: list[int], target: int) -> bool:
    """
    >>> two_sum([1, 3, 4, 6, 8, 10, 13], 13)
    True
    >>> two_sum([1, 3, 4, 6, 8, 10, 13], 6)
    False
    """
    l, r = 0, len(nums) - 1  # noqa: E741
    while l < r:
        sum = nums[l] + nums[r]
        if sum < target:
            l += 1  # noqa: E741
        elif sum > target:
            r -= 1
        else:
            return True
    return False


# https://www.hellointerview.com/learn/code/two-pointers/container-with-most-water
def max_area(heights: list[int]) -> int:
    """
    >>> max_area([3, 4, 1, 2, 2, 4, 1, 3, 2])
    21
    >>> max_area([1, 2, 1])
    2
    """
    left = [0]
    for i in range(1, len(heights)):
        if heights[i] > heights[left[-1]]:
            left.append(i)
    right = [len(heights) - 1]
    for i in range(len(heights) - 2, -1, -1):
        if heights[i] > heights[right[-1]]:
            right.append(i)
    l = r = max_area = 0  # noqa: E741
    while l < len(left) and r < len(right) and left[l] < right[r]:
        lh, rh = heights[left[l]], heights[right[r]]
        max_area = max(max_area, min(lh, rh) * (right[r] - left[l]))
        if lh < rh:
            l += 1  # noqa: E741
        else:
            r += 1
    return max_area
