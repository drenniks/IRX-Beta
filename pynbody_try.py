import matplotlib
matplotlib.use('Agg')
import numpy as np
import pynbody
import matplotlib.pylab as plt
import gc

#Z=4
below_posb = [132, 134, 69, 153, 53]
below_medb = [25, 253, 57, 177, 58, 82, 219, 15, 99]
below_negb = [418, 322, 296, 210, 198, 179, 115, 194, 272, 317, 310, 297, 325, 225, 32,355, 209, 206, 152, 155, 291, 46, 201, 245] #deleted 369 (I think it was a mistype)
below_zero = [280, 299, 446, 289, 246, 262, 17, 282, 398, 8, 295, 304, 281, 256, 341, 343, 313, 331, 241, 389, 313, 293, 334, 352]
above_posb = [76, 138, 278, 137, 151, 63, 168, 70, 305, 64, 73, 51, 45, 146, 112, 161, 102]
on_line = [270, 67, 232, 186, 234, 283, 43, 128, 87, 24, 218, 3, 5, 30, 166, 98, 22, 140, 149, 154, 27, 93]
numbers = [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177,178, 179, 180, 181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 272, 273, 275, 276, 277, 278, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 302, 303, 304, 305, 308, 310, 311, 313, 315, 316, 317, 318, 321, 322, 324, 325, 328, 331, 332, 333, 334, 335, 336, 339, 340, 341, 343, 346, 352, 355, 356, 363, 364, 366, 372, 373, 380, 387, 389, 394, 398, 410, 418, 446]

s = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.001945')
s.physical_units()
halos = s.halos(dosort=True)
data =  np.genfromtxt('skirt_data_angles.dat', names = ['halo', 'IRX', 'beta', 'neg_ebeta', 'pos_ebeta', 'intercept', 'neg_eint', 'pos_eint'])
compare_data = np.genfromtxt('BF_IRXBdata_comparison.dat', names = ['IRX', 'e_IRX', 'beta', 'e_beta'], skip_header =11)
B = np.linspace(-2.5, 2.5, 100)
y = np.log10(10**(0.4*(5.05 + 2.39*B)) - 1) + np.log10(1.68)
beta = data['beta']
IRX = np.log10(data['IRX'])
c_beta = compare_data['beta']
c_IRX = np.log10(compare_data['IRX'])

for i in below_posb:
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)
    
    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()
    
    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_stars.png')
    plt.clf()
    
    del hn
    gc.collect()
    
    #Plot the relationship and highlight outlier
    fig, ax = plt.subplots()
    plt.scatter(beta, IRX, s = 50)
    plt.plot(B,y, label = 'Fit from Forrest et al')
    plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
    x = data[data['halo'] == i]['beta']
    v = data[data['halo'] == i]['IRX']
    plt.scatter(x, np.log10(v), s = 50, c = 'red')
    ax.annotate(str(i), (x, np.log10(v)))
    plt.xlabel(r'$\beta$')
    plt.ylabel(r'log$_{10}$(IRX)')
    #plt.xlim(-2.5, 2.5)
    plt.ylim(-6.5,6)
    plt.title('z_2')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()

for i in below_medb:
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)

    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_stars.png')
    plt.clf()

    del hn
    gc.collect()
    
    #Plot the relationship and highlight outlier
    fig, ax = plt.subplots()
    plt.scatter(beta, IRX, s = 50)
    plt.plot(B,y, label = 'Fit from Forrest et al')
    plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
    x = data[data['halo'] == i]['beta']
    v = data[data['halo'] == i]['IRX']
    plt.scatter(x, np.log10(v), s = 50, c = 'red')
    ax.annotate(str(i), (x, np.log10(v)))
    plt.xlabel(r'$\beta$')
    plt.ylabel(r'log$_{10}$(IRX)')
    #plt.xlim(-2.5, 2.5)
    plt.ylim(-6.5,6)
    plt.title('z_2')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()


for i in below_negb:
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)
    print 'hn = ', hn
    print 'halos.load_copy(',i,') = ', halos.load_copy(i)
    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_stars.png')
    plt.clf()

    del hn
    gc.collect()
    
    #Plot the relationship and highlight outlier
    fig, ax = plt.subplots()
    plt.scatter(beta, IRX, s = 50)
    plt.plot(B,y, label = 'Fit from Forrest et al')
    plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
    x = data[data['halo'] == i]['beta']
    v = data[data['halo'] == i]['IRX']
    plt.scatter(x, np.log10(v), s = 50, c = 'red')
    ax.annotate(str(i), (x, np.log10(v)))
    plt.xlabel(r'$\beta$')
    plt.ylabel(r'log$_{10}$(IRX)')
    print 'halo = ', i
    print 'x = ', x
    print 'v = ', v
    
    #plt.xlim(-2.5, 2.5)
    plt.ylim(-6.5,6)
    plt.title('z_2')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()

for i in below_zero:
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)

    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_stars.png')
    plt.clf()

    del hn
    gc.collect()
    
    #Plot the relationship and highlight outlier
    fig, ax = plt.subplots()
    plt.scatter(beta, IRX, s = 50)
    plt.plot(B,y, label = 'Fit from Forrest et al')
    plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
    x = data[data['halo'] == i]['beta']
    v = data[data['halo'] == i]['IRX']
    plt.scatter(x, np.log10(v), s = 50, c = 'red')
    ax.annotate(str(i), (x, np.log10(v)))
    plt.xlabel(r'$\beta$')
    plt.ylabel(r'log$_{10}$(IRX)')
    #plt.xlim(-2.5, 2.5)
    plt.ylim(-6.5,6)
    plt.title('z_2')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()

for i in above_posb:
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)

    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_stars.png')
    plt.clf()

    del hn
    gc.collect()
    
    #Plot the relationship and highlight outlier
    fig, ax = plt.subplots()
    plt.scatter(beta, IRX, s = 50)
    plt.plot(B,y, label = 'Fit from Forrest et al')
    plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
    x = data[data['halo'] == i]['beta']
    v = data[data['halo'] == i]['IRX']
    plt.scatter(x, np.log10(v), s = 50, c = 'red')
    ax.annotate(str(i), (x, np.log10(v)))
    plt.xlabel(r'$\beta$')
    plt.ylabel(r'log$_{10}$(IRX)')
    #plt.xlim(-2.5, 2.5)
    plt.ylim(-6.5,6)
    plt.title('z_2')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()

for i in on_line:
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)

    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_stars.png')
    plt.clf()

    del hn
    gc.collect()
    
    #Plot the relationship and highlight outlier
    fig, ax = plt.subplots()
    plt.scatter(beta, IRX, s = 50)
    plt.plot(B,y, label = 'Fit from Forrest et al')
    plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
    x = data[data['halo'] == i]['beta']
    v = data[data['halo'] == i]['IRX']
    plt.scatter(x, np.log10(v), s = 50, c = 'red')
    ax.annotate(str(i), (x, np.log10(v)))
    plt.xlabel(r'$\beta$')
    plt.ylabel(r'log$_{10}$(IRX)')
    #plt.xlim(-2.5, 2.5)
    plt.ylim(-6.5,6)
    plt.title('z_2')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_4/test/final_plots/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()
