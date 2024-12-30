class Solution(object):
    def repeatedCharacter(self, s):
        seenArr = []
        for c in s:
            if c in seenArr:
                return c
            else:
                seenArr.append(c)