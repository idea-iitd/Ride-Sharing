import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle
import os
import copy

enumx = ['alpha','extension']
enumy = ['Avg waiting time (min)','Avg passenger per km', 'Orders with ridesharing (%)']

# Alpha,Only Dex,TimeVarying,TimeVaryingDecay,BasicDexDecay,DexCluster

path = './AlgorithmsCompared/'

for ey in enumy:
	for loc in ['NY', 'SG']:
		f=open(path+loc+'_alpha_'+ey,"r")

		xa = []
		# val = []
		Share= []
		ShareExp=[]
		ShareTime=[]
		ShareCls=[]

		f.readline()
		for line in f:
			p=line.strip().split(",")
			try:
				xval = float(p[0])
			except ValueError:
				xval = p[0]
			xa.append(xval)
			Share.append(float(p[1]))
			ShareExp.append(float(p[4]))
			ShareTime.append(float(p[2]))
			ShareCls.append(float(p[5]))
			# val.append(float(p[1]))

		# if loc == 'NY':
		# 	nyval = copy.deepcopy(val)
		# else:
		# 	sgval = copy.deepcopy(val)

		print(ey)
		print(Share)
		print(ShareExp)
		print(ShareTime)
		print(ShareCls)

		# exit()


		# elif ex.find('extension') != -1:
		xlbl = r'$\alpha$'
		xa = xa[:-1]
		Share = Share[:-1]
		ShareTime = ShareTime[:-1]
		ShareExp = ShareExp[:-1]
		ShareCls = ShareCls[:-1]
		xbin = 5
		
		if ey.find('Avg passenger per km') != -1:
			ylbl = r'Passengers / km'
			fname = 'avg_passenger_per_km'
		elif ey.find('Avg waiting time (min)') != -1:
			ylbl = r'Waiting time (min)'
			fname = 'avg_waiting_time'
		elif ey.find('Orders with ridesharing (%)') != -1:
			ylbl = r'Order w/o Ridesharing (%)'
			Share = [100-x for x in Share]
			ShareTime = [100-x for x in ShareTime]
			ShareExp = [100-x for x in ShareExp]
			ShareCls = [100-x for x in ShareCls]
			fname = 'order_with_ridesharing'

		matplotlib.rcParams.update({'font.size': 15})

		fig = plt.figure(figsize=(4,5))
		if loc == 'NY':
			plt.plot(xa,Share,label=r'SHARE', linestyle='solid', color = '#009E73', marker='D', linewidth=3.0, markersize=12)
			plt.plot(xa,ShareTime,label=r'SHARE+Time', linestyle='solid', color = '#0D4F9E', marker='^', fillstyle='none', linewidth=3.0, markersize=12)
			plt.plot(xa,ShareExp,label=r'SHARE+Exp', linestyle='solid', color = '#873100', marker='v', fillstyle='none', linewidth=3.0, markersize=12)
			plt.plot(xa,ShareCls,label=r'SHARE+Reg', linestyle='solid', color = '#F1E400', marker='s', fillstyle='none', linewidth=3.0, markersize=12)
		else:
			plt.plot(xa,Share,label=r'SHARE', linestyle='solid', color = '#E69F00', marker='o', fillstyle='none', linewidth=3.0, markersize=16)
			plt.plot(xa,ShareTime,label=r'SHARE+Time', linestyle='solid', color = '#0D4F9E', marker='^', fillstyle='none', linewidth=3.0, markersize=12)
			plt.plot(xa,ShareExp,label=r'SHARE+Exp', linestyle='solid', color = '#873100', marker='v', fillstyle='none', linewidth=3.0, markersize=12)
			plt.plot(xa,ShareCls,label=r'SHARE+Reg', linestyle='solid', color = '#F1E400', marker='s', fillstyle='none', linewidth=3.0, markersize=12)
		
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
		plt.savefig(loc+'_'+fname+'.pdf',bbox_inches='tight',pad_inches=-0.01)
		# plt.show()
