import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 172, 173, 174, 175, 176, 178, 181, 183, 184, 185, 186, 187, 188, 189, 190, 192, 193, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 214, 215, 216, 218, 219, 220, 223, 226, 228, 229, 230, 231, 232, 235, 238, 243, 244, 245, 247, 249, 252, 254, 255, 259, 261, 277, 281, 314]

for i in range(len(numbers)):
    data = np.genfromtxt('Zubko_' + str(numbers[i]) + '_i90_sed.dat', names = ['wave','flux'], skip_header=2)
    data2 = np.genfromtxt('nodust_' + str(numbers[i]) + '_i90_sed.dat', names = ['wave','flux'], skip_header=2)
    
    #Plot the SED
    plt.loglog(data['wave'], data['flux'], label = 'Scattered emission')
    plt.loglog(data2['wave'],data2['flux'], label = 'Non-scattered emission')
    plt.legend(loc = 3)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/1945/figures/SED_' + str(numbers[i]) + '.png')
    plt.close()
    
    #Plot the 2175 angstrom bump
    data3 = -2.5*np.log(data['flux']/data2['flux'])
    plt.plot(1/data['wave'], data3)
    plt.xlim(0,10)
    #plt.ylim(-1,1)
    plt.axvline(x=4.59770114943, label = '2175' + r'$\AA$')
    plt.xlabel('1/'+r'$\lambda$ ' + '[1/'+r'$\mu$m'+']')
    plt.ylabel('Attenuation')# + r'$\lambda*F_\lambda$' + ' ' + '(W/m2)')
    plt.legend(loc = 4)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/1945/figures/2175_' + str(numbers[i]) + '.png')
    plt.close()
    #difficult to do automatically, since the bump is so small and you need to be able to move in by eye

#plt.plot(data['wave'], data['flux'], label = 'Scattered emission')
#plt.plot(data2['wave'],data2['flux'], label = 'Non-scattered emission')
#plt.xlabel(r'$\lambda$' + ' ' + r'$\mu$m')
#plt.ylabel('Total flux' + ' ' + r'$\lambda*F_\lambda$' + ' ' + '(W/m2)')
#plt.legend(loc='lower left')
#plt.savefig('linear.png')

#B = np.log(data['flux']/data2['flux'])
#C = np.log(data['flux'][1142]/data2['flux'][1142])
#attenuation = B/C
#plt.plot(1/data['wave'], A)

