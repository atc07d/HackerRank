#! /usr/bin/python3 
# A function that uses regular expressions to make sure the password 
# string is strong:
#	at least 8 char long, contains upper and lower case,
#	has at least one digit
import re

def checkPassword(password):
	passwordRegex = re.compile(r'[0-9]*[a-zA-Z0-9]{7,}[0-9]*')
	pmo = passwordRegex.findall(password)
	print(pmo)

tempPwd = 'RunningMan1989'
tempPwd1 = 'fail'
tempPwd2 = 'justalltextyeahplz'
checkPassword(tempPwd)
checkPassword(tempPwd1)
checkPassword(tempPwd2)
	
