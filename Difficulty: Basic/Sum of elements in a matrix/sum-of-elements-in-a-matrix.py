#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        #code here
        sum1=0
        for i in range(N):
            sum1+=sum(Grid[i])
        return sum1