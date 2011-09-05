#!/usr/bin/env python
import re
import sys
import argparse

displaystart = re.compile(r'''\\\[''')
displayend = re.compile(r'''\\\]''')
inlinestart = re.compile(r'''\\\(''')
inlineend = re.compile(r'''\\\)''')

def replace_math(s):
    if type(s) == file:
        s = s.read()
    s = inlinestart.sub("$", s)
    s = inlineend.sub("$", s)
    s = displaystart.sub("$$", s)
    s = displayend.sub("$$", s)
    
    return s
    
codefence = re.compile(r"""^'''(?P<lang>.*)""", re.MULTILINE)    

def replace_delimcode(s):
    if type(s) == file:
        s = s.read()
        
    m = codefence.search(s)
    if m is None:
        return s
    
    hasmatch = True    
    while hasmatch:
        start,end = m.span()
        lang = m.group('lang')
        panfence = '~~~'
        if len(lang):
            panfence += "{.%s}" % lang
        s = s[:start] + panfence + s[end:]
        m = codefence.search(s)
        if m is None:
            hasmatch = False
            
    return s
    
    
if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type = argparse.FileType('r'), default = '-')
    args = parser.parse_args()
    print replace_delimcode(replace_math(args.input))
        