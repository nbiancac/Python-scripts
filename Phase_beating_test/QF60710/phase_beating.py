"""
Qui calcolo il phase advance con la matrice di phase_beating.
QD.60710 con DeltaK=-1e-4

"""

import sys,os,time,re
sys.path.append('/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/')
from numpy import *
from string import split, replace, find,rfind
from metaclass25 import twiss

## Dati del quadrupolo QD 60710

Qx = 26.13
Qy = 26.18
Dkquad = -1e-4
L = 3.085
phquad_x = 2*pi*22.6364182
phquad_y =2*pi*22.68274943
betaquad_x = 21.0329844
betaquad_y = 101.6479285

## Dati del lattice non perturbato

H_base=twiss('bph.base')
V_base=twiss('bpv.base')

ph_x =    2*pi*H_base.MUX
beta_x =    H_base.BETX
name_x =    H_base.NAME
pos_x =     H_base.S

ph_y =    2*pi*V_base.MUY
beta_y =    V_base.BETY
name_y =    V_base.NAME
pos_y =     V_base.S

print "\n Data read from bph.base and bpv.base \n"

outf=open('H_formula.dat','w')
print >> outf, "PHASE BEATING FORMULA X-PLANE\n"
for k in range(0,len(ph_x)):
	if 'BPH.' in name_x[k]:
		if ph_x[k] < phquad_x:
			ciccio = betaquad_x*L*Dkquad*(cos(ph_x[k]-2*phquad_x+2*pi*Qx)*sin(ph_x[k]))/(2*sin(2*pi*Qx)) 

		else:
			ciccio = (betaquad_x/2+(betaquad_x*cos(ph_x[k]-2*phquad_x)*sin(ph_x[k]-2*pi*Qx)/(2*sin(2*pi*Qx))))*(L*Dkquad)

		outf.write(name_x[k]+' '+str(pos_x[k])+' '+str(ciccio)+'\n')
	else:
		print "deleted ", name_x[k], "monitor \n"
outf.close()
	
outf=open('V_formula.dat','w')
print >> outf, "PHASE BEATING FORMULA Y-PLANE\n"		
for k in range(0,len(ph_y)):
	if 'BPV.' in name_y[k]:
		if ph_y[k] < phquad_y:
			ciccio = betaquad_y*L*-Dkquad*(cos(ph_y[k]-2*phquad_y+2*pi*Qy)*sin(ph_y[k]))/(2*sin(2*pi*Qy))

		else:
			ciccio = (betaquad_y/2+(betaquad_y*cos(ph_y[k]-2*phquad_y)*sin(ph_y[k]-2*pi*Qy)/(2*sin(2*pi*Qy))))*(-L*Dkquad)

		outf.write(name_y[k]+' '+str(pos_y[k])+' '+str(ciccio)+'\n')
	else:
		
		print "deleted ", name_y[k], "monitor \n"	
outf.close()

print "Data written in H_formula.dat and V_formula.dat \n"
