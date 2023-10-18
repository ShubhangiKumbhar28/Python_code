# 2. Write a Python program to multiply all the items in a list.
l = [23,12.3,45,67,23.89,12.45]
mul = 1
for i in l:
    mul*=i
    i+=1

print("Multiplication of list elements : ",mul)