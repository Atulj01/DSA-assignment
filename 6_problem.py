# Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.


def isOperator(op):
 
    if op == "+":
        return True
    if op == "-":
        return True
    if op == "/":
        return True
    if op == "*":
        return True
    return False
 
# Convert postfix to Prefix expression
  
def postToPre(post_exp):
    lst = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = lst[-1]
            lst.pop()
            op2 = lst[-1]
            lst.pop()
            temp = post_exp[i] + op2 + op1
            lst.append(temp)
        else:
            lst.append(post_exp[i])   
    ans = ""
    for i in lst:
        ans += i
    return ans
if __name__ == "__main__":
 
    post_exp = input("enter the post expresion :")
    print(post_exp)

     
    print("Prefix : ", postToPre(post_exp))
 