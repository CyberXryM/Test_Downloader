#!/usr/bin/python3
#Codec By Mr.yM
#Don't Copy My Code
from requests import post
try:
	from termcolor import colored
	import wget
	import click, sys
except Exception as Erorr:
	   print ("module nya belum di install lurr %s" %Erorr)
class ban(object):
	  def __init__(self):
	  	     self.c = click.clear()
	  	     self.ban = print (colored('''
  _                                        
  \\                                       
   \\_          _.-._                      
    X:\        (_/ \_)                     
    \::\       ( ==  )                     
     \::\       \== /                      
    /X:::\   .-./`-'\.--.                  
    \\/\::\ / /     (    l                 
     ~\ \::\ /      `.   L.                
       \/:::|         `.'  `               
       /:/\:|          (    `.             
       \/`-'`.          >    )             
              \       //  .-'              
               |     /(  .' / Instagram  \ 
               `-..-'_ \  \ \ Downloader / 
               __||/_ \ `-'                
              / _ \ #  |                   
             |  #  |#  |                   
             |  #  |#  |                   
	 	 	''','green'))
	  def oke(self):
	  	return print (colored("[!] contact me -> https://fb.me/Rizqy.Yusuf.Maulana [!]",'green', 'on_red'))
	  	pass
class ig:
	 def __init__(self):
	 	       self.okee = okee
	 	       self.head = {
                          'origin': 'https://igdown.net',
                          'x-requested-with': 'XMLHttpRequest',
                          'pragma': 'no-cache',
                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                          'accept': 'application/json, text/javascript, */*; q=0.01',
                          'cache-control': 'no-cache',
                          'authority': 'igdown.net',
                          'referer': 'https://igdown.net/',
                          }
	 	       self.data = {
	 	       'url': self.okee
	 	       }
	 	       import json
	 	       response = post('https://igdown.net/instagram-service.php', self.data, self.head)
	 	       self.gans = json.loads(response.text)
	 def gan(self, okee):
	 	 oh = str(input("[!] foto atau video ? :"))
	 	 okzz = self.gans["status"]
	 	 if "fail" in okzz:
	 	 	print ('invalid URL')
	 	 if oh =="foto":
	 	 	name = str(input("[ Nama File ]-> :"))
	 	 	out = (name)
	 	 	ow = []
	 	 	fot = self.gans["image"]
	 	 	for x in wget.download(fot, out):
	 	 	    ow.append(x)
	 	 elif oh =="video":
	 	 	name = str(input("[ Nama File ]-> :"))
	 	 	out = (name)
	 	 	ow = []
	 	 	vid = self.gans["videourl"]
	 	 	for x in wget.download(vid, out):
	 	 		ow.append(vid)
if __name__ == '__main__':
  try:
   oze = ban()
   oze.oke()
   okee = input(colored("[ Input Link ]-> :", 'blue'))
   oz = ig()
   p = oz.gan(str(okee))
  except KeyboardInterrupt:
	   pass
  except EOFError:
   	    pass
  except ConnectionError:
  	    pass
