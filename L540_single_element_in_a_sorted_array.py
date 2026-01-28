class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-2
        while start<=end:
            mid = (end+start)//2
            if nums[mid] == nums[mid^1]:
                start = mid+1
            else:
                end = mid-1
        return nums[start]