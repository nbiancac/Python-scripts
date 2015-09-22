"""
script per cancellare i dip e i quad di un kicker
inserire il nome del kicker

moduli riutilizzabili:
- count_line
"""

import sys, os

def count_line(path):
	"""
	conta le linee [int]=count_line[path]
	"""
	f=open(path,'r')
	lines=0
	for line in f:	
		lines+=1
	return lines
		
def delete_column(dir, element):
	
	temp='tmp.dat'
	f=open(dir+element,'r+')
	g=open(dir+temp,'w')
	lines=count_line(dir+element)
	print "numero linee:", lines
	title = f.readline()
	g.writelines(title)
	for i in range(1, lines):
		appo = f.readline()
		appo=appo.split()
		appo[1]='0.000000000000000000000000\n'
		print appo
		g.write(appo[0]+'\t\t'+appo[1])
	f.close()
	g.close()
	os.system('cp '+dir+'tmp.dat '+dir+element)	
	os.system('rm '+dir+'tmp.dat')
	
dir='/afs/cern.ch/user/n/nbiancac/scratch0/HEADTAIL_RELEASE/'
element= sys.argv[1]

print "data read from\n", sys.argv[1]

delete_column(dir, element)

print "column deleted\n" 
