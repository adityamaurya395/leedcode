class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        li=[]
        for i in range(1,len(nums)+1):
            li.append(i)
        return list(set(li)-set(nums))
