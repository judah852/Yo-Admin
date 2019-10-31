import time
import urllib.request
import sys
from multiprocessing.dummy import Pool
import argparse
from argparse import RawTextHelpFormatter

#define color code
class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
        bold='\033[1m'
        end='\033[0m'
# parse argument

parser=argparse.ArgumentParser(description='YO! Admin v1.0 (c) 2019 by ChefLoop - Please do not use in military or secret service organizations, or for illegal purposes.'+'This is a tool to uncovered admin relevant pages from web application!!' )
#ascii art
print (fg.bold+fg.lightred+'__  ______  __   ___       __          _     '+fg.end)
print (fg.bold+fg.lightblue+'\\ \\/ / __ \\/ /  /   | ____/ /___ ___  (_)___ '+fg.end)
print (fg.bold+fg.yellow+' \\  / / / / /  / /| |/ __  / __ `__ \\/ / __ \\ '+fg.end)
print (fg.bold+fg.lightgreen+' / / /_/ /_/  / ___ / /_/ / / / / / / / / / /'+fg.end)
print (fg.bold+'/_/\\____(_)  /_/  |_\\__,_/_/ /_/ /_/_/_/ /_/ \n'+fg.end)

parser.add_argument('-u', help='The target to find admin relevant pages and http:// or http:// is needed : website domain URL such as https://www.example.com')
parser.add_argument('-d', help='The wordlist FILE to load from' )
args=parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)


#get variable as input
start = time.time()
url=args.u
#url = sys.argv[1]
if url.endswith('/')!=True:
    url=url+'/'
wordlist=args.d
#wordlist = sys.argv[2]
f = open ( wordlist, 'r' )
check=0
succeed=0

#multiprocessing and looping 
pool=Pool(10)
responselist=[]
for x in f:
    fullurl= (url+x).split("\n")[0]
    responselist.append(pool.apply_async(urllib.request.urlopen,[fullurl]))
    check+=1
    print ('Testing at URL :', fullurl + ''*10, end='\r', flush=True)
if f.read()== '':
    print (' '*100)
for response in responselist:
    print ('Checking response:', response,end='\r', flush=True)
    try:
        if(response.get().getcode()==200):
            print ('You have uncovered the admin login page.'+ ' '*100) 
            print (fg.lightgreen+'The URL is :',response.get().geturl().split('?')[0]+fg.end)
            succeed+=1
    except urllib.error.URLError:
        pass
#Signposting about result
print(" Finished checking "+str(check)+' URLs'+' '*100)
print('There are ', succeed , 'valid links to admin login page')	
end=time.time()
time=end-start
print ('Process time in Seconds:',time)
