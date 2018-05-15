#!/usr/bin/env python
#______                 _       _ _   
#░░░▒█ ▒█░▒█ ░█▀▀█ ▒█▄░▒█ 
#░▄░▒█ ▒█░▒█ ▒█▄▄█ ▒█▒█▒█ 
#▒█▄▄█ ░▀▄▄▀ ▒█░▒█ ▒█░░▀█ 


from urllib2 import *
from platform import system
import sys
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
banner = '''
__________________¶________________¶
_________________¶¶________________¶¶
_______________¶¶¶__________________¶¶¶
_____________¶¶¶¶____________________¶¶¶¶
____________¶¶¶¶¶____________________¶¶¶¶¶
___________¶¶¶¶¶______________________¶¶¶¶¶
__________¶¶¶¶¶¶______________________¶¶¶¶¶¶
__________¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶
__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____________¶¶¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
___¶________¶¶¶¶¶¶¶______¶¶¶¶______¶¶¶¶¶¶¶
___¶_______¶¶¶¶¶¶¶¶___O_¶¶¶¶¶__O__¶¶¶¶¶¶¶¶
__¶¶¶______¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶
__¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
_¶¶¶¶¶____¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶
___¶¶_____¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶
___¶¶______¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶
____¶¶______¶¶________¶¶¶¶¶¶¶¶¶¶_______¶¶
_____¶¶______¶¶¶_______________________¶
_____¶¶________¶¶____¶¶¶¶¶¶¶¶¶¶¶______¶
______¶¶________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶__¶
_______¶¶__________¶¶¶_____¶¶¶¶¶¶¶¶¶¶
_________¶¶___________¶¶¶¶¶__¶¶¶¶¶¶¶¶¶
_____________________________¶¶¶¶¶¶¶¶¶¶
______________________________¶¶¶¶¶¶¶¶¶
_______________________________¶¶¶¶¶¶¶                                                                                         
==[[ .:: Name : JXPloit ::.]]==\033[91m
==[[ .:: Version: 1.0 ::.]]==\033[96m
==[[ .:: Author : JuaN ::.]]==\033[92m
==[[ .:: Facebook : https://www.facebook.com/juanluhax ::.]]==\033[93m
==[[ .:: Twitter: https://twitter.com/akaJuaN_ ::.]]==\033[95m
'''
print banner
def menu():
   print'''
\033[91m 1 \033[96m} \033[91m ==\033[93m> \033[92m DNS Lookup 
\033[91m 2 \033[96m} \033[91m ==\033[93m> \033[92m Whois Lookup
\033[91m 3 \033[96m} \033[91m ==\033[93m> \033[92m GeoIP Lookup
\033[91m 4 \033[96m} \033[91m ==\033[93m> \033[92m Port Scanner
\033[91m 5 \033[96m} \033[91m ==\033[93m> \033[92m Zone Transfer
\033[91m 6 \033[96m} \033[91m ==\033[93m> \033[92m Host Finder
\033[91m 7 \033[96m} \033[91m ==\033[93m> \033[92m Host DNS Finder
\033[91m 8 \033[96m} \033[91m ==\033[93m> \033[92m About Me 
\033[91m 00\033[96m} \033[91m ==\033[93m> \033[92m Exit
'''

slowprint("\033[1;91mThis Is Simple Script By :\033[92m JuaN " + "\n \033[93m Let's Start \033[96m --> --> --> \033[91m ")

menu()
def ext():
    ex = raw_input ('\033[92mContinue/Exit->-> ')
    if ex[0].upper() == 'E' :
           print 'Good-bye!!!'
           exit()
    else:
           clear()
           print banner
           menu()
           select()

def  select():
  try:
    joker = input("\033[96mEnter \033[92m00/\033[91m18 => =>  ")
    if joker == 2:
      dz = raw_input('\033[91mEnter IP Address : \033[91m')
      whois = "http://api.hackertarget.com/whois/?q=" + dz
      dev = urlopen(whois).read()
      print (dev)
      ext()
    elif joker == 1:
      dz = raw_input('\033[96mEntre Your Domain :\033[96m')
      dns = "http://api.hackertarget.com/dnslookup/?q=" + dz
      joker = urlopen(dns).read()
      print (joker)
      ext()
    elif joker == 3:
      dz = raw_input('\033[91mEnter IP Address : \033[91m')
      geo = "http://api.hackertarget.com/geoip/?q=" + dz
      ip = urlopen(geo).read()
      print (ip)
      ext()
    elif joker == 4:
      dz = raw_input('\033[96mEnter IP Address : \033[96m')
      port = "http://api.hackertarget.com/nmap/?q=" + dz
      scan = urlopen(port).read()
      print (scan)
      ext()
    elif joker == 5:
      dz = raw_input('\033[92mEntre Your Domain :\033[92m')
      zon = "http://api.hackertarget.com/zonetransfer/?q=" + dz
      tran = urlopen(zon).read()
      print (tran)
      ext()
    elif joker == 6:
      dz = raw_input('\033[91mEntre Your Domain :\033[91m')
      host = "http://api.hackertarget.com/hostsearch/?q=" + dz
      finder = urlopen(host).read()
      print (finder)
      ext()
    elif joker == 7:
      dz = raw_input('\033[91mEntre Your Domain :\033[91m')
      get = "https://api.hackertarget.com/mtr/?q=" + dz
      page = urlopen(get).read()
      print(page)
      ext()
    elif joker == 8:
      slowprint("............... ")
      slowprint("Name : JXPloit \033[92m")
      slowprint("...............")
      slowprint("Version : 1.0 \033[91m")
      slowprint(".............")
      slowprint("Author: JuaN \033[96m")
      slowprint("......................")
      slowprint("Twitter : https://twitter.com/akaJuaN_  \033[91m")
      slowprint("...........................................")
      slowprint("Facebook : https://www.facebook.com/juanluhax \033[96m ")
      slowprint(".............................................................. ")
      ext() 
    elif joker == 00:
      print "Good-bye!!"
  except(KeyboardInterrupt):
    print "\nCtrl + C -> Exiting!!"
select()