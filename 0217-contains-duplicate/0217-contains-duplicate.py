class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set1=set(nums)
        if len(set1)==len(nums):
            return False
        else:
            return True