n1 = int(input("Enter firet Number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

if n1>n2 and n1>n3:
	print("Buggest number is : ", n1)
elif n2>n3:
	print("Biggest number is : ", n2)
else:
	print("Biggest number is : ", n3)
