import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


skirt_data = np.genfromtxt('skirt_data.dat', names = ['halo', 'IRX', 'beta', '-ebeta', '+ebeta', 'intercept', '-eint', '+eint'])
compare_data = np.genfromtxt('BF_IRXBdata_comparison.dat', names = ['IRX', 'e_IRX', 'beta', 'e_beta'], skip_header = 11)
beta = np.linspace(-3,3, 100)
IRX = np.arange(-10, 8, 0.1)
y = np.log(10**(0.4*(5.05 + 2.39*beta)) - 1) + np.log(1.68)
plt.plot(beta, y, label ='Fit from Forrest et al')
plt.scatter(skirt_data['beta'], np.log(skirt_data['IRX']), marker = 'o', c = 'r', label = 'Romulus')
plt.scatter(compare_data['beta'], np.log(compare_data['IRX']), marker = '*', c = 'green', s = 50, label = 'Forrest et al')
plt.axhline(y = 0, c = 'black', ls = 'dashed')
plt.xlim(-2.5,3.0)
plt.ylim(-2.5, 8)
plt.legend(loc = 2)
plt.xlabel(r'$\beta$')
plt.ylabel('IRX')
plt.savefig('comparison.png')


#names = ['halo', 'IRX', 'beta', 'intercept']
#output = {}

#with open('skirt_data.dat') as sfd:
#    for i, line in enumerate(sfd.readlines()):
#        skirt_name = names[i]
#        first_col, second_col, third_col, fourth_col = line.split(' ')
#        output[skirt_name] = int(third_col[1])
#    print output
