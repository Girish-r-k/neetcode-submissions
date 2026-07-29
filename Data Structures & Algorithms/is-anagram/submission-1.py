class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        has={}
        ma={}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in has:
                has[i]=1
            else:
                val=has.get(i,0)+1
                has[i]=val
        for i in t:
            if i not in ma:
                ma[i]=1
            else:
                val=ma.get(i,0)+1
                ma[i]=val
        
        for k in ma:
            if has.get(k)!=ma.get(k):
                return False
        
        return True
        