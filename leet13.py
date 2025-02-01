class Solution:
  

    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            curr = self.valu(i,s)
            next = self.valu(i + 1,s)
            if curr >= next:
                res += curr
            else:
                res -= curr
        res += self.valu(len(s) - 1,s)
        return(res)
        
    def valu(self,i,s):
        if s[i] == "M":
            return 1000
        elif s[i] == "X":
            return 10
        elif s[i] == "L":
            return 50
        elif s[i] == "I":
            return 1
        elif s[i] == "V":
            return 5
        elif s[i] == "C":
            return 100
        elif s[i] == "D":
            return 500