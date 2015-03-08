# 196-algorithm based Palindrome Generator

#The 196-algorithm is a procedure for creating a palindromic integer: an integer that has the same value when examined forwards or backwards.
#The 196-algorithm is as follows:
#		1. If the integers is a palindrome, then print that integer
#		2. Otherwise, take the integer and its reversal and add them together.
#		3. With the sum, repeat the process starting at step 1.
#It is called the 196-algorithm because the integer 196 is the first number that, it appears, does not converge to a palindromic number.
#Such a number is called a Lychrel number.

#This programs takes a range from the user and reports Natural palindromes, lychrel numbers and non-lychrel numbers within that range

def palindrome_196():
# Prompts user to input starting of the range to check	
	while(1):
		start = raw_input("Enter starting of the range of numbers to check: ")
		if not start.isdigit():
			print "not valid, please enter again"
		else:
			break
# Prompts user to input ending of the range to check				
	while(1):
		stop = raw_input("Enter ending of the range of numbers to check: ")
		if not stop.isdigit():
			print "not valid, please enter again"
		else:
			break
	nat_pal = 0
	non_lych = 0
	lych = 0
	
	for item in range( int(start),int(stop)+1):
# checking for natural palindromes
		newitem = str(item)
		if newitem == newitem[::-1]:
			nat_pal += 1
		else:
			count = 0
			item1 = newitem
			while(count<60):
				total = int(item1) + int(item1[::-1])
				count += 1
				item1s = str(total)
				item1 = item1s
# checking for non lychrel numbers
				if item1s == item1s[::-1]:
					non_lych += 1
					break
			else:
# checking for lychrel numbers and printing them
				lych += 1
				print newitem + " is a Lychrel number"
	
# printing total count of natural palindromes, non-lychrel numbers and lychrel numbers
	print "The total number of natural palindromes are " + str(nat_pal)
	print "The total number of non Lychrel numbers are " + str(non_lych)
	print "The total number of Lychrel numbers are " + str(lych)
	
palindrome_196()
	
			
				
					
				
		
	
