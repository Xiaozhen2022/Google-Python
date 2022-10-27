#!/usr/bin/env python3
import csv
import re
import operator
import os

error={}
per_user={}
logfile = os.path.abspath("syslog.log")
#print(logfile)
with open(logfile,"r") as f:
 for line in f:
   #r=re.search(r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$",line)
   r=re.search(r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) \(([\w.]*)\)$",line)
   print(line)
   print(r) 
   if r.group(1)=='ERROR':
      if r.group(2) not in error.keys():
         error[r.group(2)] = 0
      error[r.group(2)] += 1
      if r.group(3) not in per_user.keys():
         per_user[r.group(3)] = {}
         per_user[r.group(3)]['INFO']=0
         per_user[r.group(3)]['ERROR']=0
      per_user[r.group(3)]['ERROR'] += 1
   else:
      if r.group(3) not in per_user.keys():
         per_user[r.group(3)] = {}
         per_user[r.group(3)]['INFO']=0
         per_user[r.group(3)]['ERROR']=0
      per_user[r.group(3)]['INFO'] += 1
sorted_messages=[("Error","Count")]+sorted(error.items(), key = operator.itemgetter(1), reverse=True)
sorted_users=[("Username","INFO","ERROR")]+sorted(per_user.items())
#print(sorted_messages)
#print(sorted_users) 
with open("error_message.csv", "w") as error_file:
 for line in sorted_messages:
  error_file.write("{}, {}\n".format(line[0], line[1]))
with open("user_statistics.csv", "w") as user_file:
 for line in sorted_users:
  if line[0]=='Username':
    user_file.write("{},{},{}\n".format('Username','INFO','ERROR'))
  else:
    user_file.write("{},{},{}\n".format(line[0],str(line[1]['INFO']),str(line[1]['ERROR'])))
