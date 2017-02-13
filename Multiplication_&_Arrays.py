# Assignment: Multiply

# Create a function called 'multiply' that reads each value in the 
# list (e.g. a = [2, 4, 10, 16]) and returns a list where each value
# has been multiplied by 5.The function should multiply each value 
# in the list by the second argument.



#function 'multiply' takes input a and creates an array, a, and 
#it then multiplies each element in the array by input b
a = input("enter array ")
b = input("enter value b ")

def multiply(a,b):
	for element in a:
 		a = element*b
 		print a

multiply([1,2,3,4,5],b)


#second way of doing this by creating a new array 

#def multiply(a,b):
#	new_Array=[]
# 	for element in a:
# 		a=element*b
# 		new_Array.append(a)
# 	print new_Array 

# multiply([2,4,10,6],5)

