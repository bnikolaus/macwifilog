#!/usr/bin/python
import os
import datetime
import sys
import subprocess
import time
import getpass

interval = 1
arr =[]
sudoPassword = getpass.getpass()
sezitup = "sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/bin/airport"
command = "airport -I"  # the shell command
p = os.system('echo %s|sudo -S %s' % (sudoPassword, sezitup))

#for line in iter(process.stdout.readline,''): 
#   arr.append(line.rstrip('\n'))
#   text = map(lambda x: x.strip(" "), arr)
#   print ','.join(new_arr)

f = open('wifilog.log', 'w')

def _log(text):
   process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True) 
   for line in iter(process.stdout.readline,''):
      arr.append(line.rstrip('\n'))
      text = map(lambda x: x.strip(" " + "'"), arr)
      text = ",".join(text) 
   print "{date} - {text}".format(date=datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), text=text)
   f.write("{date} - {text}\n".format(date=datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), text=text))

if __name__ == '__main__':
   while True:   
      _log('')
      arr =[] 
      time.sleep(interval)
