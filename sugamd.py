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
table_mode = False

hrline = '---------------------------------------------------------------------------------------------------\n'

records = []

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

for line in content:
    painted = False

    if(re.match("[^`]*```[^`]*", line)):
        block = not block
        line = '\n' + indent + GREEN + hrline

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

        if(re.match("^\s*[\*]\s+[^*]*", line)):
            line = indent + ' - ' + BOLD + line.strip().replace('*', '')
            painted = True

        if(not painted and line != hrline):
            line = NORMAL + indent + line.strip()

        if(re.match(r'.*\|', line)):
            table_mode = True
            xs = line.split("|")[1:]
            xs = [x.strip() for x in xs]
            records.append(xs)
        elif(table_mode == True):
            table_mode = False

            col_max_sizes = []
            for col in records[0]:
                col_max_sizes.append(0)
                
            for row in records:
                i = 0
                for col in row:
                    if(col_max_sizes[i] < len(col)):
                        col_max_sizes[i] = len(col)
                    i = i + 1
            
            records_cp = []
            for row in records:
                rlflag = False
                xs = []
                i = 0
                for col in row:
                    col = col.replace(':', '-')
                    if(len(col) < col_max_sizes[i]):
                        for j in range(col_max_sizes[i] - len(col)):
                            pad = ' '
                            if(re.match("^\-+$", col)):
                                pad = '-'
                            if(rlflag):
                                col = pad + col
                            else:
                                col = col + pad
                            rlflag = not rlflag
                    xs.append(col) 
                    i = i + 1
                records_cp.append(xs)
            
            for row in records_cp:
                for col in row:
                    print(col + '|', end = '')
                print("")
            records = []

        if(not table_mode):
            line = re.sub('`([^`]+)`', BOLD + '\\1' + NORMAL, line)
            line = re.sub('\*\*([^*]+)\*\*', BOLD + '\\1' + NORMAL, line)
            line = re.sub('\*([^*]+)\*', BOLD + '\\1' + NORMAL, line)
        # line = re.sub('(\(http.*\))', BOLD + '\\1' + NORMAL, line).replace('(', '').replace(')', '')

    if(block and line != hrline):
        line = GREEN + indent + line

    if(not table_mode):
        print(line)

print(NORMAL + '---')
