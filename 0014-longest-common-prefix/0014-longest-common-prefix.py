class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        p=strs[0]
        for s in strs[1:]:
            while not s.startswith(p):
                p=p[:-1]
                if not p:
                    return ""
        return p                