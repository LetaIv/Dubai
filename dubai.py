#!/usr/bin/python


# Author: Ivan Letal
# Updated: 15.06.2018
# Usage: python dubai.py
# Note: recommended is to use scheduler (Windows Scheduler or Cron) for regular checking
# What does it do? Checks regularly if there is a new motorbike to buy at Dubai Duty Free. Sends a notification mail. Can be also used as an example for website scrapping.


from bs4 import BeautifulSoup
import requests
import os
#import smtplib
#from email.mime.multipart import MIMEMultipart


log = './motorbike.last'
recipients = ['dareback@gmail.com']
url = 'https://online.dubaidutyfree.com/ddf/browse/subcategory_win_withddf.jsp?navAction=push&navCount=1&categoryName=+Finest+Surprise+-+Bike&categoryId=cat520005'


#def send_mail1(mbike):
  #msg = MIMEMultipart()
  #msg['Subject'] = 'New motorbike on Dubai Duty Free - {}'.format(mbike)
  #msg['From'] = 'motorbike@yourdomain.com'
  #msg['To'] = "","".join(recipients)
  #msg.preamble = 'New motorbike'
  #s = smtplib.SMTP('smtp.yourdomain.com')
  #s.sendmail(msg['From'], msg['To'], msg.as_string())
  #s.quit()

def send_mail2(mbike):
  for i in recipients:
    os.popen('echo "" | mail -s "New motorbike on Dubai Duty Free - {}" {}'.format(mbike, i))


if __name__ == '__main__':
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  divs = soup.find_all('div', attrs={'class':'showcase'})
  links = []
  for d in divs:
    link = d.find('img')
    links.append(link.attrs['alt'])  
  mbike = links[-1]

  if os.path.exists(log):
    with open(log, 'r') as f: line = f.readline()  
    if line <> mbike: # content changed
      with open(log, 'w') as f: f.write(mbike)
      send_mail2(mbike)
    else: # content did not change
      pass    
  else: # running the script for the first time
    with open(log, 'w') as f: f.write(mbike)
    send_mail2(mbike)

