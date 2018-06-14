#!/usr/bin/python


#Author: Ivan Letal


from bs4 import BeautifulSoup
import requests
import os
#import smtplib
#from email.mime.multipart import MIMEMultipart


log = './motorbike.last'
recipients = ['dareback@gmail.com']
url = 'https://online.dubaidutyfree.com/ddf/browse/subcategory_win_withddf.jsp?navAction=push&navCount=1&categoryName=+Finest+Surprise+-+Bike&categoryId=cat520005'


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


if __name__ == '__main__':
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  divs = soup.find_all('div', attrs={'class':'showcase'})
  links = []
  for d in divs:
    link = d.find('img')
    links.append(link.attrs['alt'])  
  motorbike = links[-1]

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
