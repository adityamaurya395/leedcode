class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[dt]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for indx ,val in enumerate(nums):
            diff=target-val
            if diff in hashmap:
                return [hashmap[diff],indx]
            else:
                hashmap[val]=indx    
                           


        
        