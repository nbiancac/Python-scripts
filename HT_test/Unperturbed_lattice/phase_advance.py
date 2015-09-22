#!python2.5

import os, sys
from numpy import *

dir = '/afs/cern.ch/user/n/nbiancac/scratch0/Python/HT_test/Unperturbed_lattice/'
g=open('BPV_unperturbed.dat','w')
g.write('Phase X'+'\t\t'+'Phase Y'+'\n')

for file in os.listdir(dir):
	if '.ph' in file:
		print file
		f=open(file,'r')
		f.readline()
		appo=f.readline()
		g.write(appo+'\n')
		f.close()
g.close()
