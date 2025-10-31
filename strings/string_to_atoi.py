class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        i=0
        if s[0] in ['-','+']:
            if s[0] in ['-']:
                sign = -1
            i+=1
        num =0
        while i<len(s) and s[i].isdigit():
            num = num*10+int(s[i])
            i = i+1
        
        num = sign*num

        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if num<INT_MIN:
            return INT_MIN
        if num>INT_MAX:
            return INT_MAX
        return num
