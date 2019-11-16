import os

loop = 1
login = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE + "########  ##    ## ##     ## ########  ########  ######")   
print(bcolors.OKBLUE + "##     ##  ##  ##  ###   ### ##     ## ##       ##    ##")  
print(bcolors.OKBLUE + "##     ##   ####   #### #### ##     ## ##       ##")        
print(bcolors.OKBLUE + "########     ##    ## ### ## ########  ######   ##   ####") 
print(bcolors.OKBLUE + "##           ##    ##     ## ##        ##       ##    ##")  
print(bcolors.OKBLUE + "##           ##    ##     ## ##        ##       ##    ##")  
print(bcolors.OKBLUE + "##           ##    ##     ## ##        ########  ######")
print(bcolors.OKBLUE + "\nBy: Luxzi")
print(bcolors.OKBLUE + "\nVersion 0.0.2a" + bcolors.BOLD + bcolors.WARNING + " ALPHA BUILD" + bcolors.OKGREEN + " https://github.com/Luxzi/PyMPEG\n")

def mainloop():

	com = input(bcolors.BOLD + bcolors.OKGREEN + "FFmpeg#> ")
	os.system("ffmpeg " + com)

while loop == 1:    
    mainloop()
