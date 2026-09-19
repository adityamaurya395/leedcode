class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(h)-1
        mw=0
        while l<r:
            wid=r-l
            ch=min(h[l],h[r])
            cw=wid*ch
            mw=max(mw,cw)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return mw          