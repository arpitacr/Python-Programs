# DNA Sequence Alignment Program
# Supports researchers to do DNA alignment by hand
import sys
def dna_seq():
# Block for prompting users to enter 2 valid DNA strings
	while(1):
		flag1 = 0
		flag2 = 0
		str1 = raw_input("Enter first string containing only A, T, C or G: ")
		str2 = raw_input("Enter second string containing only A, T, C or G: ")
		for ch in str1:
			if (ch != 'a' and ch!= 'A' and ch != 't' and ch!= 'T' and ch != 'c' and ch!= 'C' and ch != 'g' and ch!= 'G'):
				flag1 = 1
		for ch in str2:
			if (ch != 'a' and ch!= 'A' and ch != 't' and ch!= 'T' and ch != 'c' and ch!= 'C' and ch != 'g' and ch!= 'G'):
				flag2 = 1
		if flag1 == 1 or flag2 == 1 :
			print "Not valid, enter again"
		else:
			break
# Block for prompting users to enter a valid operation to perform
	while(1):
		while(1):
			choice = raw_input( "What do you want to do: \n a - add indel \n d - delete indel \n s - score \n q - quit \n")
			if (choice!= 'a' and choice!= 'd' and  choice!= 's' and choice!= 'q'):
				print "Not valid choice, please enter choice again"
			else:
				break
# Adding an indel
		if choice == 'a':
# Accepting valid string to operate upon
			while(1):
				strchoice = raw_input("Which string do you want to modify - str1 or str2 : ")
				if (strchoice != 'str1' and strchoice != 'str2'):
					print "Enter a valid option for string"
				else:
					break
			if strchoice == 'str1':
				strman = str1
			else:
				strman = str2
		#print len(strman)
# Prompting user to input valid index value
			while(1):
				ind = raw_input("Before which index: ")
				ind = int(ind)
				if(ind < 1 or ind > len(strman)):
					print "Not valid index, enter index again"
				else:
					break
				
# DNA manipulation
			if ind == 1:
				finalstr = '-' + strman
			else:
				finalstr = strman[:ind-1] + '-' + strman[ind-1:]
			if strman == str1:
				str1 = finalstr
			else:
				str2 = finalstr
# Deleting an indel			
		elif choice == 'd':
# Accepting valid string to operate upon
			while(1):
				strchoice = raw_input("Which string do you want to modify - str1 or str2: ")
				if (strchoice != 'str1' and strchoice != 'str2'):
					print "Enter a valid option for string "
				else:
					break
			if strchoice == 'str1':
				strman = str1
			else:
				strman = str2
# Prompting user to input valid index value
			while(1):
				ind = raw_input("At which index:")
				ind = int(ind)
				if(ind < 0 or ind > (len(strman) - 1) or strman[ind] != '-'):
					print "Not valid index, enter index of indel to be deleted again"
				else:
					break
# DNA Manipulation
			if ind == 0:
				finalstr = strman[:ind] + strman[ind+1:]
			elif ind == len(strman)-1:
				finalstr = strman[:ind]
			else:
				finalstr = strman[:ind] + strman[ind+1:]
			if strman == str1:
				str1 = finalstr
			else:
				str2 = finalstr
# Scoring
		elif choice == 's':
# Comparing lengths of 2 DNA strings and adding appropriate number of '-'s to shorter string
			len1 = len(str1)
			len2 = len(str2)
			if len1 < len2:
				str1 = str1 + ((len2 - len1) * '-')
			else:
				str2 = str2 + ((len1 - len2) * '-')
		
# Calculating matches and mismatches		
			length = len(str1)
			finalstr1 = ""
			finalstr2 = ""
			matches = 0
			mismatches = 0
			for item in range(0,length):
				if str1[item] == str2[item]:
					finalstr1 = finalstr1 + str1[item]
					finalstr2 = finalstr2 + str2[item]
					matches += 1
				else:
					mismatches += 1
					if str1[item] == '-':
						finalstr1 = finalstr1 + str1[item]
						finalstr2 = finalstr2 + str2[item].upper()
					elif str2[item] == '-':
						finalstr1 = finalstr1 + str1[item].upper()
						finalstr2 = finalstr2 + str2[item]
					else:
						finalstr1 = finalstr1 + str1[item].upper()
						finalstr2 = finalstr2 + str2[item].upper()
			print "Matches : ",matches
			print "Mismatches : ",mismatches
			print "String 1: %s" % (finalstr1)
			print "String 2: %s" % (finalstr2)
			
	
# Quit
		else:
			break
			sys.exit(0)
	
dna_seq()
	
	
		
		
		
	
	
	
	
