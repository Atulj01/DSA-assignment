# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.



def rev(array):
    element = len(array)
    i = 0
    j = element - 1
    while i < j:
        lst =array[i]
        array[i] = array[j]
        array[j] = lst
        i += 1
        j -= 1

element = int(input("enter size of element :"))
array = []
for i in range(0,element):
    array.append(int(input("enter the values : ")))
rev(array)
print("reverse of array is : ",array)








# def reversearray(array,start,end):
#     if start >= end:
#         return
#     # array[start], array[end] = array[end], array[start]
#     # reversearray(array,start+1)


# element = int(input("enter the eliment size :"))
# array = []
# for i in range(1 , element+1 ):
#     lst2 = int(input("enter the value :"))
#     array.append(lst2)
# print("array :",array)

# print("Reversed array is")
# print(reversearray)

