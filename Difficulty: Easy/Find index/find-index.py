#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())
for i in range(len(arr)):
    if arr[i]==x:
        print(i)
        break
