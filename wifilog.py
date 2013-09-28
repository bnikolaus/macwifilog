#!/usr/bin/python
import os
import datetime
import sys
import subprocess
import time
import getpass
import argparse

interval = 1
arr =[]
args = ""
# setup symlink
try: 
	with open('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport'): pass

except IOError:
   print "airport is not where I am expecting it cannot setup symlink"

try:
   with open('/usr/bin/airport'): pass
  
except IOError:
   sudoPassword = getpass.getpass()
   sezitup = "sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/bin/airport"
   p = os.system('echo %s|sudo -S %s' % (sudoPassword, sezitup))
     
scan = "airport -s"
command = "airport -I"
outpath = ""

# Setup for parsing 
# for line in iter(process.stdout.readline,''): 
#   arr.append(line.rstrip('\n'))
#   text = map(lambda x: x.strip(" "), arr)
#   print ','.join(new_arr)

today = datetime.datetime.today().strftime('%m-%d-%Y')
fname = today + "-macwifilog.log"
f = open(outpath + fname, 'w')

def _log(text):
   process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True) 
   for line in iter(process.stdout.readline,''):
      arr.append(line.rstrip('\n'))
      text = map(lambda x: x.strip(" " + "'"), arr)
      text = ",".join(text) 
   print "{date},{text}".format(date=datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), text=text)
   f.write("{date},{text}\n".format(date=datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), text=text))

def parseArgs():
   parser = argparse.ArgumentParser(description='Display airport interface statistics')
   parser.add_argument('-o', help="path for output", required=False, dest='outpath')
   return args

if __name__ == '__main__':
   args = parseArgs() 
   startscan = subprocess.Popen(scan, stdout=subprocess.PIPE, stderr=None, shell=True)
   scanout = startscan.communicate()[0] 
   print scanout 
   while True:   
      _log('')
      arr =[] 
      time.sleep(interval)
