class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        total_numbers = 1 << n  
        return [i ^ (i >> 1) for i in xrange(total_numbers)]
        