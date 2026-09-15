class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        Count_s,Count_t = {},{}
        for i in s:
            Count_s[i] = 1 + Count_s.get(i, 0)
        for i in t:
            Count_t[i] = 1 + Count_t.get(i, 0)
        for c in Count_s:
            if Count_s[c] != Count_t.get(c,0):
                return False
        return True

            
            
       
        