from typing import Optional

from _common import ListNode

# +++ Linked List
# https://www.hellointerview.com/learn/code/linked-list/overview


# https://www.hellointerview.com/learn/code/linked-list/palindrome-linked-list
def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    >>> is_palindrome(ListNode.from_list([1, 2, 3, 1]))
    False
    """
    if not head:
        return True
    # step 1: find middle
    slow = fast = head
    while fast and fast.next:
        assert slow.next
        slow = slow.next
        fast = fast.next.next
    # step 2: reverse second half
    prev = slow
    next = slow.next
    cnt = 1
    while next:
        tmp = next.next
        next.next = prev
        prev = next
        next = tmp
        cnt += 1
    # step 3: cmp left and right
    left, right = head, prev
    while left and right and cnt > 0:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
        cnt -= 1
    return True


# https://www.hellointerview.com/learn/code/linked-list/linked-list-cycle
def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        assert slow.next
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# ---

# +++ Stack
# https://www.hellointerview.com/learn/code/stack/overview


# https://www.hellointerview.com/learn/code/stack/largest-rectangle-in-histogram
def largest_rectangle_area(heights: list[int]) -> int:
    """
    >>> largest_rectangle_area([2, 8, 5, 6, 2, 3])
    15
    """
    stack: list[int] = []
    left: list[int] = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left.append(stack[-1] + 1 if stack else 0)
        stack.append(i)
    stack.clear()
    right: list[int] = []
    for i in range(len(heights) - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right.append(stack[-1] - 1 if stack else len(heights) - 1)
        stack.append(i)
    right.reverse()
    max_area = 0
    for l, r, h in zip(left, right, heights):
        max_area = max(max_area, (r - l + 1) * h)
    return max_area


# https://www.hellointerview.com/learn/code/stack/daily-temperatures
def daily_temperatures(temps: list[int]) -> list[int]:
    """
    >>> daily_temperatures([65, 70, 68, 60, 55, 75, 80, 74])
    [1, 4, 3, 2, 1, 1, 0, 0]
    """
    stack: list[int] = []
    res: list[int] = [0] * len(temps)
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


# https://www.hellointerview.com/learn/code/stack/longest-valid-parentheses
def longest_valid_parentheses(s: str) -> int:
    """
    >>> longest_valid_parentheses("())))")
    2
    >>> longest_valid_parentheses("((()()())")
    8
    >>> longest_valid_parentheses("")
    0
    """
    stack = [-1]
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len


# https://www.hellointerview.com/learn/code/stack/decode-string
def decode_string(s: str) -> str:
    """
    >>> decode_string("3[a]2[bc]")
    'aaabcbc'
    >>> decode_string("3[a2[c]]")
    'accaccacc'
    >>> decode_string("2[abc]3[cd]ef")
    'abcabccdcdcdef'
    """
    cnt: list[int] = []
    dec: list[str] = []
    i = 0
    res = ""
    while i < len(s):
        if s[i].isdigit():
            c = int(s[i])
            while s[i + 1].isdigit():
                c = 10 * c + int(s[i + 1])
                i += 1
            cnt.append(c)
        elif s[i] == "[":
            dec.append("")
        elif s[i] == "]":
            d = dec.pop()
            c = cnt.pop()
            if dec:
                dec[-1] += c * d
            else:
                res += c * d
        else:  # char
            if dec:
                dec[-1] += s[i]
            else:
                res += s[i]
        i += 1
    return res


# https://www.hellointerview.com/learn/code/stack/valid-parentheses
def is_valid(s: str) -> bool:
    """
    >>> is_valid("(){({})}")
    True
    >>> is_valid("(){({}})")
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


# ---

# +++ Intervals
# https://www.hellointerview.com/learn/code/intervals/overview


# https://www.hellointerview.com/learn/code/intervals/employee-free-time
def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    """
    >>> employee_free_time([[[2, 4], [7, 10]], [[1, 5]], [[6, 9]]])
    [[5, 6]]
    """
    intervals = [i for s in schedule for i in s]
    if not intervals:
        return []
    merged: list[list[int]] = []
    intervals.sort()
    istart, iend = intervals[0]
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if iend < start:
            merged.append([istart, iend])
            istart, iend = start, end
        else:
            iend = max(iend, end)
    merged.append([istart, iend])
    free: list[list[int]] = []
    for i in range(len(merged) - 1):
        free.append([merged[i][1], merged[i + 1][0]])
    return free


# https://www.hellointerview.com/learn/code/intervals/merge-intervals
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    >>> merge_intervals([[3, 5], [1, 4], [7, 9], [6, 8]])
    [[1, 5], [6, 9]]
    """
    if not intervals:
        return []
    merged: list[list[int]] = []
    intervals.sort()
    istart, iend = intervals[0]
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if iend < start:
            merged.append([istart, iend])
            istart, iend = start, end
        else:
            iend = max(iend, end)
    merged.append([istart, iend])
    return merged


# https://www.hellointerview.com/learn/code/intervals/non-overlapping-intervals
def non_overlapping_intervals(intervals: list[list[int]]) -> int:
    """
    >>> non_overlapping_intervals([[1, 3], [5, 8], [4, 10], [11, 13]])
    1
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda ivl: ivl[1])
    iend = intervals[0][1]
    cnt = 1
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if iend <= start:
            cnt += 1
            iend = end
    return len(intervals) - cnt


