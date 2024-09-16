class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for i in range(len(s)):
            sDict[s[i]] += 1
            tDict[t[i]] += 1
        for c in sDict:
            if sDict[c] != tDict[c]:
                return False
        return True