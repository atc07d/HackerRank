# dotcount.py
# ac 09 28 17
# loop through the hyperion \\LOGS directory and count the dots in each application's log
import os
shared_dir_name = r'\\LOGS'
log_year = '17'
with open(r'C:\Users\user\Documents\dotcount'+ log_year + '.log', mode='w', encoding='utf-8') as dc_log_file:
    os.chdir(shared_dir_name)
    for cw_dir in os.listdir('.'):
        if cw_dir[-2:] == log_year:            
            os.chdir(cw_dir)            
            dc_log_file.write('****DATE: ' + cw_dir[-10:] + '****\n') # write name of dir in to log file eg 01-01            
            for log_filename in os.listdir('.'):                
                if log_filename[-9:] == 'calcs.log':                    
                    dc_log_file.write('--' + log_filename[:-10] + '--\n') # write name of file eg payroll.calcs.log                    
                    with open(log_filename, encoding='utf-8') as open_log_file:                        
                        for a_line in open_log_file:                            
                            if 'CalcObject' in a_line:                                
                                dc_log_file.write(a_line[21:]) # write name of calc                             
                            if 'Calculation in progress' in a_line:                                
                                dc_log_file.write(str(len(a_line[50:])) + '\t') # write length of remaing characters aka number of dots            
            os.chdir(shared_dir_name) # change back to main LOGS dir after looping through log files in dir of specific date 
