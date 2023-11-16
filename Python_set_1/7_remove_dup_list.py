## 7. Write a Python program to remove duplicates from a list. 

## 1st
# l = ['shu','shu', 7, 7, 7,23, 28,28]
# l = set(l)

## 2nd

l = ['shu','shu', 7, 7, 7,23, 28,28]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)

