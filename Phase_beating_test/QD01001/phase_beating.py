"""
Qui calcolo il phase advance con la matrice di phase_beating.

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
phquad_x = 2*pi*0.135272664
phquad_y =2*pi*0.1357600375
betaquad_x = 20.96175452
betaquad_y = 103.1593376

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

print "\n Qx,y, BETX,Y Dk read.\n Calculating phase advance matrix...\n"


(beta_x, beta_y) = read_betaxy('bpm.base')
(ph_x, ph_y)= read_muxy('bpm.base')

phase_adv_x=[]


for k in range(0,len(ph_x)):
	if ph_x[k] < phquad_x:
		ciccio = betaquad_x*(cos(ph_x[k]-2*phquad_x+2*pi*Qx)*sin(ph_x[k])*L*Dkquad)/(2*sin(2*pi*Qx)) 
		#ciccio=betaquad_x*(Dkquad*L)/(4*sin(2*pi*Qx))*(sin(2*ph_x[k]-2*phquad_x-2*pi*Qx)+sin(2*phquad_x+2*pi*Qx)))))
		phase_adv_x.append(ciccio)
	else:
		ciccio = (betaquad_x/2+(betaquad_x*cos(ph_x[k]-2*phquad_x)*sin(ph_x[k]-2*pi*Qx)/(2*sin(2*pi*Qx))))*(L*Dkquad)
		#ciccio=betaquad_x*(Dkquad*L)/(4*sin(2*pi*Qx))*(sin(2*ph_x[k]-2*phquad_x-2*pi*Qx)+sin(2*phquad_x+2*pi*Qx))
		phase_adv_x.append(ciccio)
		
phase_adv_y=[]
for k in range(0,len(ph_y)):
	if ph_y[k] < phquad_y:
		ciccio = betaquad_y*(cos(ph_y[k]-2*phquad_y+2*pi*Qy)*sin(ph_y[k])*(-L*Dkquad))/(2*sin(2*pi*Qy))
		#ciccio=-betaquad_y*(-Dkquad)/4-betaquad_y*(-Dkquad)/(4*sin(2*pi*Qy))*sin(2*(phquad_y-ph_y[k])-2*pi*Qy)
		phase_adv_y.append(ciccio)
	else:
		ciccio = (betaquad_y/2+(betaquad_y*cos(ph_y[k]-2*phquad_y)*sin(ph_y[k]-2*pi*Qy)/(2*sin(2*pi*Qy))))*(-L*Dkquad)
		#ciccio=-betaquad_y*(-Dkquad)/4-betaquad_y*(-Dkquad)/(4*sin(2*pi*Qy))*sin(2*(ph_y[k]-phquad_y)-2*pi*Qy)
		phase_adv_y.append(ciccio)		





f=open('phase_beating.dat','w')	
f.write('Phase_advance_Xplane'+'\t'+'Phase_advance_Yplane'+'\n\n')
phase_adv_x=[str(x) for x in phase_adv_x]
phase_adv_y=[str(y) for y in phase_adv_y]
for k in range(0, len(phase_adv_x)):
	f.writelines(phase_adv_x[k]+'\t\t'+phase_adv_y[k]+'\n')		
f.close()	
		
print "Data written in phase_beating.dat\n"
