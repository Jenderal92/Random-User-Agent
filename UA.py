# -*- coding: utf-8 -*
#!/usr/bin/python
#Random Useragent !
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#CONTACT ME :(
       # ICQ : https://icq.im/Shin403
       # Telegram : t.me/Shin_code
       # Youtube : Smile Of Beauty 
import requests,time,re,sys,random,os
from colorama import Fore,Style, init
init(autoreset=True)

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

def Useragent():
	try:
		apiS = "https://user-agents.net/random"
		getUs = requests.post(apiS
		,data={'limit': Limit,
		'action':'generate'}
		,headers={'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Origin' : 'https://user-agents.net',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.1124.105 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'Referer': 'https://user-agents.net/random',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'Cookie': '__gads=ID=852cc6da44d008fc-221cac59bbdf00c4:T=1682511968:RT=1682511968:S=ALNI_MYq6GEcio_mQ9rln1PYjpEb2RuASw; __gpi=UID=00000bfddc42bf19:T=1682511968:RT=1682511968:S=ALNI_MYmKYMzNKN-LvPVXIzhFm9HXiQT6g; _ga=GA1.2.1108192057.1682511983; _gid=GA1.2.1736687524.1682511991'}).content
		if 'Generate random list' in getUs:
			regex = re.findall('">Mozilla(.*?)</a></li>',getUs)
			for res in regex:
				print(g + 'Mozilla'+o+res)
				open('UA.txt','a').write('Mozilla'+res+'\n')
	except:
		pass
if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print "{} Random User Agent Generator  | {}Shin Code\n".format(y,c)
	Limit = sys.argv[1]
	Useragent()
#Thanks To : https://user-agents.net/



			
		
		
		