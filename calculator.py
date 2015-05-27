# Pete Miller
# January, 10th, 2015
# Calculator

flag = True

numbers = [2, 3, 5, 7]

while flag:
	print " "
	print "Hello"
	math_type = raw_input("What type of math do you want to do, addition, subtraction, multiplication, dovision, exponents, square roots, to find if a number is prime or not, or quit? ")
	math_type = math_type.title()
	if math_type == "Addition":
		ad_1 = float(raw_input("What is the first number you would like to add?" ))
		ad_2 = float(raw_input("What is the second number you would like to add? "))
		print ad_1 + ad_2
	elif math_type == "Subtraction":
		sub_1 = float(raw_input("What is the first number you would like to sutract? "))
		sub_2 = float(raw_input("What is the second number you would like to sutract? "))
		print sub_1 - sub_2
	elif math_type == "Multiplication":
		mult_1 = float(raw_input("What is the first number you would like to multiply? "))
		mult_2 = float(raw_input("What is the second number you would like to multiply? "))
		print mult_1 * mult_2
	elif math_type == "Division":
		div_1 = float(raw_input("What is the first number you would like to add? "))
		div_2 = float(raw_input("What is the second number you would like to add? "))
		if div_2 == 0:
			print "You cannot divide by zero."
		else:
			print div_1 / div_2
	elif math_type == "Exponents":
		num = float(raw_input("What is teh base number you want?"))
		expo = float(raw_input("What exponent do you want?"))
		print num ** expo
	elif math_type == "Square Roots":
		num = float(raw_input("What number do you want to find the square root of?"))
		if num < 0:
			num = num * -1
			sqrt = num ** 0.5
			print "%si" % (sqrt)
		else:
			print num ** 0.5
	elif math_type == "Prime Or Not":
		prime_test_num = float(raw_input("What number would you like to test? "))
		for number in numbers:
			if prime_test_num % number == 0:
				print "The number is not prime."
				break
			elif prime_test_num % number != 0:
				print "The number is prime."
	elif math_type == "Quit":
		flag = False
	else:
		print "That is not a valid math type."