
#in this code I will write my first function to calculate
#the larger of two numbers given.

def largNum( numA, numB):
	'''
	This function calculate the larger of two numbers given. It receives two
	parameters like arguments numA and numB '''

	if numA > numB:
		print("The number A is larger than B")
	elif numA < numB:
		print("The number B is larger than A")
	else:
		print("The numbers are equals")
	
		
#Requesting the numbers
nA = int(input("Input the number A: "))
nB = int(input("Input the number B: "))

#Showing the input numbers, see that i need to cast int number to string
#print("Numbers are nA: " + str(nA) + " nB: " + str(nB))

#Calling the largNum function
largNum(nA, nB)
 