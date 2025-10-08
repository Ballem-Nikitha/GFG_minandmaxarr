class Solution:
    def sumOfDigits(self, n):
        # code here
        sum=0
        for i in str(n):
            sum+=int(i)
        return sum