class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array=[]
        inital=0

        for j in range(len(nums)):
            for i in range(j+1,len(nums)):
                if nums[j]+nums[i]==target:
                    return j,i
