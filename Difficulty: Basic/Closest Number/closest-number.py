class Solution:
    def closestNumber(self, n, m):
        # code here 
        if (n%m==0):
            return n
        small=(n//m)*m
        
        # closest greater divisible by m
        great=((n//m)+1)*m
             
         #choose the one near to n
        if abs(n-small) < abs(great-n):
            return small
        elif abs(n-small) > abs(great-n):
            return great
        else:
            return great if abs(great) > abs(small) else small