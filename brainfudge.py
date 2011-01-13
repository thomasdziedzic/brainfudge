#!/usr/bin/env python2

import sys

b2c = {'>':'++p;', '<':'--p;', '+':'++*p;', '-':'--*p;', '.':'putchar(*p);', ',':'*p=getchar();', '[':'while(*p){', ']':'}'}

def translate(c):
	try:
		return b2c[c]
	except KeyError:
		return ''

f = open(sys.argv[1] + '.c', 'w')

f.write('#include<stdio.h>\n')
f.write('#include<stdlib.h>\n')
f.write('int main(){unsigned char* p=malloc(sizeof(unsigned char) * 8 * 1024 * 1024);' + ''.join( translate(c) for c in open(sys.argv[1]).read() ) + 'return 0;}')

f.close()
