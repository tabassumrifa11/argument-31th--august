print('\033c')

import os

shutdown = input("Do you wish to shutdown your computer? (yes or no):") 

if shutdown == 'no':
    exit()
    
    
else:
    os.system("shutdown /s /t 0")