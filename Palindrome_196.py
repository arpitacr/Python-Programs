def palindrome_196():
	while(1):
		start = raw_input("Enter starting of the range of numbers to check: ")
		if not start.isdigit():
			print "not valid, please enter again"
		else:
			break
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
				if item1s == item1s[::-1]:
					non_lych += 1
					break
			else:
				lych += 1
				print newitem + " is a Lychrel number"
	
	print "The total number of natural palindromes are " + str(nat_pal)
	print "The total number of non Lychrel numbers are " + str(non_lych)
	print "The total number of Lychrel numbers are " + str(lych)
	
palindrome_196()
	
			
				
					
				
		
	
