class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        hsh = {}

        for str in strs:
            k = "".join(sorted(str))
            if k in hsh:
                hsh[k].append(str) 
            else:
                hsh[k] = [str]
        
        return list(hsh.values())