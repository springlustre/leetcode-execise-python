def groupAnagrams(strs):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        maps = {}
        res = []
        for s in strs:
                l = list(s)
                l.sort()
                temp = "".join(l)
                if temp in maps:
                        maps[temp].append(s)
                else:
                        maps[temp] = [s]
        for (k,v) in maps.items():
                res.append(v)
        return res
                

a = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)
    
