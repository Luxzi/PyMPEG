import os
import sys

loop = 1

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


def main():

    while loop == 1:    
        com = input(bcolors.BOLD + bcolors.OKGREEN + "FFmpeg~>")
        if(com[:1] == "-"):
            os.system("ffmpeg " + com)
        else:
            print(bcolors.WARNING + "Please Use A Paramter!")
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting... KeyboardInterupt')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
