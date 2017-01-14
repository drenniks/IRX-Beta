import matplotlib
matplotlib.use('Agg')
import numpy as np
import pynbody
import matplotlib.pylab as plt
import gc

below_posb = [18, 33,  35,  36,  45,  49,  57,  67,  68,  72,  80, 102, 124, 187]
below_negb = [30,  31,  43,  96, 105, 125, 135, 142, 147, 149, 160, 161, 169, 170, 180]
below_zero = [23,  70,  72,  80, 124, 127, 157, 159, 181, 194, 216]
above = [92, 104, 108, 152, 153, 158]
on_line = [27,  34,  38, 47,  48,  52,  63,  64,  66,  71,  79, 86,  87,  95, 103, 107, 117, 121, 122, 126, 133, 137, 138, 139, 141, 143, 151, 151, 155, 162, 167, 193, 214]
#removed 41 from on_line (insufficient particles around centre to get velocity)

s = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.008192')
s.physical_units()
halos = s.halos(dosort=True)
numbers =  [18, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 132, 133, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 186, 187, 188, 189, 190, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 213, 214, 215, 216]
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
    print i

    #Plot the gas density
    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()
    
    #Plot the stars
    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_stars.png')
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
    plt.title('z_0')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()

for i in below_negb:
    
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)
    print i

    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()
    
    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_stars.png')
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
    plt.title('z_0')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()
    
for i in below_zero:
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)
    print i

    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_stars.png')
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
    plt.title('z_0')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()

for i in above:
    
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)
    print i
    
    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_stars.png')
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
    plt.title('z_0')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()

for i in on_line:
    
    hn = halos.load_copy(i)
    pynbody.analysis.angmom.faceon(hn)
    print i
    pynbody.plot.image(hn.g, qty='rho', units='g cm^-3', width='40 kpc', cmap='Greys')
    plt.title('h'+str(i)+', gas.rho')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_grho.png')
    plt.clf()

    pynbody.plot.stars.render(hn, width='40 kpc')
    plt.title('h'+str(i)+', stars.png')
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_stars.png')
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
    plt.title('z_0')
    plt.legend(loc=2)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/pynbody_images/'+str(i)+'_outlier.png')
    plt.clf()
