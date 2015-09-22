"""
sort by position
"""
import os

dir=os.getcwd()
for file in os.listdir(dir):
	if '.ph' in file:
		print int(file[-9:-4])
