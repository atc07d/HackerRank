#Begin with simple binary to decimal conversion of smaller binary numbers

import cmath,math,re,string

#function for actual conversion after length and contents test are passed
#found online in pthon docs..."Pythons for statements iterates over the items
#of any sequence(list or string) in the order that they appear."
#numInput is the actual string and length is length of said string
def nowConvert(numInput, length):
    total = 0
    counter = length - 1
    for x in numInput:
        #print(x)
        if x == '1':
            #print(counter)
            total = total + 2**counter
            counter = counter - 1
            #print(total)
        else:
            counter = counter - 1

    return total

def promptUser():
    print('Welcome to the binary to decimal converter!')
    print('Please enter a binary number with <10 digits:')
    bnum = input()
    return bnum

def filterPrompt(response):
    bnum = response
    bnlength = len(bnum)
#try if find_this in str1 and find_this2 in str1:
#use regular expression to make sure string is only 0s and 1s
    if re.match("[0-1]*$", bnum):
        #print(bnum + ' contains only 0 and 1...proceed')
        #checks to make sure string is <10 digits
        if bnlength < 10:
            #call nowConvert function to return total and print
            #totalstr = str(nowConvert(bnum, bnlength))
            #print('Your number in decimal form is:  ' + totalstr)
            print('Your number in decimal form is:  ' )
            print(nowConvert(bnum, bnlength))
            print('Try again? (yes or no)')
            answer = input()
        else:
            print('String too long, try again? (yes or no)')
            answer = input()
    else:
        print('Input must contain only 1\'s and 0\'s and of correct length.')
        print('try again? (yes or no)', end='')
        answer = input()
  
    return answer

##############################
#main

answer = 'yes'

while answer == 'yes' or answer == 'y':
    asked = promptUser()
    
    if len(asked) > 9:
        print("Please input number less than 10.")
        asked
        answer = filterPrompt(asked)
    else:
        asked
        answer = filterPrompt(asked)
