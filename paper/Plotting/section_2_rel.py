import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os
import copy

enumx = ['alpha']
enumy = ['ridesharing_pct','avg_waiting_time','avg_passenger_per_km']

path = './Section_2/'

for ey in enumy:
	for ex in enumx:
		for loc in ['NY','SG']:
			f=open(path+loc+'_'+ex+'_'+ey,"r")

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
				rdex = [(x-y)/(100-y)*100 if y > 0 else 0 for x, y in zip(dex, pxa)]
				# rdex = [(y-x)/y*100 if y > 0 else 0 for x, y in zip(dex, pxa)]
			elif ey.find('avg_waiting_time') != -1:
				rdex = [(y-x)/y*100 if y > 0 else 0 for x, y in zip(dex, pxa)]
			elif ey.find('avg_passenger_per_km') != -1:
				rdex = [(x-y)/y*100 if y > 0 else 0 for x, y in zip(dex, pxa)]

			if loc == 'NY':
				nyrdex = copy.deepcopy(rdex)
			else:
				sgrdex = copy.deepcopy(rdex)

		print(ex+'_'+ey)
		print(nyrdex)
		print(sgrdex)

		if ex.find('alpha') != -1:
			xlbl = r'$\alpha$'
			xbin = 6
		elif ex.find('no_of_cabs') != -1:
			xlbl = '# cabs'
			xbin = 5
		elif ex.find('start_time') != -1:
			xlbl = 'Start Time'
			xbin = 3

		if ey.find('avg_passenger_per_km') != -1:
			ylbl = r'$\Delta$ Avg passenger / km (%)'
		elif ey.find('avg_waiting_time') != -1:
			ylbl = r'Avg wait time (%)'
		elif ey.find('ridesharing_pct') != -1:
			ylbl = r'Order w/o Ridesharing (%)'
			# ylbl = r'Order w/ Ridesharing (%)'

		matplotlib.rcParams.update({'font.size': 20})

		fig = plt.figure(figsize=(5,5))
		if ey.find('ridesharing_pct') != -1:
			plt.yscale('symlog')
		plt.plot(xa,nyrdex,label=r'NY', linestyle='solid', color = 'tab:green', marker='s',linewidth=5.0, markersize=12)
		plt.plot(xa,sgrdex,label=r'SG', linestyle='solid', color = 'tab:purple', marker='s',linewidth=5.0, markersize=12)
		plt.xlabel(xlbl , fontsize=20)
		plt.ylabel(ylbl , fontsize=20)
		plt.tick_params(axis='both', which='major', labelsize=20)
		plt.tick_params(axis='both', which='minor', labelsize=20)
		plt.locator_params(axis='x', nbins=xbin)
		# plt.ylim((0,100))
		# plt.ylim(bottom=0)
		plt.legend(loc = 0)
		plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
		# plt.savefig('dag.eps',bbox_inches='tight')
		plt.savefig(ex+'_'+ey+'.pdf',bbox_inches='tight',pad_inches=-0.01)
		# plt.show()
