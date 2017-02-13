# Assigment: This code will have two parts, part 1 & 2. Part one involves
#retrieving the first and last name of each individual from a list. Part 
#Two involves retrieving the first and last names from two dictionaries
#and also giving a value equal to the length of each name

# PART ONE: 

# given the following list: 

# students = [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# create a program that outputs

# Michael Jordan 
# John Rodales 
# Mark Guillen 
# KB Tonel 

# ----------------------------------------------------------
#Part I Code

students = [
     {'first_name' : 'Michael',	'last_name' : 'Jordan'},
     {'first_name' : 'John',	'last_name' : 'Rosales'},
     {'first_name' : 'Mark',	'last_name' : 'Guillen'},
     {'first_name' : 'KB',		'last_name' : 'Tonel'}
]

for val in students:
	print val['first_name'], val['last_name']

#-----------------------------------------------------------
#Part II

users = {
 'Students': [ 
    {  'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {  'first_name' : 'John', 'last_name' : 'Rosales'},
    {  'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {  'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
    {'first_name' : 'Michael','last_name' : 'Choi'},
    { 'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, data in users.items():
	count = 0
 	for value in data: 
 		fullname= len(value["first_name"]) + len(value["last_name"])
 		count += 1
 		print count, "-" , value["first_name"].upper(), value["last_name"].upper(), fullname
 		

# I need to access one key at a time
# for key in users["Students"]:
#   print key 

























