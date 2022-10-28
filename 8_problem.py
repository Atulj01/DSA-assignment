# Write a program to check if all the brackets are closed in a given code snippet.
# import os

# def isBalanced(s):
#     check = {")":"(" , "]":"[" , "}":"{" }
#     stack = []
#     for c in s:
#         if c in check.values():
#             stack.append(c)
#         elif stack and check[c] == stack[-1]:
#             stack.pop()
#         else:
#             return 'NO'
#     if stack == []:
#         return 'YES'
#     else:
#         return 'NO'

# if __name__== "__main__":
#     str = input("enter the string with brackets :")

#     t = int(input().strip())

#     for t_istr in range(t):
#         s = input()

#         result = isBalanced(s)

#         str.write(result + '\n')

#     str.close()


def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    expr = input("enter the expresion :")
 
    # Function call
    if areBracketsBalanced(expr):
        print("all bracket  are close in :")
    else:
        print("Not all bracket are close in :")
 

