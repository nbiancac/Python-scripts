"""
Qui calcolo il phase advance semplicemente confrontanto i due lattice di madx, 
con e senza quadrupolar error.
"""



import sys,os,time,re
sys.path.append('/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/')
from operator import *
from numpy import *
from string import split, replace, find,rfind
from metaclass25 import twiss

Qx=26.13
Qy=26.18

print "\nData analysis...\n"

H_base=twiss('bph.base')
H_pert=twiss('bph.pert')
V_base=twiss('bpv.base')
V_pert=twiss('bpv.pert')

outf=open('H_madx.dat','w')
print >>outf, "X-PLANE PHASE BEATING FROM MAD-X"
name=H_base.NAME
pos=H_base.S
phx=map(sub, 2*pi*H_pert.MUX, 2*pi*H_base.MUX)

for k in range(0,len(name)):
	if 'BPH.' in name[k]:
		outf.write(name[k]+' '+str(pos[k])+' '+str(phx[k])+'\n')
	else:
		print "deleted ", name[k], "monitor \n"
outf.close()

outf=open('V_madx.dat','w')
print >>outf, "V-PLANE PHASE BEATING FROM MAD-X"
name=V_base.NAME
pos=V_base.S
phy=map(sub, 2*pi*V_pert.MUY, 2*pi*V_base.MUY)

for k in range(0,len(name)):
	if 'BPV.' in name[k]:
		outf.write(name[k]+' '+str(pos[k])+' '+str(phy[k])+'\n')
	else:
		print "deleted ", name[k], "monitor" 
outf.close()
	
		
print "Data written in H_madx.dat and V_madx.dat.dat\n"
		
	
	
