def info():
    print(
        colored(' [*] Your PC/exec. Informations:', 'dark_grey'),

f'''
    Platform:\t\t {platform.system()} - {platform.architecture()[0]}
    Py. Version:\t Python {platform.python_version()[0]}
    
    --termcolor = \"{version('termcolor')
}\"\n''')

def connScan(self, tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		
		print(colored(f' [+] {tgtPort}: TCP Open', 'green'))

	except:
		print(colored(f' [-] {tgtPort}: TCP Closed', 'red'))

	finally: sock.close()

def portScan(self, tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)

	except: print(f'\n [*] Unknown \"{tgtHost}\" Host.')

	try:
		tgtName = gethostbyaddr(tgtIP)
		print(f'\n [*] Scan Results for \"{tgtName[0]}\":\n')

	except: return

	socket().settimeout(1)

	for tgtPort in tgtPorts:
		try:
			assert len(tgtPort ) != 0

			t = Thread(target = self.connScan, args = (tgtHost, int(tgtPort)))
			t.start()

		except ValueError as err:
			if str(err)[41:45] == 'None':
				print(f' [-] -H <target host> {colored("-p", "red")} <target port>')
				return
			
			else:
				print(colored(f' [-] Port \"{tgtPort}\"??', 'red'))
		
		except Exception: pass

def main(self):
	'''
    ** MADE WITH/FOR:
        Platform:\t Windows
        Py. Version:\t Python 3

        --termcolor = "2.2.0"

    FUNCTION: Scan the Specified Port(s) From Host Input.
    '''

	parser = optparse.OptionParser('[*] Usage of program: -H <target host> -p <target port>')

	parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'Specify Target Host.')
	parser.add_option('-p', dest = 'tgtPort', type = 'string', help = 'Specify Target Ports Seperated by Comma.')

	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')

	if (tgtHost == None) | (tgtPorts[0] == None):
		print(f' {parser.usage}'); exit(0)

	info(); parser.print_help()
	self.portScan(tgtHost, tgtPorts)

import optparse, platform

from socket import *
from os import system
from threading import Thread
from termcolor import colored
from importlib.metadata import version

obj = type('Obj', (object, ), {'main': main, 'connScan': connScan, 'portScan': portScan})
start = obj()

try:
    system('cls'); help(obj.main); start.main()
except KeyboardInterrupt: exit(0)	
except Exception as err: input(colored(f'\n {type(err).__name__}: {err}.', 'red'))