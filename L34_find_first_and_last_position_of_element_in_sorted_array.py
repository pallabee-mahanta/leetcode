from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # finds the leftmost (first) index to insert target
        left = bisect_left(nums, target)
        # finds the rightmost (last) index to insert target
        right = bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]