# weight
def weight():
	weight = float(input("enter the weight: "))
	unit = input("enter the unit (kg/lbs): ")
	
	if unit == "kg":
		conv_weight = weight * 2.205
		unit2 = "lbs"
		print(f"{round(weight)}{unit} is {round(conv_weight)}{unit2}.")
	elif unit == "lbs":
		conv_weight = weight / 2.205
		unit2 = "kgs"
		print(f"{round(weight)}{unit} is {round(conv_weight)}{unit2}.")
	else:
		print("invalid unit")
	
# temperature
def temp():
	temperature = float(input("enter the temperature: "))
	unit = input("enter the unit (C/F): ")
	unit = unit.lower()
	
	if unit == "c":
		conv_temp = round((temperature * 9) / 5 + 32)
		unit2 = "F"
		print(f"{round(temperature)}°{unit} is {conv_temp}{unit2}.")
	elif unit == "f":
		conv_temp = round((temperature - 32) * 5 / 9)
		unit2 = "C"
		print(f"{round(temperature)}{unit} is {conv_temp}°{unit2}.")
	else:
		print("invalid unit")
		
		
#temp()

# length
def length():
	leng = float(input("enter length: "))
	unit = input("enter unit (cm/m)")
	unit = unit.lower()
	
	if unit == "cm":
		conv_len = round(leng / 100, 3)
		unit2 = "m"
		print(f"{round(leng)}{unit} is equal to {conv_len}{unit2}.")
	elif unit == "m":
		conv_len = round(leng * 100, 3)
		unit2 = "cm"
		print(f"{round(leng)}{unit} is equal to {conv_len}{unit2}.")
	else:
		print("invalid unit")
		
# length()

# speed
def speed():
	spee = float(input("enter speed: "))
	unit = input("enter unit (km/s / m/s): ")
	unit = unit.lower()
	
	if unit == "km/s":
		conv_speed = round(spee * 1000, 3)
		unit2 = "m/s"
		print(f"{round(spee, 3)}{unit} is equal to {conv_speed}{unit2}.")
	elif unit == "m/s":
		conv_speed = round(spee / 1000, 3)
		unit2 = "km/s"
		print(f"{round(spee, 3)}{unit} is equal to {conv_speed}{unit2}.")
	else:
		print("invalid unit")
		
# speed()