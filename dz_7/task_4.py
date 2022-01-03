
import os
def write_dict(dict_stat,size):
   for key in dict_stat:
      if size <= key:
         dict_stat[key] += 1
         break
   else:
      dict_stat.setdefault(key*10,0)
      write_dict(dict_stat, size)

dict_stat = {100:0}
for root, dirs, files in os.walk(r'C:\Windows'):
   for file in files:
      size = int(os.stat(os.path.join(root,file)).st_size)
      write_dict(dict_stat, size)

for key,value in dict_stat.items():
   print(key,value)