class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s2 = ""
        t = ""
        for i in s:
            if i != " ":
                t = i + t
            else:
                s2 = s2 + t + " "
                t = ""
        s2 = s2 + t
        return s2
