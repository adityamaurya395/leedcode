class Solution(object):
    def romanToInt(self, s):
        r={'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,}
        ttl=pv=0
        for ch in reversed(s):
            cv=r[ch]
            if cv<pv:
                ttl-=cv
            else:
                ttl+=cv
            pv=cv
        return ttl            