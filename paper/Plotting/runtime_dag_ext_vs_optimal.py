import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pickle

fi= open('runtime_dag_ext_vs_optimal')
opt=[]
dex=[]
xAxis=[]

count=0
for line in fi:
	sp= line.split(' ')
	print(sp)
	if(count%2 == 0 ):
		opt.append(float(sp[-1]))
	else:
		dex.append(float(sp[-1]))

	
	if(count%2==0):
		chars = list(sp[0])
		num=''
		if(ord(chars[-1])- ord('0') < 9 and ord(chars[-1])- ord('0') >=0 ):
			num= chars[-1]
			if(ord(chars[-3])- ord('0') < 9 and ord(chars[-3])- ord('0') >=0 ):
				num= chars[-3] + '.' + num
		else:
			num=chars[-2]
			if(ord(chars[-4])- ord('0') < 9 and ord(chars[-4])- ord('0') >=0 ):
				num= chars[-4] + '.' + num

		
		xAxis.append(float(num))


		
	count+=1

choose = [0,1,3,5,7,9,11,13,15]
opt = [opt[i] for i in choose]
dex = [dex[i] for i in choose]
xAxis = [xAxis[i] for i in choose]

print(opt)
print(dex)
print(xAxis)


opt = [x/1e6 for x in opt]
dex = [x/1e6 for x in dex]


matplotlib.rcParams.update({'font.size': 20})

fig = plt.figure(figsize=(4,5))
plt.semilogy(xAxis,opt,label=r'Optimal', linestyle='solid', color='#000000', marker='*',linewidth=5.0, markersize=16)
plt.semilogy(xAxis,dex,label=r'SHARE', linestyle='solid', color='#56B4E9', marker='s',linewidth=5.0, markersize=12)
plt.xlabel("Path length (km)" , fontsize=20)
plt.ylabel("Running time (sec)" , fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.tick_params(axis='both', which='minor', labelsize=20)
# plt.ylim((0,100))
plt.legend(loc = 0)
# plt.title('Running Time comparison of Optimal and DAG Extended algorithms\n')
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
# plt.savefig('dag.eps',bbox_inches='tight')
plt.savefig('runtime_dag_ext_vs_optimal.pdf',bbox_inches='tight',pad_inches=-0.01)
# plt.show()

