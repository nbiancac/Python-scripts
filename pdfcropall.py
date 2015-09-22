#!/usr/bin/python

import sys, os

lista=os.listdir((os.getcwd()))

if len(sys.argv)>1:
	for el in lista:
		if ('pdf' in el) and ('crop' not in el) and (sys.argv[1] in el):
			print el
			os.system('pdfcrop '+el);
else:
	for el in lista:
		if ('pdf' in el) and ('crop' not in el):
			print el
			os.system('pdfcrop '+el);

