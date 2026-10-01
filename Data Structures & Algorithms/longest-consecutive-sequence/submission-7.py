class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ct = {}
        
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1

        max_len = 1
        i=1

        for x in nums:
            if x in ct: 
                ct[x]+=1
            else:
                ct[x]=1
            
        ct = sorted(ct)
        print(ct)

        streak = 1
        while i<len(ct):
            if abs(ct[i]-ct[i-1])==1:
                streak +=1
            else:
                streak = 1
            max_len = max(max_len,streak)
            i+=1
        
        return max_len



        