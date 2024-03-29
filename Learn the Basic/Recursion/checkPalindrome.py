string="abbba"
def checkPalindrome(i,n):
    if i>=n//2:
        return "true"
    if string[i]!=string[n-i]:
        return "false"
    return checkPalindrome(i+1,n)
    
n=len(string)
print(checkPalindrome(0,n-1))
