# berlin-citizen-office-helper

So this is my very first python project born from the difficulty to get an appointment at the berlin citizen office ("Bürgeramt") during peak of the COVID-crisis.
I'm very aware that I am violating some basic rules of what's considered to be professional programming style. Sorry for that, might fix it later.

The type of appointment is set to the purpose of apartment registration. But that could be changed easily.

So what do you need to run it?
A Linux system with Python 3.X installed. I did it with a Raspberry Pi 3.
Make sure the path home/$user/Projekte/Wohnungsanmeldungstermin/Rohdaten/ exists.
And of course, if you'd like to receive a Push Notification, make sure to have the app Prowl installed and retreive the necessary token.
pyprowl, requests, os and datetime musst be installed in Python.
