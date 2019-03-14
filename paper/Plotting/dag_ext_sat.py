from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib
import itertools
from matplotlib import rc

#rc('font', **{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

#pp = PdfPages('memvslandmark.pdf')
matplotlib.rcParams.update({'font.size': 20})
# We change the fontsize of minor ticks label 
f=open("SF_trajectories_satisfy_dag_extension","r")
a=[]
b=[]
f.readline()
for line in f:
    p=line.strip().split(",")
    a.append(float(p[0]))
    b.append(float(p[1]))

fig = plt.figure(figsize=(6,5))
plt.plot(a,b,label=r'San Francisco', linestyle='solid', color='#56B4E9', marker='s',linewidth=5.0, markersize=12)
plt.ylabel(r"Covered Trajectories (%)",fontsize=20)
plt.xlabel(r"$\epsilon$ (km)",fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.tick_params(axis='both', which='minor', labelsize=20)
#plt.yscale('log')
plt.ylim((0,100))
plt.xlim((0,2))
plt.legend(loc=0)

plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
plt.savefig('dag_ext_sat.pdf',bbox_inches='tight',pad_inches=-0.01)
plt.show()
#pp.close()
