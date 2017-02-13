#Assignment: Odd/Even
#create a function that counts from 1 to 2000. 
#as it loops through each number, have your program generate
#the number and specify whether it's an odd or even number 

# Code 1, determines even and odds and prints if the num is even or odd
# for num in range(1, 2001):
# 	print "Number is", num
#  	if num % 2 == 0:
#  		print " This is an even number."
#  	else:
#  		print " This is an odd number." 

#Code 2, determines even and odds, then prints out concatenated sentence
for num in range(1,2001):
 	if num % 2 == 0:
 		print("Number is "+ str(num) +" this is an even number")
 	else:
 		print("Number is " + str(num) + " This is an odd number.")

