# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        for i in s:
            if i not in ("0","1"):
                return False
        return True