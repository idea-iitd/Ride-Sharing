import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os

path = './Section_1/'
listing = os.listdir(path)
print(listing)
print()

for infile in listing:
	f=open(path+infile,"r")
	xa = []
	dij = []
	dag = []
	dex = []
	f.readline()
	for line in f:
		p=line.strip().split(",")
		try:
			xval = float(p[0])
		except ValueError:
			xval = p[0]
		xa.append(xval)
		dij.append(float(p[1]))
		dag.append(float(p[2]))
		dex.append(float(p[3]))

	print(infile)
	print(xa)
	print(dij)
	print(dag)
	print(dex)

	if infile.find('alpha') != -1:
		xlbl = r'$\alpha$'
		xbin = 6
	elif infile.find('no_of_cabs') != -1:
		xlbl = '# cabs'
		xbin = 5
	elif infile.find('start_time') != -1:
		xlbl = 'Start Time'
		xbin = 3

	if infile.find('avg_passenger_per_km') != -1:
		ylbl = 'Avg passenger / km'
	elif infile.find('avg_waiting_time') != -1:
		ylbl = 'Avg waiting time (min)'
	elif infile.find('ridesharing_pct') != -1:
		ylbl = 'Order w/Ridesharing (%)'

	
	matplotlib.rcParams.update({'font.size': 20})

	fig = plt.figure(figsize=(5,5))
	plt.plot(xa,dij,label=r'SP', linestyle='solid', marker='*',linewidth=5.0, markersize=12)
	plt.plot(xa,dag,label=r'SHARE', linestyle='solid', color = 'tab:orange', marker='o',linewidth=5.0, markersize=12)
	plt.plot(xa,dex,label=r'SHARE-X', linestyle='solid', color = 'tab:green', marker='s',linewidth=5.0, markersize=12)
	plt.xlabel(xlbl , fontsize=20)
	plt.ylabel(ylbl , fontsize=20)
	plt.tick_params(axis='both', which='major', labelsize=20)
	plt.tick_params(axis='both', which='minor', labelsize=20)
	plt.locator_params(axis='x', nbins=xbin)
	# plt.ylim((0,100))
	plt.legend(loc = 0)
	plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
	# plt.savefig('dag.eps',bbox_inches='tight')
	plt.savefig(infile+'.pdf',bbox_inches='tight',pad_inches=-0.01)
	# plt.show()
