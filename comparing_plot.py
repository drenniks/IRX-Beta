import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Data
skirt_data = np.genfromtxt('skirt_data_angles_final.dat', names = ['halo', 'angle', 'IRX', 'beta', 'neg_ebeta', 'pos_ebeta', 'intercept', 'neg_eint', 'pos_eint'])
compare_data = np.genfromtxt('BF_IRXBdata_comparison.dat', names = ['IRX', 'e_IRX', 'beta', 'e_beta'], skip_header = 11)

#Comparing data with BF
beta = np.linspace(-3,3, 100)
IRX = np.arange(-10, 8, 0.1)
y = np.log10(10**(0.4*(5.05 + 2.39*beta)) - 1) + np.log10(1.68)
plt.plot(beta, y, label ='Fit from Forrest et al')
plt.scatter(skirt_data['beta'], np.log10(skirt_data['IRX']), marker = 'o', c = 'r', label = 'Romulus')
plt.scatter(compare_data['beta'], np.log10(compare_data['IRX']), marker = '*', c = 'green', s = 50, label = 'Forrest et al')
plt.axhline(y = 0, c = 'black', ls = 'dashed')
plt.xlim(-2.5,3.0)
plt.ylim(-4, 5)
plt.legend(loc = 2)
plt.xlabel(r'$\beta$')
plt.ylabel('IRX')
plt.savefig('comparison.png')
plt.close()

#IRX vs. beta (angles)
plt.scatter(compare_data['beta'], np.log10(compare_data['IRX']), marker = '*', c = 'green', s = 50, label = 'Forrest et al')
for i in skirt_data:
    if skirt_data['angle'][i] == 0.0:
        plt.scatter(skirt_data['beta'][i], np.log10(skirt_data['IRX'][i]), marker = 'o', c = 'red')
    elif skirt_data['angle'][i] == 90.0:
        plt.scatter(skirt_data['beta'][i], np.log10(skirt_data['IRX'][i]), marker = 'o', c = 'blue')
    elif skirt_data['angle'][i] == 135.0:
        plt.scatter(skirt_data['beta'][i], np.log10(skirt_data['IRX'][i]), marker = 'o', c = 'black')
    elif skirt_data['angle'][i] == 225.0:
        plt.scatter(skirt_data['beta'][i], np.log10(skirt_data['IRX'][i]), marker = 'o', c = 'cyan')
plt.axhline(y = 0, c = 'black', ls = 'dashed')
plt.xlim(-2.5,3.0)
#plt.ylim(-2.5, 8)
plt.gca().set_ylim(top=4)
red = matplotlib.lines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="red")
blue = matplotlib.lines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="blue")
black = matplotlib.lines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="black")
cyan = matplotlib.lines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="cyan")
green = matplotlib.lines.Line2D(range(1), range(1), color = "white", marker = '*', markerfacecolor="green")
plt.legend((red, blue, black, cyan, green), ('0.0 deg', '90.0 deg', '135.0 deg', '225.0 deg', 'Forrest et al'), numpoints=1, loc = 'lower right')
plt.xlabel(r'$\beta$')
plt.ylabel('IRX')
plt.savefig('angles_IRXbeta.png')
