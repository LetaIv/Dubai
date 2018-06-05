#!/usr/bin/python

#Author: Ivan Letal

from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import os
#import smtplib
#from email.mime.multipart import MIMEMultipart

log = './motorbike.last'
recipients = ['dareback@gmail.com', 'dwad@seznam.cz']

page = urllib.urlopen('http://www.dubaidutyfree.com/Finest_Surprise/buy_bike')
soup = BeautifulSoup(page, 'html.parser')
li = soup.findAll('div', attrs={'class':'title'})
motorbike = str(li[1]).split('\n')[2].strip()

def sendmail(mbike):
  #msg = MIMEMultipart()
  #msg['Subject'] = 'New motorbike on Dubai Duty Free - ' + mbike
  #msg['From'] = 'root@stark.xpear.net'
  #msg['To'] = "","".join(recipients)
  #msg.preamble = 'New motorbike'
  #s = smtplib.SMTP('xpear.net')
  #s.sendmail(msg['From'], msg['To'], msg.as_string())
  #s.quit()
  for i in recipients:
    os.popen('echo "" | mail -s "New motorbike on Dubai Duty Free - %s" %s' % (mbike, i))

if os.path.exists(log):
  with open(log, 'r') as f: line = f.readline()  
  if line <> motorbike:
    # content changed
    with open(log, 'w') as f: f.write(motorbike)
    sendmail(motorbike)
  else: 
    # content did not change
    pass    
else:
  # running the script for the first time
  with open(log, 'w') as f: f.write(motorbike)
  sendmail(motorbike)
