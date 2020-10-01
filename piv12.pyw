

import pyprowl
import requests
import os
import datetime

username = 'javajim'
prioritaetsvariable = 0

url = 'https://bit.ly/37313HC'

#naechste Zeile auskommentieren, wenn alte datei verwendet werden soll
myfile = requests.get(url, allow_redirects=True)

file1 = '/home/'+ username +'/Projekte/Wohnungsanmeldungstermin/Rohdaten/result.html'

filelocation = file1

#naechste Zeile auskommentieren, wenn alte datei verwendet werden soll
open(filelocation, 'wb').write(myfile.content)

erfolgsvariable = 0

with open(file1) as myfile:
     if '\"nichtbuchbar\"' in myfile.read():
         print('nichtbuchbar vorhanden '+ str(datetime.datetime.utcnow()))
     else:
         print('nichtbuchbar nicht vorhanden '+ str(datetime.datetime.utcnow()))

with open(file1) as myfile:
     if '\"buchbar\"' in myfile.read():
         print('buchbar vorhanden')
         erfolgsvariable = 1
         prioritaetsvariable = 2
         p = pyprowl.Prowl('d8ae5589186cee2ecdb647127b3fd2cb6196ee5d')

         try:
         	p.verify_key()
         	print("Prowl API key successfully verified!")
         except Exception as e:
         	print("Error verifying Prowl API: {}".format(e))
         	exit()
         
         try:
         	p.notify(event=' Neuer Termin?', description="ERFOLG", 
         			 priority=prioritaetsvariable, url='https://bit.ly/37313HC', 
         			 #apiKey='uncomment and add API KEY here if different', 
         			 appName='Berlin.de Bot ')
         	print("Notification successfully sent to Prowl!")
         except Exception as e:
         	print("Error sending notification to Prowl: {}".format(e))


     else:
         print('buchbar nicht vorhanden '+ str(datetime.datetime.utcnow()))

         




