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


def data():
	data = input("enter data: ")
	unit = input("enter unit (GB/MB): ")
	unit = unit.lower()
	
	if unit == "gb":
		conv_data = round(float(data) * 1024, 3)
		unit2 = "MB"
		print(f"{data}{unit} is equal to {conv_data}{unit2}.")
	elif unit == "mb":
		conv_data = round(float(data) / 1024, 3)
		unit2 = "GB"
		print(f"{data}{unit} is equal to {conv_data}{unit2}.")
	else:
		print("invalid unit")

def volume():
	vol = float(input("enter volume: "))
	unit = input("enter unit (ml/l): ")
	unit = unit.lower()
	
	if unit == "ml":
		conv_vol = round(vol / 1000, 3)
		unit2 = "l"
		print(f"{vol}{unit} is equal to {conv_vol}{unit2}.")
	elif unit == "l":
		conv_vol = round(vol * 1000, 3)
		unit2 = "ml"
		print(f"{vol}{unit} is equal to {conv_vol}{unit2}.")
	else:
		print("invalid unit")

def area():
	area = float(input("enter area: "))
	unit = input("enter unit (cm2/m2): ")
	unit = unit.lower()
	
	if unit == "cm2":
		conv_area = round(area / 10000, 3)
		unit2 = "m2"
		print(f"{area}{unit} is equal to {conv_area}{unit2}.")
	elif unit == "m2":
		conv_area = round(area * 10000, 3)
		unit2 = "cm2"
		print(f"{area}{unit} is equal to {conv_area}{unit2}.")
	else:
		print("invalid unit")

def time():
	time = float(input("enter time: "))
	unit = input("enter unit (min/hr): ")
	unit = unit.lower()
	
	if unit == "min":
		conv_time = round(time / 60, 3)
		unit2 = "hr"
		print(f"{time}{unit} is equal to {conv_time}{unit2}.")
	elif unit == "hr":
		conv_time = round(time * 60, 3)
		unit2 = "min"
		print(f"{time}{unit} is equal to {conv_time}{unit2}.")
	else:
		print("invalid unit")

def tip():
	bill = float(input("enter bill amount: "))
	tip = float(input("enter tip percentage: "))
	
	tip_amount = round(bill * tip / 100, 2)
	total = round(bill + tip_amount, 2)
	
	print(f"tip amount: {tip_amount}")
	print(f"total amount: {total}")

# data()
# volume()
# area()
# time()
# tip()