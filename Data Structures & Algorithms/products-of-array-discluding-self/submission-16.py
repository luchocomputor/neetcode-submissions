class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = []
        left_pdt = [1]*n
        right_pdt = [1]*n
        for i in range (1,n):

            left_pdt[i]=left_pdt[i-1]*nums[i-1]
            right_pdt[n-i-1]=right_pdt[n-i]*nums[n-i]
            
        for i in range (n):
            out.append(left_pdt[i]*right_pdt[i])
        
        return out
