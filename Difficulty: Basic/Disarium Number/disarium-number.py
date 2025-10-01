#User function Template for python3

class Solution:
    def isDisarium(self, N):
        # code here
        M=N
        sum=0
        N_str = str(N)
        for i in range(len(N_str)):
            sum+=int(N_str[i])**(i+1)
        if sum==M:
            return 1
        else:
            return 0
            
            