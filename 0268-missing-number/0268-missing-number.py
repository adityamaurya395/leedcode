class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        s=0
        for i in range(n+1):
            s+=i
        return s-sum(nums)    

        