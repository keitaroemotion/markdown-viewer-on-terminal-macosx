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
BLINK     = '\033[5m'
BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
NORMAL    = '\033[0m'
LIGHTBLUE = '\033[104m'

#
# 
#
f = open(file_name, 'r')
content = f.read().split('\n')
f.close()

block  = False
indent = '' 

hrline = '\n---------------------------------------------------------------------------------------------------\n'

for line in content:
    painted = False

    if(re.match("[^`]*```[^`]*", line)):
        block = not block
        line = hrline

    if(not block):
        if(re.match("^#[^#].*", line)):
            line = "\n" + BOLD + line.strip()[1:].strip()
            painted = True
            indent  = '' 

        if(re.match("^##[^#].*", line)):
            line = "\n  " + BOLD + line.strip()[2:].strip()
            painted = True
            indent  = '    ' 

        if(re.match("^###[^#].*", line)):
            line = "\n    " + BOLD + line.strip()[4:].strip()
            painted = True
            indent  = '        ' 

        if(re.match("^####[^#].*", line)):
            line = "\n    " + BOLD + line.strip()[6:].strip()
            painted = True
            indent  = '            ' 

        if(re.match("^\s*\*\s*.*", line)):
            line = indent + ' - ' + line.strip()[1:]
            painted = True

        if(not painted and line != hrline):
            line = NORMAL + indent + line.strip()

        line = re.sub('`([^`]+)`', BOLD + '\\1' + NORMAL, line)
        # line = re.sub('(\(http.*\))', BOLD + '\\1' + NORMAL, line).replace('(', '').replace(')', '')

    if(block and not hrline):
        line = BOLD + line

    print(line)

print(NORMAL + '---')
