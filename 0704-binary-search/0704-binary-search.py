class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while (left <= right):
            midpoint = (left + right) / 2
            midpoint = int(midpoint)
            if target < nums[midpoint]:
                right = midpoint
            elif target > nums[midpoint]:
                left = midpoint + 1
            elif target == nums[midpoint]:
                return midpoint
            if left == right:
                midpoint = (left + right) / 2
                midpoint = int(midpoint)
                if nums[midpoint] == target:
                    return left
                return -1
        return -1