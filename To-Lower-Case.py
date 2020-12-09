class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return str
        t = ''
        for i in s:
            if ord(i) > 64 and ord(i) < 91:
                t += chr(ord(i) + 32)
            else:
                t += i
        return t
