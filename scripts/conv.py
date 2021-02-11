#!/usr/bin/env python3

import sys



    #print(i)
for test in sys.stdin:
    test = test.rstrip()
    if test.startswith('#'):
        txt = test.count('#')
        if txt:
            t = txt * '#'
            m = test.split(' ')[0].replace(t,f'<h{txt} align="right">')
            c = test.split(' ')
            c[0] = m
            print(''.join(c))
