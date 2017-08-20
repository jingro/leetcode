class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            t = [j for j in i]
            t.sort()
            t = ''.join(t)
            if t not in d:
                d[t] = [i]
            else:
                d[t].append(i)
        res = []
        for i in d:
            res.append(d[i])
        return res
