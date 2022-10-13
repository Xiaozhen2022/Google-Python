import re
def show_time_of_pid(line):
  pattern1 = r"^(\w{3} \d?\d (\d\d:){2}\d\d)|(\[(\d+)\])" 
  #result1 = re.search(pattern1, line)
  #pattern2 = r"\[(\d+)\]"
  #result2 = re.search(pattern2, line)
  #return result1[1]+' pid:'+result2[1]
  print(re.search(pattern1,line))
  #return re.sub(pattern1, r"\1 pid:\2", line)
print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440