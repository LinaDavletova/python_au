class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        n = 0
        l = [i for i in s]
        m = len(l)-1
        while n < m:
            if l[n] not in a and l[m] not in a:
                n += 1
                m -= 1
            elif l[n] not in a:
                n += 1
            elif l[m] not in a:
                m -= 1
            else:
                l[n], l[m] = l[m], l[n]
                n += 1
                m -= 1
        return "".join(l)
