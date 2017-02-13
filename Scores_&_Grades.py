#Assignment: Scores and Grades

#Create a program that prompts the user ten times for a test score
#between 60 and 100. Each time a score is generated, your program
#should display what is the grad of that score
	# Score: 60 - 69; Grade - D
	# Score: 70 - 79; Grade - C
	# Score: 80 - 89; Grade - B
	# Score: 90 - 100; Grade - A
 
# first code
def myGrades():
	new_Array=[]
	for int in range(1,11):
		int = input('Enter test-score here ')
		new_Array.append(int)
	print new_Array		

 	print("Scores and Grades")
   	for element in new_Array:
   		if element >=90:
  			print("Score:" + str(element)+ " Your grade is a A")
   		elif element >= 80:
 			print("Score:" + str(element)+ " Your grade is a B")
   		elif element >= 70:
 			print("Score:" + str(element)+ " Your grade is a C")
  		elif element >= 60:
 		 	print("Score:" + str(element)+ " Your grade is a D")
  		elif element >= 25:
 		 	print("Score:" + str(element)+ " Your grade is an F")
 		elif element < 25:
 			print("Score:" + str(element)+ " I'm so sorry..but goddamn! you did bad.. ")	
 	print("End of Program")	 

myGrades()
