import os

dir= '/afs/cern.ch/user/n/nbiancac/scratch0/Python/HT_test/Unperturbed_lattice/'

for file in os.listdir(dir):
	
	if 'BPV' in file:
		f=open(dir+file,'r')
		a=f.readlines()
		print a
		a.pop()
		f.close()
		g=open(dir+file,'w')
		g.writelines(a)
		g.close()

		
