class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(c for c in s.lower() if c.isalnum())
        n = len(s)
        i = 0
        while i < (n//2):
            if s[i]!=s[n-1-i]:
                return False
            i +=1
        
        return True
        