class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # check for left half sorted
            elif nums[left] <= nums[mid]:
                # check if target lies in that sorted left range
                # if target is between nums[left] and nums[mid]:
                if nums[left] <= target < nums[mid]:
                    # shorten the left search space
                    right = mid - 1
                else:
                    # skip/eliminate the left
                    left = mid + 1
            # if not left then right is sorted
            else:
                # same check if target is in the right sorted range
                # if target is between nums[mid] and nums[right]:
                if nums[mid] < target <= nums[right]:
                    # shorted the right search space
                    left = mid + 1
                else:
                    # skip/eliminate the right
                    right = mid - 1

        # if not found
        return -1