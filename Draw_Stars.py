# Assignment: Stars

# Part 1 
# create a function called draw_stars() that takes a list of numbers and prints out *. 
# for example: 
# 	x = [ 4, 6, 1, 3, 5, 7, 25] will print:
# 		**** 
# 		****** 
# 		* 
# 		*** 
# 		***** 
# 		******* 
# 		*************************

#this function creates an array of n elements to generate n rows, of which, each contains 
#some number of starts equal to the value of the nth element

#def draw_stars(a):
# 	for element in a:			
#		print("*"*element)

#draw_stars([4,6,1,3,7,25])

#PART TWO:
# Modify the function above. Allow a list containing integers and strings 
#to be passed to the  draw_stars() function. When a string is passed, instead of 
# displaying *, display the first letter of the string according to the example below.
# You may use the .lower() string method for this part.

# For example:
#  x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x) should print the following in the terminal:

# **** 
# ttt 
# * 
# mmmmmmm 
# ***** 
# ******* 
# jjjjjjjjjjj


def draw_stars(x):
	for element in x:	
		if type(element) != str:
	 		print("*" * element)
	 	else:
	 		print((element[0] * len(element)).lower())	

draw_stars([4,"Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

