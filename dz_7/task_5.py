import os
import json as js

def write_list_extension(list_ext,ext):

   if ext != '' and not ext in list_ext:
      list_ext.append(ext)
   return list_ext


def write_dict(dict_stat,name_file,size):
   ext = os.path.splitext(name_file)[1]
   for key in dict_stat:
      if size <= key:
         local_list = list(dict_stat[key])
         local_list[0] = local_list[0]+1
         local_list[1] = write_list_extension(local_list[1], ext)
         dict_stat[key] = tuple(local_list)
         break
   else:
      dict_stat.setdefault(key*10,(0,[]))
      write_dict(dict_stat,name_file,size)

dict_stat = {100:(0,[])}
for root, dirs, files in os.walk('E:\curs'):
   for file in files:
      size = int(os.stat(os.path.join(root,file)).st_size)
      write_dict(dict_stat,file,size)

file_name = os.path.basename(os.getcwd())+'_summary.json'
with open(file_name,'w') as f:
   js.dump(dict_stat,f)
