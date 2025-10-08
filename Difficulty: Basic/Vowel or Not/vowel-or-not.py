#User function Template for python3
class Solution:
    def isVowel (ob,c):
        # code here 
        main="aeiou"
        i=c.lower()
        if i in main:
            return "YES"
        else:
            return "NO"