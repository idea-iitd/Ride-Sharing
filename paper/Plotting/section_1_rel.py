import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os
import copy

enumx = ['alpha','no_of_cabs','start_time']
enumy = ['ridesharing_pct','avg_waiting_time','avg_passenger_per_km']

path = './Section_1/'

for ey in enumy:
	for ex in enumx:
		for loc in ['NY','SG']:
			f=open(path+loc+'_'+ex+'_'+ey,"r")

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

			if ey.find('ridesharing_pct') != -1:
				# (SP - SHARE) / SHARE
				# SP = 100-y; SHARE = 100-x;
				rdag = [((100-y)-(100-x))/(100-x)*100 if y > 0 else 0 for x, y in zip(dag, dij)]
				rdex = [((100-y)-(100-x))/(100-x)*100 if y > 0 else 0 for x, y in zip(dex, dij)]
			elif ey.find('avg_waiting_time') != -1:
				# (SP - SHARE) / SHARE
				rdag = [(y-x)/x*100 if y > 0 else 0 for x, y in zip(dag, dij)]
				rdex = [(y-x)/x*100 if y > 0 else 0 for x, y in zip(dex, dij)]
			elif ey.find('avg_passenger_per_km') != -1:
				# (SHARE - SP) / SHARE
				rdag = [(x-y)/x*100 if y > 0 else 0 for x, y in zip(dag, dij)]
				rdex = [(x-y)/x*100 if y > 0 else 0 for x, y in zip(dex, dij)]

			if loc == 'NY':
				nyrdag = copy.deepcopy(rdag)
				nyrdex = copy.deepcopy(rdex)
			else:
				sgrdag = copy.deepcopy(rdag)
				sgrdex = copy.deepcopy(rdex)


		if ex.find('alpha') != -1:
			xlbl = r'$\alpha$'
			xa = xa[:-1]
			nyrdag = nyrdag[:-1]
			nyrdex = nyrdex[:-1]
			sgrdag = sgrdag[:-1]
			sgrdex = sgrdex[:-1]
			xbin = 5
		elif ex.find('no_of_cabs') != -1:
			xlbl = '# taxis'
			xbin = 5
		elif ex.find('start_time') != -1:
			xlbl = 'Start Time'
			xbin = 3

		# if ey.find('avg_passenger_per_km') != -1:
		# 	ylbl = r'$\Delta$ Avg passenger / km (%)'
		# elif ey.find('avg_waiting_time') != -1:
		# 	ylbl = r'Avg wait time (%)'
		# elif ey.find('ridesharing_pct') != -1:
		# 	ylbl = r'Order w/o Ridesharing (%)'

		ylbl = 'Improvement (%)'

		matplotlib.rcParams.update({'font.size': 20})

		fig = plt.figure(figsize=(5,5))
		plt.plot(xa,nyrdex,label=r'NY', linestyle='solid', color = '#009E73', marker='D', linewidth=5.0, markersize=12)
		plt.plot(xa,sgrdex,label=r'SG', linestyle='solid', color = '#E69F00', marker='o', fillstyle='none', linewidth=5.0, markersize=16)
		plt.xlabel(xlbl , fontsize=20)
		plt.ylabel(ylbl , fontsize=20)
		plt.tick_params(axis='both', which='major', labelsize=20)
		plt.tick_params(axis='both', which='minor', labelsize=20)
		plt.locator_params(axis='x', nbins=xbin)
		if max(nyrdex+sgrdex) < 20:
			plt.ylim((0,20))
		plt.ylim(bottom=0)
		plt.legend(loc = 0)
		plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
		# plt.savefig('dag.eps',bbox_inches='tight')
		plt.savefig(ex+'_'+ey+'.pdf',bbox_inches='tight',pad_inches=-0.01)
		# plt.show()
