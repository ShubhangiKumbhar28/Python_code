
"""6. Write a Python program to get a list, "sorted in increasing order by the last element in each tuple" from a given list of non-empty tuples. 
	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] """

l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

l = []
for i in l1:
    l.append(list(i))
print(l)

sorted_tup = tuple(sorted(l, key=lambda x:x[1]))
print("sorted in increasing order by the last element in each tuple is :",sorted_tup)

# 2nd way is to sort data by using Bubble sort algorithm

l2 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

n = len(l2)

# Bubble Sort
for i in range(n):
    for j in range(0, n-i-1):
        # Compare the last element of each tuple
        if l2[j][-1] > l2[j+1][-1]:
            l2[j], l2[j+1] = l2[j+1], l2[j] 

print(l2)
