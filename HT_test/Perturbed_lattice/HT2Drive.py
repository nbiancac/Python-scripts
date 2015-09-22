

from optparse import OptionParser
import os, sys

parser = OptionParser()
parser.add_option("-a", "--accel",
                help="Which accelerator: LHCB1 LHCB2 SPS RHIC",
                metavar="ACCEL", default="LHCB1",dest="ACCEL")
parser.add_option("-p", "--path",
                help="Path to Headtail BPM data",
                metavar="PATH", default="./", dest="path")
parser.add_option("-m", "--model",
                help="Twiss File",
                metavar="TwissFile", default="0", dest="Twiss")



(options, args) = parser.parse_args()


path=options.path

files=os.listdir(path)
files=filter(lambda p: '.dat.gz'  in p and ('BPV.' in p or 'BPH.' in p),  files)
print "extracting...\n"
for el in files:
	os.system('gunzip '+el)
    
files=os.listdir(path)
files=filter(lambda p: '.dat'  in p and ('BPV.' in p or 'BPH.' in p),  files)    

outf=open('fordrive.dat','w')
print >>outf, "#TITLE"

for el in files:
    f=open(el,'r')\
    
    if 'BPH' in el:
        HV=0
    elif 'BPV' in el:
        HV=1
    else:
        print "Problem with ", el
        sys.exit()
    
    name=el.replace('_test.dat','')
    pos=el.replace('BPH.','').replace('BPV.','').replace('_test.dat','')
    outf.write(str(HV)+' '+name+' '+pos+' ')  
    d=f.readlines()
    for line in d:
        dat=line.split()[HV*2+1]
        outf.write(str(dat)+' ')
    outf.write('\n')
    f.close()
outf.close()
