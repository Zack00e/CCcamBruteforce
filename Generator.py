
import sys
import random
import string 
import time
from colorama import init, Fore
init()
digits = string.digits
letters = string.ascii_lowercase

def hiberlo():
 x = int(input('How many clines you want to generate?: '))

 print( '\n'
 'Ex: \n' 
 'C:' '93.104.212.242 3333 AA(111) hiberlo.com \n'
 'C:' '93.104.212.242 3333 AA(2222) hiberlo.com \n'
 'C:' '93.104.212.242 3333 AA(33333) hiberlo.com \n'
 '\n'
 '> Default: 3 digits'
 '\n'
 )

 print('How many digits on the clines username you want?: \n')
 print('Enter 1 for (3 digits) \n')
 print('Enter 2 for (4 digits) \n')
 print('Enter 3 for (5 digits) \n') 
 choice = int(input('Enter your choice: '))

 if (choice == 1):
  with open ('list.txt', 'w') as f:
   for i in range (x):
    f.write('93.104.212.242 3333 ' + ( ''.join(random.choice(letters) for i in range(2))) + ( ''.join(random.choice(digits) for i in range(3))) + ' hiberlo.com' + '\n')
 
 elif (choice == 2):
   with open ('list.txt', 'w') as f:
    for i in range (x):
     f.write('93.104.212.242 3333 ' + ( ''.join(random.choice(letters) for i in range(2))) + ( ''.join(random.choice(digits) for i in range(4))) + ' hiberlo.com' + '\n')

 elif (choice == 3):
   with open ('list.txt', 'w') as f:
    for i in range (x):
     f.write('93.104.212.242 3333 ' + ( ''.join(random.choice(letters) for i in range(2))) + ( ''.join(random.choice(digits) for i in range(5))) + ' hiberlo.com' + '\n')

 else:
  print(Fore.RED + 'Invalid choice')
  sys.exit(1)

 time.sleep(2)  
 print('> Results has been saved inside list.txt')


def cccamserverde():
 p = int(input('How many clines you want to generate?: '))
 with open ('list.txt', 'w') as f:
   for i in range (p):
    f.write('cccamtv.spdns.org 24500 ' + ( ''.join(random.choice(letters) for i in range(2))) + ( ''.join(random.choice(digits) for i in range(4))) + ' server.de' + '\n')
   
 time.sleep(2)  
 print('> Results has been saved inside list.txt')
 



print(Fore.BLUE + """    ____ _ _                
  / ___| (_)_ __   ___ ____
 | |   | | | '_ \ / _ \_  /
 | |___| | | | | |  __// / 
  \____|_|_|_| |_|\___/___|
                            by Zack00e """)                           
time.sleep(2)
print('\n')
print(Fore.RED + '[!] Only two CCcam providers added at the moment')
print('\n')
print('\033[39m')
print('Enter 1 for Hiberlo.com clines \n')
print('Enter 2 for Cccam-server.de clines \n')

choice0 = int(input('Choose what CCcam server you want: '))
if (choice0 == 1):
 hiberlo()
elif (choice0 == 2):
 cccamserverde()
else:
 print(Fore.RED + 'Invalid choice')
 sys.exit(1)




