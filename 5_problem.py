#  Read about the Tower of Hanoi algorithm. Write a program to implement it.


def towerofhanoi(n,class_A,class_B,class_C):
    if n == 0:
        return
    towerofhanoi(n-1,class_A,class_B,class_C)
    print("move student no ", n, "from class ",class_A,"to class ", class_B)
    towerofhanoi(n-1,class_C , class_B , class_A)

N = int(input("enter the number of student to move :"))

towerofhanoi(N,'A','B','C')


