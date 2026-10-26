class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for w in strs:
            dic = {}
            for l in w:
                dic[l]= dic.get(l,0)+1

            key = tuple(sorted(dic.items()))
            if key not in output:
                output[key]=[]
            output[key].append(w)
        return list(output.values())