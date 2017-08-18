# regex version of strip()
# Write a function that takes a string and does the same thing as the strip() function
# If no args are passed other than string then white space chars will be removed from start/end of string
# If second arg included then remove that char from string
# Run Py -3 regexStrip.py
import re, sys
 
def regexStripSysArg():
 
        if len(sys.argv) == 2:  # strip white space
                victimRegex = re.compile(r'(\s*)')
        elif len(sys.argv) == 3:        # strip second arg char
                victimRegex = re.compile(r'[' + sys.argv[2] +']*')
        else:   # need either 1 or 2 args to run
                print("Please enter one or two arguments: victim string and/or pattern")
                sys.exit(0)
       
        print(victimRegex.sub('',sys.argv[1]))
       
def regexStripVar(victim):
 
        victimRegex = re.compile(r'(\s*)')
        print(victimRegex.sub('', victim))
 
victim = 'This is my first time guys so pleaes go easy K.'     
regexStripSysArg()
#regexStripVar(victim)
#print(sys.argv)
