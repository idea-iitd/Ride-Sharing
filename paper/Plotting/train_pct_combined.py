import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os
import copy

enumx = ['train_pct']
enumy = ['ridesharing_pct','avg_waiting_time','avg_passenger_per_km']

base = 2

path = './TrainPct/'

for ex in enumx:
	for loc in ['NY','SG']:
		for ey in enumy:
			f=open(path+loc+'_'+ex+'_vs_'+ey,"r")

			xa = []
			val = []
			f.readline()
			for line in f:
				p=line.strip().split(",")
				xval = p[0]
				xa.append(xval)
				val.append(float(p[1]))

			xa = xa[1:]
			if ey.find('ridesharing_pct') != -1:
				pcprdex = [((100-val[0])-(100-x))/(100-x)*100 for x in val[1:]]
				# rdex = [(y-x)/y*100 if y > 0 else 0 for x, y in zip(dex, pxa)]
			elif ey.find('avg_waiting_time') != -1:
				awtrdex = [(val[0]-x)/x*100 for x in val[1:]]
			elif ey.find('avg_passenger_per_km') != -1:
				apkrdex = [(x-val[0])/x*100 for x in val[1:]]

		
		print(ex+'_'+ey)
		print(pcprdex)
		print(awtrdex)
		print(apkrdex)

		if ex.find('train_pct') != -1:
			xlbl = r'Training data (%)'
			xbin = 3

		ylbl = 'Improvement (%)'

		matplotlib.rcParams.update({'font.size': 17})

		fig = plt.figure(figsize=(5.5,5))
		plt.plot(xa,pcprdex,label=r'Orders w/o ridesharing', linestyle='solid', color='#D55E00',marker='*', linewidth=5.0, markersize=16)
		plt.plot(xa,awtrdex,label=r'Waiting Time', linestyle='solid', color='#CC79A7', marker='s',fillstyle='none',linewidth=5.0, markersize=12)
		plt.plot(xa,apkrdex,label=r'Passenger / km', linestyle='solid', color='#0072B2', marker='X',linewidth=5.0, markersize=16)
		plt.xlabel(xlbl , fontsize=20)
		plt.ylabel(ylbl , fontsize=20)
		plt.tick_params(axis='both', which='major', labelsize=20)
		plt.tick_params(axis='both', which='minor', labelsize=20)
		plt.locator_params(axis='x', nbins=xbin)
		# if ey.find('running_time') != -1:
			# plt.ylim((0,0.5))
		# plt.ylim(bottom=0)
		plt.legend(loc = 0)
		plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
		# plt.savefig('dag.eps',bbox_inches='tight')
		plt.savefig(loc+'_'+ex+'.pdf',bbox_inches='tight',pad_inches=-0.01)
		# plt.show()
