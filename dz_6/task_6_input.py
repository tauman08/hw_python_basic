import sys


if len(sys.argv)>1:
     with open('bakery.cav','a') as f:
         f.write(f'{sys.argv[1]}\n')





