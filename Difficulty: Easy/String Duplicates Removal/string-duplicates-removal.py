#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    s1=''
	    for i in s:
	        if i not in s1:
	            s1+=i
	    return s1