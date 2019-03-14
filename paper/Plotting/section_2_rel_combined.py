import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os
import copy

enumx = ['alpha']
enumy = ['ridesharing_pct','avg_waiting_time','avg_passenger_per_km']

path = './Section_2/'


for ex in enumx:
	for ey in enumy:
		f=open(path+'NY_'+ex+'_'+ey,"r")

		xa = []
		pxa = []
		dex = []
		f.readline()
		for line in f:
			p=line.strip().split(",")
			try:
				xval = float(p[0])
			except ValueError:
				xval = p[0]
			xa.append(xval)
			pxa.append(float(p[1]))
			dex.append(float(p[2]))

		if ey.find('ridesharing_pct') != -1:
			pcprdex = [((100-y)-(100-x))/(100-x)*100 if y > 0 else 0 for x, y in zip(dex, pxa)]
			# rdex = [(y-x)/y*100 if y > 0 else 0 for x, y in zip(dex, pxa)]
		elif ey.find('avg_waiting_time') != -1:
			awtrdex = [(y-x)/x*100 if y > 0 else 0 for x, y in zip(dex, pxa)]
		elif ey.find('avg_passenger_per_km') != -1:
			apkrdex = [(x-y)/x*100 if y > 0 else 0 for x, y in zip(dex, pxa)]

	print(ex+'_'+ey)
	print(pcprdex)
	print(awtrdex)
	print(apkrdex)

	if ex.find('alpha') != -1:
		xlbl = r'$\alpha$'
		xa = xa[:-1]
		pcprdex = pcprdex[:-1]
		awtrdex = awtrdex[:-1]
		apkrdex = apkrdex[:-1]
		xbin = 5	
	elif ex.find('no_of_cabs') != -1:
		xlbl = '# cabs'
		xbin = 5
	elif ex.find('start_time') != -1:
		xlbl = 'Start Time'
		xbin = 3

	ylbl = 'Improvement (%)'

	matplotlib.rcParams.update({'font.size': 20})

	fig = plt.figure(figsize=(6.5,5))
	plt.plot(xa,pcprdex,label=r'Orders w/o ridesharing', linestyle='solid', color='#D55E00',marker='*', linewidth=5.0, markersize=16)
	plt.plot(xa,awtrdex,label=r'Waiting Time', linestyle='solid', color='#CC79A7', marker='s',fillstyle='none',linewidth=5.0, markersize=12)
	plt.plot(xa,apkrdex,label=r'Passenger / km', linestyle='solid', color='#0072B2', marker='X',linewidth=5.0, markersize=16)
	plt.xlabel(xlbl , fontsize=20)
	plt.ylabel(ylbl , fontsize=20)
	plt.tick_params(axis='both', which='major', labelsize=20)
	plt.tick_params(axis='both', which='minor', labelsize=20)
	plt.locator_params(axis='x', nbins=xbin)
	# plt.ylim((0,100))
	# plt.ylim(top=100)
	plt.legend(loc = 0)
	# plt.legend(loc='lower center', bbox_to_anchor=(0.5, 0.95))
	plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
	# plt.savefig('dag.eps',bbox_inches='tight')
	plt.savefig('NY_'+ex+'_paware.pdf',bbox_inches='tight',pad_inches=-0.01)
	# plt.show()
