class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        res = 0
        while i < len(s) and s[i].isdigit():
            res = (res * 10) + int(s[i])
            i += 1
            
        res *= sign
        
        if res < MIN_INT:
            return MIN_INT
        if res > MAX_INT:
            return MAX_INT
            
        return res
