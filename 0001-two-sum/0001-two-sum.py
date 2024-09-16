class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for num in range(len(nums)):
            if target - nums[num] not in hashMap:
                hashMap[nums[num]] = num
                continue
            firstIdx = hashMap[target - nums[num]]    
            hashMap[nums[num]] = num
            return [firstIdx, hashMap[nums[num]]]