# https://www.hellointerview.com/learn/code/intervals/insert-interval
def insert_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    """
    >>> insert_interval([[1, 3], [6, 9]], [2, 5])
    [[1, 5], [6, 9]]
    >>> insert_interval([[1, 2], [3, 5], [6, 7], [8, 10]], [5, 6])
    [[1, 2], [3, 7], [8, 10]]
    >>> insert_interval([], [5, 7])
    [[5, 7]]
    """
    updated: list[list[int]] = []
    i = 0
    while i < len(intervals):
        start, end = intervals[i]
        new_start, _ = new_interval
        if end >= new_start:
            new_interval[0] = min(new_start, start)
            break
        updated.append([start, end])
        i += 1
    while i < len(intervals):
        start, end = intervals[i]
        _, new_end = new_interval
        if new_end < start:
            break
        new_interval[1] = max(new_end, end)
        i += 1
    updated.append(new_interval)
    updated += intervals[i:]
    return updated


# https://www.hellointerview.com/learn/code/intervals/can-attend-meetings
def can_attend_meetings(intervals: list[list[int]]) -> bool:
    """
    >>> can_attend_meetings([[1, 5], [3, 9], [6, 8]])
    False
    >>> can_attend_meetings( [[10, 12], [6, 9], [13, 15]])
    True
    """
    intervals.sort()
    ptr = 0
    for start, end in intervals:
        if ptr > start:
            return False
        ptr = max(ptr, end)
    return True


# ---

# +++ Variable Length Sliding Window
# https://www.hellointerview.com/learn/code/sliding-window/variable-length


# https://www.hellointerview.com/learn/code/sliding-window/longest-repeating-character-replacement
def char_replacement(s: str, k: int) -> int:
    """
    >>> char_replacement("BBABCCDD", 2)
    5
    """
    counter: dict[str, int] = dict()
    start = end = max_length = 0
    while end < len(s):
        if s[end] not in counter:
            counter[s[end]] = 0
        counter[s[end]] += 1
        while max(counter.values()) + k < end - start + 1:
            counter[s[start]] -= 1
            if counter[s[start]] == 0:
                del counter[s[start]]
            start += 1
        max_length = max(max_length, end - start + 1)
        end += 1
    return max_length


# https://www.hellointerview.com/learn/code/sliding-window/longest-substring-without-repeating-characters
def longest_substr_without_repeat(s: str) -> int:
    """
    >>> longest_substr_without_repeat("eghghhgg")
    3
    >>> longest_substr_without_repeat("substring")
    8
    """
    index: dict[str, int] = dict()
    start = end = max_length = 0
    while end < len(s):
        if s[end] in index:
            start = max(start, index[s[end]] + 1)
        max_length = max(max_length, end - start + 1)
        index[s[end]] = end
        end += 1
    return max_length


# ---

# +++ Fixed Length Sliding Window
# https://www.hellointerview.com/learn/code/sliding-window/fixed-length


# https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-distinct-subarrays-with-length-k
def max_unique_sum(nums: list[int], k: int) -> int:
    """
    >>> max_unique_sum([3, 2, 2, 3, 4, 6, 7, 7, -1], 4)
    20
    >>> max_unique_sum([5, 5, 5, 5, 5], 3)
    0
    """
    counter: dict[int, int] = dict()
    sum = 0
    for i in range(k):
        if nums[i] not in counter:
            counter[nums[i]] = 0
        counter[nums[i]] += 1
        sum += nums[i]
    max_sum = 0
    if len(counter) == k:
        max_sum = sum
    for i in range(k, len(nums)):
        rm = nums[i - k]
        counter[rm] -= 1
        if counter[rm] == 0:
            del counter[rm]
        sum -= rm
        add = nums[i]
        if add not in counter:
            counter[add] = 0
        counter[add] += 1
        sum += add
        if len(counter) == k:
            max_sum = max(max_sum, sum) if max_sum != 0 else sum
    return max_sum


# https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-subarrays-of-size-k
def max_sum(nums: list[int], k: int) -> int:
    """
    >>> max_sum([2, 1, 5, 1, 3, 2], 3)
    9
    """
    s = sum(nums[:k])
    m = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        m = max(m, s)
    return m


# https://www.hellointerview.com/learn/code/sliding-window/maximum-points-you-can-obtain-from-cards
def max_score(cards: list[int], k: int) -> int:
    """
    >>> max_score([2, 11, 4, 5, 3, 9, 2], 3)
    17
    >>> max_score([1, 100, 10, 0, 4, 5, 6], 3)
    111
    """
    n = len(cards) - k
    s = sum(cards[:n])
    m = s
    for i in range(n, len(cards)):
        s += cards[i] - cards[i - n]
        m = min(m, s)
    return sum(cards) - m


# ---

# +++ Two Pointers
# https://www.hellointerview.com/learn/code/two-pointers/overview


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


# ---
