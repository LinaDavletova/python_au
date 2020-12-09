class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for i in s:
            if t.find(i) == -1:
                return False
            t = t.replace(str(i), '', 1)
        return True
