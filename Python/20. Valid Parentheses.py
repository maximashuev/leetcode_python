"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        else:
            if len(stack) == 0:
                print("More left")
                return False
            last = stack.pop()
            if last == "(" and i != ")":
                return False
            if last == "[" and i != "]":
                return False
            if last == "{" and i != "}":
                return False
    if len(stack) > 0:
        print("False")
        return False
    else:
        print("Pass")
        return True


isValid("()")
