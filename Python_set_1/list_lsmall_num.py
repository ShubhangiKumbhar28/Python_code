# 4. Write a Python program to get the smallest number from a list.
l = [43,67,89,-1,0,-14,78]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print("Smallest number from list {} is : {}".format(l,temp) )