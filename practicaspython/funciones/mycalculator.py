"""In this program I will calculate mathematical operation with two numbers callig
	opMat module"""

#Importing the opMath module are in the same directory
import opMath

#Requesting the numbers
nA = int(input("Input the number A: "))
nB = int(input("Input the number B: "))

#Calling each function inside opMath module, and  we pass arguments. Then we print it results.
print(opMath.add(nA, nB))
print(opMath.sub(nA, nB))
print(opMath.multi(nA, nB))
print(opMath.div(nA, nB))