class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            seen = {}
            for i in range (len(s)):
                seen[s[i]]= seen.get(s[i],0)+1
                seen[t[i]]= seen.get(t[i],0)-1

            for x in seen:
                if seen[x]!=0:
                    return False
            return True
        