#!/usr/bin/env python3

import re
import sys

file_name = 'README.md'

if(len(sys.argv) > 1):
    file_name = sys.argv[1]

PURPLE    = '\033[95m'
CYAN      = '\033[96m'
DARKCYAN  = '\033[36m'
BLUE      = '\033[94m'
GREEN     = '\033[92m'
YELLOW    = '\033[93m'
RED       = '\033[91m'
BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
NORMAL    = '\033[0m'

#
# 
#
f = open(file_name, 'r')
content = f.read().split('\n')
f.close()

for line in content:
    if(re.match("^#[^#].*", line)):
        print(BOLD + line[1:].strip())

print(NORMAL + '---')
