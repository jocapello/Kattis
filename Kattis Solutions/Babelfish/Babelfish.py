import sys
from collections import defaultdict

Words=defaultdict(lambda: 'eh')
Add = True

for line in sys.stdin:
    if Add:
        if line == '\n':
            Add=False
        else:
            Split=line.split()
            Words[Split[1]] = Split[0]
    else:
        print(Words[line[0:-1]])