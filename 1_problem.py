# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

from array import array


element = int(input("enter the eliment size :"))
array = []
for i in range(1 , element +1 ):
    lst2 = int(input("enter the value :"))
    array.append(lst2)
print("array :",array)

summ = int(input("enter the sum value :"))
print("Pairs whose sum is :", summ)

for i in range(len(array)-1):
    for j in range(i + 1,len(array)):
        if (array[i] + array[j]) == summ:
            print(array[i] , array[j])
