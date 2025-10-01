#User function Template for python3
#Back-end complete function Template for Python 3
n = int(input())

########### Write your code below ###############
fib=0
fib2=1
if n==0:
    fib=0
else:
    for i in range(n):
        fib,fib2=fib2,fib2+fib
########### Write your code above ###############
print(fib)
