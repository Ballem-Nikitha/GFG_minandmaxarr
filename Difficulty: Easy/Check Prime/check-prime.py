#User function Template for python3
n = int(input())

# Your code here
if n<=1:
    print(False)
else:
    for i in range(2,n):
        if n%i==0:
            print(False)
            break
    else:
        print(True)
