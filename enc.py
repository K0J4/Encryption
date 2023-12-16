import os
try:
  os.system('chmod 777 enc && ./enc')
except:
  from enc import main
