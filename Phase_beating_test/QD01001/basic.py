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

def read_phase_adv(file):
	f=twiss(file)
	phx=2*pi*f.MUX
	phy=2*pi*f.MUY
	
	return phx, phy

print "\nData read, calculating phase advance...\n"
	
(phx_base_x, phy_base_y) = read_phase_adv('bpm.base')
(phx_quad_x, phy_quad_y) = read_phase_adv('bpm.dat')

delta_phase_adv_x = map(sub, phx_quad_x, phx_base_x)
delta_phase_adv_y = map(sub, phy_quad_y, phy_base_y)


f=open('phase_advance.dat','w')	
f.write('Phase_advance_Xplane'+'\t'+'Phase_advance_Yplane'+'\n\n')
delta_phase_adv_x=[str(x) for x in delta_phase_adv_x]
delta_phase_adv_y=[str(y) for y in delta_phase_adv_y]
for k in range(0, len(delta_phase_adv_x)):
	f.writelines(delta_phase_adv_x[k]+'\t\t'+delta_phase_adv_y[k]+'\n')		
f.close()	
		
print "Data written in phase_advance.dat\n"
		
	
	
