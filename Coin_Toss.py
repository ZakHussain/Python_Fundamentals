# Assignment: Coin Tosses 

# simulates tossing a coin 5,000 times. It program
# should display how many times the head/tail appears. 
# Sample outpt should be like the following: 

def coinToss():
	head = 0
	tail = 0
	b = "... it's a head!... "
	c = "... it's a tail!... "
	attempt = 1

	for count in range(1,5001):
		import random
		random_num = random.random()
		x = round(random_num)		
		if x == 0:
			head += 1
			print("Attempt"+ str(attempt) +": Throwing a coin..."+ b +"Got "+
			str(head) +"(s) so far and "+ str(tail) +"(s) so far") 
		elif x== 1:
			tail += 1
			print("Attempt"+ str(attempt) +": Throwing a coin..."+ c +"Got "+
			str(head) +"(s) so far and "+ str(tail) +"(s) so far") 
		attempt += 1
		 
	if count == 5000:
	   	print("Ending the program, thank you!") 	

	print("heads =" +str(head)+ " times!")
	print("tails =" +str(tail)+ " times!")

coinToss()