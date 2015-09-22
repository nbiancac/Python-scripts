"""
Qui calcolo il beta beating con la matrice di beta_beating.

"""

import sys,os,time,re
sys.path.append('/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/')
from numpy import *
from string import split, replace, find,rfind
from metaclass25 import twiss

Qx = 26.13
Qy = 26.18
Dkquad = -1e-4
L = 3.085
phquad_x = 2*pi*22.6364182
phquad_y =2*pi*22.68274943
betaquad_x = 21.0329844
betaquad_y = 101.6479285

def read_betaxy(file):
	f=twiss(file)
	beta_x=f.BETX
	beta_y=f.BETY

	return beta_x, beta_y

def read_muxy(file):
	f=twiss(file)
	phx=2*pi*f.MUX
	phy=2*pi*f.MUY
	
	return phx, phy

print "\n Qx, Qy, beta, phase, Dk read.\n Calculating beta beating matrix...\n"


(beta_x, beta_y) = read_betaxy('bpm.base')
(ph_x, ph_y)= read_muxy('bpm.base')

beta_beat_x=[]

for k in range(0,len(ph_x)):
	
		ciccio = -L*beta_x[k]*betaquad_x*cos(2*abs(ph_x[k]-phquad_x)-2*pi*Qx)*Dkquad/(2*sin(2*pi*Qx))
	
		beta_beat_x.append(ciccio)
	
		
beta_beat_y=[]

for k in range(0,len(ph_y)):
	
		ciccio = -L*beta_y[k]*betaquad_y*cos(2*abs(ph_y[k]-phquad_y)-2*pi*Qy)*-Dkquad/(2*sin(2*pi*Qy))
	
		beta_beat_y.append(ciccio)
	

f=open('beta_beating_formula.dat','w')	
f.write('beta_beat_Xplane'+'\t'+'beta_beat_Yplane'+'\n\n')
beta_beat_x=[str(x) for x in beta_beat_x]
beta_beat_y=[str(y) for y in beta_beat_y]
for k in range(0, len(beta_beat_x)):
	f.writelines(beta_beat_x[k]+'\t\t'+beta_beat_y[k]+'\n')		
f.close()	
		
print "Data written in beta_beating_formula.dat\n"
