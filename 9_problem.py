# Write a program to reverse a stack.

class Stack:
 

    def __init__(self):
        self.Elements = []
         
    def push(self, value):
        self.Elements.append(value)
       
    def pop(self):
        return self.Elements.pop()
     
    def empty(self):
        return self.Elements == []
     
    def show(self):
        for value in reversed(self.Elements):
            print(value)

def BottomInsert(s, value):
   
    if s.empty():
         
        s.push(value)
         
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)

stk = Stack()
 
stk.push(int(input("enter the value :")))
stk.push(int(input("enter the value :")))
stk.push(int(input("enter the value :")))
stk.push(int(input("enter the value :")))
# stk.push(int(input("enter the value :")))
# stk.push(int(input("enter the value :"))

 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()