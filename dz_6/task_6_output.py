import sys
with open('bakery.cav') as f:

    if len(sys.argv) == 1:
        print(f.read())
    elif len(sys.argv) == 2:
        numstr = int(sys.argv[1])
        for i,line in enumerate(f):
            if (i+1) >= numstr:
                print(line.strip())
    elif len(sys.argv) == 3:
        numstr_start = int(sys.argv[1])
        numstr_end = int(sys.argv[2])
        for i,line in enumerate(f):
            if (i+1) >= numstr_start and (i+1)<=numstr_end:
                print(line.strip())
    else:
        print('слишком много аргументов')

