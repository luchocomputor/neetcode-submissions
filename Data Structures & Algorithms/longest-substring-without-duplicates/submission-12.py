class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ct = {}
        left = 0
        max_len = 0

        for right,x in enumerate(s):
            if x not in ct:
                ct[x]=right
            else:
                left = max(left,ct[x]+1)
                ct[x]=right

            max_len = max(max_len,right-left+1)
        return max_len
        