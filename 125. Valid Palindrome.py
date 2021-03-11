"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
#solution 1
def isPalindrome( s: str) -> bool:
    k=''.join(filter(str.isalnum,s.lower()))
    print(k)
    print(''.join(reversed(k))==k,"\n")
    return ''.join(reversed(''.join(filter(str.isalnum,s.lower())))) == ''.join(filter(str.isalnum, s.lower()))
    return ''.join(reversed(k))==k

#solution 2

def isPalindrome( s: str) -> bool:
    k = ''.join(filter(str.isalnum, s.lower()))
    print(k)
    left,right=0,len(k)-1
    while left<right:
        if k[left]!=k[right]:
            return False
        left+=1
        right-=1
    print("True")
    return True


isPalindrome("A man, a plan, a canal: Panama")