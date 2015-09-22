#python

from metaclass25 import twiss
from numpy import array, zeros, arange
from pylab import plot, show
## Dati del quadrupolo QD 60710


px_base=array(twiss('bph.base').MUX)
px_pert=array(twiss('bph.dat').MUX)
py_base=array(twiss('bpv.base').MUY)
py_pert=array(twiss('bpv.dat').MUY)
names=twiss('bph.base').NAME


print "\n Data read from twiss.base and twiss.dat \n"

dpx=zeros((1,len(px_base)),float)
print len(px_base)
print dpx[0,1]
dpy=zeros((1,len(py_base)),float)

for i in range(1,len(px_base)-2):
 print i
 dpx[0,i]=px_pert[i+1]-px_pert[i]-px_base[i+1]+px_base[i];

for i in range(0,len(py_base)-2):
 dpy[0,i]=py_pert[i+1]-py_pert[i]-py_base[i+1]+py_base[i];

f=open('dpx.dat','w')
for el in dpx:
 f.write(str(el)+"\n");
f.close()


f=open('dpy.dat','w')
for line in dpy:
	for el in line:
 	 f.write(str(el)+"\n");
f.close()

plot(arange(1,len(dpx)-1),dpx);
plot(arange(1,len(dpy)-1),dpy);
show();



