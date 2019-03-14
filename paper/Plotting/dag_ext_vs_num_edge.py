import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os
import copy

enumx = ['dag_ext']
enumy = ['num_edge']

path = './'

for ey in enumy:
	for ex in enumx:
		for loc in ['NY','SG']:
			f=open(path+loc+'_'+ex+'_vs_'+ey,"r")

			xa = []
			val = []
			f.readline()
			for line in f:
				p=line.strip().split(",")
				try:
					xval = float(p[0])
				except ValueError:
					xval = p[0]
				xa.append(xval)
				val.append(int(p[2])/int(p[1]))

			if loc == 'NY':
				nyval = copy.deepcopy(val)
			else:
				sgval = copy.deepcopy(val)

		print(ex+'_'+ey)
		print(nyval)
		print(sgval)

		if ex.find('dag_ext') != -1:
			xlbl = r'$\epsilon$ (km)'
			xbin = 5
		
		if ey.find('num_edge') != -1:
			ylbl = r'# of edges in $E_X$'

		matplotlib.rcParams.update({'font.size': 20})

		fig = plt.figure(figsize=(4,5))
		plt.plot(xa,nyval,label=r'NY', linestyle='solid', color = '#009E73', marker='D', linewidth=5.0, markersize=12)
		plt.plot(xa,sgval,label=r'SG', linestyle='solid', color = '#E69F00', marker='o', fillstyle='none', linewidth=5.0, markersize=16)
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
