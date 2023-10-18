# 3. Write a Python program to get the largest number from a list. 
l = [12,678,987.6,566,90,1,2,45]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] >= l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print("sorted list : ",l)
print(l[-1])




