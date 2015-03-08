def windchill():
	while(1):
		flag = 0
		temp = raw_input("Enter Air temperature (in Fahrenheit): ")
		for c in temp:
			if c.isalpha() :
				flag = 1
		if flag == 1 :
			print "Not valid, please enter a valid number: "
		else:
			break
	temp = float(temp)
	while(1):
		flag = 0
		speed = raw_input("Enter Wind speed (in MPH): ")
		for c in speed:
			if c.isalpha() :
				flag = 1
		if flag == 1 :
			print "Not valid, please enter a valid number: "
		else:
			break
	speed = float(speed)
			
	wct_index =  35.74 + (0.6215 * temp) - (35.75 * (speed**0.16))  + (0.4275 * temp * (speed**0.16))
	print "Temperature (degrees F): %s" % (str(temp))
	print "Wind Speed (MPH): %s" % (str(speed))
	print "Wind Chill Temperature Index: %s" % (str(wct_index))	

windchill()
