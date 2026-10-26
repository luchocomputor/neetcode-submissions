class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            dic[x]= dic.get(x,0)+1
        dic = sorted(dic.items(), key=lambda kv: kv[1])
        return list(x[0] for x in dic[-k:])