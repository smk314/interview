# ===============
# Two Pointers
# https://www.hellointerview.com/learn/code/two-pointers/overview
# ===============

# https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water
def trapping_water(height: list[int]) -> int:
    """
    >>> trapping_water([3, 4, 1, 2, 2, 5, 1, 0, 2])
    10
    """
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            if height[left] > left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
        else:
            right -= 1
            if height[right] > right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
    return water


# https://www.hellointerview.com/learn/code/two-pointers/sort-colors
def sort_colors(nums: list[int]) -> None:
    """
    >>> nums = [2, 1, 2, 0, 1, 0, 1, 0, 1]
    >>> sort_colors(nums)
    >>> nums
    [0, 0, 0, 1, 1, 1, 1, 2, 2]
    >>> nums = [1, 2, 0]
    >>> sort_colors(nums)
    >>> nums
    [0, 1, 2]
    """
    zero, two = 0, len(nums) - 1
    i = zero
    while i <= two:
        if nums[i] == 0:
            nums[zero], nums[i] = nums[i], nums[zero]
            zero += 1
            i += 1
        elif nums[i] == 1:
            i += 1
        else:  # nums[i] == 2
            nums[two], nums[i] = nums[i], nums[two]
            two -= 1


# https://www.hellointerview.com/learn/code/two-pointers/move-zeroes
def move_zeroes(nums: list[int]) -> None:
    """
    >>> nums = [2, 0, 4, 0, 9]
    >>> move_zeroes(nums)
    >>> nums
    [2, 4, 9, 0, 0]
    >>> nums = [0, 0, 0]
    >>> move_zeroes(nums)
    >>> nums
    [0, 0, 0]
    """
    slow = fast = 0
    while fast < len(nums):
        while fast < len(nums) and nums[fast] == 0:
            fast += 1
        if fast < len(nums):
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


# https://www.hellointerview.com/learn/code/two-pointers/valid-triangle-number
def triangle_number(nums: list[int]) -> int:
    """
    >>> triangle_number([11, 4, 9, 6, 15, 18])
    10
    """
    nums.sort(reverse=True)
    cnt = 0
    for i in range(len(nums) - 2):
        longest = nums[i]
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > longest:
                cnt += r - l
                l += 1
            else:
                r -= 1
    return cnt


# https://www.hellointerview.com/learn/code/two-pointers/3-sum
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    >>> three_sum([-1, 0, 1, 2, -1, -1])
    [[-1, -1, 2], [-1, 0, 1]]
    """
    nums.sort()
    res: list[list[int]] = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:  # sum == target
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
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
    l, r = 0, len(nums) - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum < target:
            l += 1
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
    l = r = max_area = 0
    while l < len(left) and r < len(right) and left[l] < right[r]:
        lh, rh = heights[left[l]], heights[right[r]]
        max_area = max(max_area, min(lh, rh) * (right[r] - left[l]))
        if lh < rh:
            l += 1
        else:
            r += 1
    return max_area
