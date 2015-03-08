def richter_energy():
	while(1):
		flag = 0
		inp = raw_input("Enter a number between 1 and 10: ")
		for c in inp:
			if c.isalpha() :
				flag = 1
		if flag == 1 :
			print "Not valid, please enter a number between 1 and 10: "
		elif ( float(inp) < 1.0 or float(inp) > 10.0 ):
			print "Number not in Richter scale, please enter again: "
		else:
			break
	
	richter = float(inp)
	energy = 10 ** ((1.5 * richter) + 4.8)
	tons_of_tnt = energy/(4.184 * (10 ** 9))
	print "The earthquake of " + str(richter) + " on Richter scale released energy of " + str(energy) + " Joules which is worth exploding " + str(tons_of_tnt) + " tons of TNT"
		
richter_energy()
