gmail_num = 0
yahoo_num = 0
aol_num = 0
hotmail_num = 0
other = 0

emails = open(".\emailList.txt", "r")
output_email = open(".\output_email.py", "wb")
for email in emails:
	email = email.rstrip()
	email_parts = email.split("@")
	if email_parts[1] == "gmail.com":
		gmail_num += 1
	elif email_parts[1] == "yahoo.com":
		yahoo_num += 1
	elif email_parts[1] == "aol.com":
		aol_num += 1
	elif email_parts[1] == "hotmail.com":
		hotmail_num += 1
	else:
		other += 1

gmail_num = str(gmail_num)
yahoo_num = str(yahoo_num)
aol_num = str(aol_num)
hotmail_num = str(hotmail_num)
other = str(other)

output_email.write("There are " + gmail_num + " gmails" + "\n")
output_email.write("There are " + yahoo_num + " yahoos" + "\n")
output_email.write("There are " + aol_num + " aols " + "\n")
output_email.write("There are " + hotmail_num + " hotmails" + "\n")
output_email.write("There are " + other + " other emails")

emails.close()
output_email.close()
