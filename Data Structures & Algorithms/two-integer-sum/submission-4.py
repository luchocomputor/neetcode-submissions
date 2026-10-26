class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}
        for i,x in enumerate(nums):
            if x not in nums_d:
                nums_d[x]=[]
            nums_d[x].append(i)
            obj = target-x
            if obj in nums_d:
                if obj==x:
                    if len(nums_d[x])>1:
                        return[nums_d[x][0],nums_d[x][1]]
                else:
                    return[nums_d[obj][0],nums_d[x][0]]
        