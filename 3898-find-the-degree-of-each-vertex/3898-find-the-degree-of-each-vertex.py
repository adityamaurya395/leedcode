class Solution(object):
    def findDegrees(self, matrix):
       return [sum(row) for row in matrix]
        