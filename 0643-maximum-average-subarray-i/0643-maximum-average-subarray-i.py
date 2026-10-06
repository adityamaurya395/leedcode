class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr=sum(nums[:k])
        maxsum=curr
        for i in range(k,len(nums)):
            curr+=nums[i]-nums[i-k]
            if maxsum<curr:
                maxsum=curr
        return maxsum/k   