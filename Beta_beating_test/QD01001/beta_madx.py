"""
Qui calcolo il beta beat semplicemente confrontanto i due lattice di madx, 
con e senza quadrupolar error.
"""



import sys,os,time,re
sys.path.append('/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/')
from operator import *
from numpy import *
from string import split, replace, find,rfind
from metaclass25 import twiss

print "\nReading beta functions...\n"
	
	
beta_pertx=twiss("bpm.dat").BETX
beta_perty=twiss("bpm.dat").BETY
betax=twiss("bpm.base").BETX
betay=twiss("bpm.base").BETY

delta_beta_x=map(sub,beta_pertx, betax)
delta_beta_y=map(sub,beta_perty, betay)



f=open('beta_beating_madx.dat','w')	
f.write('Beta_beating_Xplane'+'\t'+'Beta_beating_Yplane'+'\n\n')
delta_beta_x=[str(x) for x in delta_beta_x]
delta_beta_y=[str(y) for y in delta_beta_y]
for k in range(0, len(delta_beta_x)):
	f.writelines(delta_beta_x[k]+'\t\t'+delta_beta_y[k]+'\n')		
f.close()	
		
print "Data written in beta_beating_madx.dat\n"
		
	
	
