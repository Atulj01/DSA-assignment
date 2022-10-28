# Write a program to convert prefix expression to infix expression.
def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()
 
def isOperator(op):
    if op == "*" or op == "+" or op == "-" or op == "/" or op == "^" or op == "(" or op == ")":
        return True
    else:
        return False

if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print("convert to infix :",prefixToInfix(str))
     
