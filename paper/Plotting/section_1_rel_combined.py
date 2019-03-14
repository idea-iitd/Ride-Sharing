import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os

enumx = ['alpha','no_of_cabs','start_time']
enumy = ['ridesharing_pct','avg_waiting_time','avg_passenger_per_km']

path = './Section_1/'

plot_cnt = 1
fig = plt.figure(figsize=(21,18))

for ey in enumy:
	for ex in enumx:
		f=open(path+'NY_'+ex+'_'+ey,"r")
	
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
			nyrdag = [(100-x)/(100-y)*100-100 if y > 0 else 0 for x, y in zip(dag, dij)]
			nyrdex = [(100-x)/(100-y)*100-100 if y > 0 else 0 for x, y in zip(dex, dij)]	
		else:
			nyrdag = [x/y*100-100 if y > 0 else 0 for x, y in zip(dag, dij)]
			nyrdex = [x/y*100-100 if y > 0 else 0 for x, y in zip(dex, dij)]

		f=open(path+'SG_'+ex+'_'+ey,"r")

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
			sgrdag = [(100-x)/(100-y)*100-100 if y > 0 else 0 for x, y in zip(dag, dij)]
			sgrdex = [(100-x)/(100-y)*100-100 if y > 0 else 0 for x, y in zip(dex, dij)]	
		else:
			sgrdag = [x/y*100-100 if y > 0 else 0 for x, y in zip(dag, dij)]
			sgrdex = [x/y*100-100 if y > 0 else 0 for x, y in zip(dex, dij)]


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
			ylbl = r'$\Delta$ Avg wait time (%)'
		elif ey.find('ridesharing_pct') != -1:
			ylbl = r'$\Delta$ Order w/o Ridesharing (%)'
		
		matplotlib.rcParams.update({'font.size': 26})

		# fig = plt.figure(figsize=(5,5))

		plt.subplot(3,3,plot_cnt)

		plt.plot(xa,nyrdag,label=r'NY SHARE / SP', linestyle='solid', color = 'tab:orange', marker='o',linewidth=8.0, markersize=16)
		plt.plot(xa,nyrdex,label=r'NY SHARE-X / SP', linestyle='solid', color = 'tab:green', marker='s',linewidth=8.0, markersize=16)
		plt.plot(xa,sgrdag,label=r'SG SHARE / SP', linestyle='solid', color = 'tab:red', marker='o',linewidth=8.0, markersize=16)
		plt.plot(xa,sgrdex,label=r'SG SHARE-X / SP', linestyle='solid', color = 'tab:purple', marker='s',linewidth=8.0, markersize=16)
		plt.xlabel(xlbl , fontsize=26)
		if plot_cnt % 3 == 1:
			plt.ylabel(ylbl , fontsize=26)
		plt.tick_params(axis='both', which='major', labelsize=26)
		plt.tick_params(axis='both', which='minor', labelsize=26)
		plt.locator_params(axis='x', nbins=xbin)
		# plt.ylim((0,100))
		if plot_cnt <= 6:
			plt.ylim(top=0)
		else:
			plt.ylim(bottom=0)
		if plot_cnt == 8:
			plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

		# plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
		# plt.savefig('dag.eps',bbox_inches='tight')
		# plt.savefig(infile+'.pdf',bbox_inches='tight',pad_inches=-0.01)
		# plt.show()

		plot_cnt += 1

		# break

plt.savefig('section_1_relative.pdf',bbox_inches='tight',pad_inches=-0.01)
# plt.show()