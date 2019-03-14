import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pickle

xa = [0.0, 0.1, 0.2, 0.3, 0.5, 0.8]
ya2 = [20.28, 19.11, 13.35, 6.97, 4.98, 4.97]

ya3 = [25.5,23.9,18.26,9.89,6.34,6.04]
ya3 = [(100-x)/100 for x in ya3]

matplotlib.rcParams.update({'font.size': 18})

fig = plt.figure(figsize=(4,5))
plt.plot(xa,ya3,label=r'San Francisco', linestyle='solid', color='#56B4E9', marker='s',linewidth=5.0, markersize=12)
plt.xlabel(r"$\epsilon$ (km)" , fontsize=20)
plt.ylabel("Approximation ratio" , fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.tick_params(axis='both', which='minor', labelsize=20)
plt.locator_params(axis='x', nbins=5)
plt.ylim((0,1))
plt.legend(loc = 0)
# plt.title('%age loss on using DAG Extension algorithm')
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
# plt.savefig('dag.eps',bbox_inches='tight')
plt.savefig('score_dag_ext_vs_optimal.pdf',bbox_inches='tight',pad_inches=-0.01)
# plt.show()
