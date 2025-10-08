class Solution:
    def greatestOfThree(self, a, b, c):
        #code here
        if a>b and a>c:
            return a
        elif b>c:
            return b
        else:
            return c