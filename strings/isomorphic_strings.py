class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_st = {}
        map_ts = {}
        
        for ch1, ch2 in zip(s, t):
            if ch1 in map_st and map_st[ch1] != ch2:
                return False
            if ch2 in map_ts and map_ts[ch2] != ch1:
                return False
            map_st[ch1] = ch2
            map_ts[ch2] = ch1
        
        return True
