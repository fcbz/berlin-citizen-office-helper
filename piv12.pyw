

import pyprowl
import requests
import os
import datetime

p = pyprowl.Prowl('enter Prowl token here')
username = 'javajim'
prioritaetsvariable = 0
url = 'https://bit.ly/37313HC'
file1 = '/home/'+ username +'/Projekte/Wohnungsanmeldungstermin/Rohdaten/result.html'


#naechste Zeile auskommentieren, wenn alte datei verwendet werden soll
myfile = requests.get(url, allow_redirects=True)


filelocation = file1

#naechste Zeile auskommentieren, wenn alte datei verwendet werden soll
open(filelocation, 'wb').write(myfile.content)

erfolgsvariable = 0

with open(file1) as myfile:
     if '\"nichtbuchbar\"' in myfile.read():
         print('not-bookable available '+ str(datetime.datetime.utcnow()))
     else:
         print('not-bookable unavailable '+ str(datetime.datetime.utcnow()))

with open(file1) as myfile:
     if '\"buchbar\"' in myfile.read():
         print('bookable available')
         erfolgsvariable = 1
         prioritaetsvariable = 2


         try:
         	p.verify_key()
         	print("Prowl API key successfully verified!")
         except Exception as e:
         	print("Error verifying Prowl API: {}".format(e))
         	exit()
         
         try:
         	p.notify(event=' New appointment available?', description="SUCCESS, Appointment available", 
         			 priority=prioritaetsvariable, url='https://bit.ly/37313HC', 
         			 #apiKey='uncomment and add API KEY here if different', 
         			 appName='Berlin.de Bot ')
         	print("Notification successfully sent to Prowl!")
         except Exception as e:
         	print("Error sending notification to Prowl: {}".format(e))


     else:
         print('no appointment available '+ str(datetime.datetime.utcnow()))

         




