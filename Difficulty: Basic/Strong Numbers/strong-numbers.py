#User function Template for python3

class Solution:
    def isStrong(self, N):
        # code here 
        M=N
        res=0
        while N>0:
            dig=N%10
            res+=self.fact(dig)
            N=N//10
        if res==M:
            return 1
        else:
            return 0
    def fact(self,dig):
        if dig==0:
            return 1
        else:
            sum=1
            for i in range(1,dig+1):
                sum*=i
            return sum