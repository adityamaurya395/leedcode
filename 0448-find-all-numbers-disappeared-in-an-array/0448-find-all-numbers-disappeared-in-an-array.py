class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[]
        hashtable=[0]*(n+1)
        for i in nums:
            hashtable[i]=1
        for i in range(1,n+1):
            if hashtable[i]==0:
                result.append(i)
        return result            
