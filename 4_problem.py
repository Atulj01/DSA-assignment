# Write a program to print the first non-repeated character from a string?


str = input('Enter a string: ')

index = -1
fun = ""
for i in str:
    if str.count(i) == 1:
        fun += i
        break
    else:
        index += 1
if index != 1:
    print("First non-repeating character is", fun)