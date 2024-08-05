'''
		###########
		 Echo Typhoon
		###########
 	Developed by Tanvir		
		
'''

import os
import sys
import time


os.system("clear")

# Color codes
b = '\033[1m'
g = '\033[32m'
c = '\033[36m'
rs = '\033[0m'

# logo
logo = f'''{b+c}

      _______          _                       
     |__   __|        | |                      
        | |_   _ _ __ | |__   ___   ___  _ __  
        | | | | | '_ \| '_ \ / _ \ / _ \| '_ \ 
        | | |_| | |_) | | | | (_) | (_) | | | |
        |_|\__, | .__/|_| |_|\___/ \___/|_| |_|
            __/ | |                            
           |___/|_|                            
                                                                                               
      {g} 
      
     	 #############################
	  [-] Tool Name: Pip installer	 
	  [-] Developer : Tanvir               
	  [-] Team: Echo Typhoon		  
	  [-] TG: @echo_typhoon           
	 #############################
      
                         
    {rs}'''
for i in logo:
	sys.stdout.write(i)
	sys.stdout.flush()
	time.sleep(0.001)

print("\t\t\tPypi Library Installing\n")
A = "\033[1;91m"
B = "\033[1;96m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
L = "\033[1;95m"
M = "\033[1;94m"
print(f'{A}={B}={C}={E}={H}={L}={M}='*9)

# List all libraries
libraries = [
    'mechanize', 'requests', 'pyfiglet', 'py_compile', 'youtube_dl', 'uuid',
    'colorama', 'beautifulsoup4', 'pafy', 'argparse', 'InstagramAPI',
    'generate_user_agent', 'cfonts', 'secrets', 'hashlib', 'threading',
    'datetime', 'json', 'webbrowser', 're'
]

for library in libraries:
    os.system(f'pip install {library}')


os.system('pip list --outdated --format=freeze | grep -v "^\-e" | cut -d = -f 1 | xargs -n1 pip install -U')

print("≠" * 50)
print("ALL PIP'S ARE INSTALLED AND UPGRADED")