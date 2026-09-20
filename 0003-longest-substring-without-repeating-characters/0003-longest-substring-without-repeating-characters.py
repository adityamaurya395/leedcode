class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        maxl=0
        for r in range(len(s)):
            while s[r] in s[l:r]:
                l+=1
            maxl=max(maxl,r-l+1)    

        return maxl