import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tangos as db
import pynbody 
from matplotlib import rc
import gc

#Halo numbers
#numbers =  [18, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 132, 133, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 186, 187, 188, 189, 190, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 213, 214, 215, 216]
numbers = [38]

#Simulation data
sim = db.get_simulation('cosmo25')
step1 = db.get_timestep('cosmo25%/%8192')
s = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.008192')
s.physical_units()
gal = s.halos(dosort=True)

#Skirt data & comparison data
data =  np.genfromtxt('skirt_faceon.dat', names = ['halo', 'IRX', 'beta', 'neg_ebeta', 'pos_ebeta', 'intercept', 'neg_eint', 'pos_eint'])
#data = data_angles[data_angles['angle'] == 90.]
compare_data = np.genfromtxt('BF_IRXBdata_comparison.dat', names = ['IRX', 'e_IRX', 'beta', 'e_beta'], skip_header =11)

#Fit from Forrest et al.
B = np.linspace(-2.5, 2.5, 100)
y = np.log10(10**(0.4*(5.05 + 2.39*B)) - 1) + np.log10(1.68)

#Grabbing my variables
halomvir = []
for i in numbers:
    string = i - 1
    halomvir.append(np.log10(step1.halos[int(string)]['Mvir']))
halomvir = np.array(halomvir)
print 'len(halomvir) = ', len(halomvir)

haloMColdG = []
for i in numbers:
    hn = gal.load_copy(i)
    haloMColdG.append(np.sum(hn.gas[hn.gas['temp'] <= 30000.]['mass']))
haloMColdG = np.array(haloMColdG)
print 'len(haloMColdG) = ', len(haloMColdG)

haloMgas = []
for i in numbers:
    string = i - 1
    haloMgas.append(np.log10(step1.halos[int(string)]['Mgas']))
haloMgas = np.array(haloMgas)
print 'len(haloMgas) = ', len(haloMgas)

haloMstars = []
for i in numbers:
    string = i - 1
    haloMstars.append(np.log10(step1.halos[int(string)]['Mstar']))
haloMstars = np.array(haloMstars)
print 'len(haloMstars) = ', len(haloMstars)

agestars = []
for i in numbers:
    hn = gal.load_copy(i)
    stars = hn.stars[hn.stars['tform'] >= 0.]
    halo_age = stars['age'].in_units('yr')
    total_age = np.sum(halo_age)
    num_stars = len(stars)
    avg_age = total_age/num_stars
    agestars.append(avg_age)
agestars = np.array(agestars)
print 'len(agestars) = ', len(agestars)

Z_sun = 0.019
Z_stars = []
for i in numbers:
    hn = gal.load_copy(i)
    stars = hn.stars[hn.stars['tform'] >=0.]
    Z_avg = np.sum(stars['metals'])/len(stars['metals'])
    Z_frac = Z_avg/Z_sun
    Z_stars.append(np.log10(Z_frac))
Z_stars = np.array(Z_stars)
print 'len(Z_stars) = ', len(Z_stars)

Z_gas = []
for i in numbers:
    hn = gal.load_copy(i)
    Z_avg = np.sum(hn.gas['metals'])/len(hn.gas['metals'])
    Z_frac = Z_avg/Z_sun
    Z_gas.append(np.log10(Z_frac))
Z_gas = np.array(Z_gas)
print 'len(Z_gas) = ', len(Z_gas)

luminosity = np.genfromtxt('luminosity.dat', names = ['halo', 'lum'])
lum = luminosity['lum']
m_sun = 2e30 

beta = data['beta']
IRX = np.log10(data['IRX'])
c_beta = compare_data['beta']
c_IRX = np.log10(compare_data['IRX'])

#Plotting

#IRX vs. Beta, colored by the log of mass of cold gas of the halo (temp < 30000K) divided by the mass of th sun.
sm = plt.cm.ScalarMappable(cmap = 'bone', norm = plt.Normalize(vmin = np.min(haloMColdG), vmax = np.max(haloMColdG)))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = haloMColdG, s=50, alpha = 0.7, cmap = 'bone', vmin = np.min(haloMColdG), vmax = np.max(haloMColdG), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'red', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'Mass$_{Cold Gas}$')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_MColdGas.png')
#plt.show()
plt.clf()
del sm
del cbar

#IRX vs. Beta, colored by the log of the mass of the gas divided by the mass of the sun.
sm = plt.cm.ScalarMappable(cmap = 'bone', norm = plt.Normalize(vmin = np.min(haloMgas), vmax = np.max(haloMgas)))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = haloMgas, alpha = 0.7, s=50, cmap = 'bone', vmin = np.min(haloMgas), vmax = np.max(haloMgas), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'red', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'$log_{10} ( Mass_{gas} ) $')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_Mgas.png')
#plt.show()
plt.clf()
del sm
del cbar

#IRX vs. Beta, colored by the log of the mass of the halo divided by the mass of the sun.
sm = plt.cm.ScalarMappable(cmap = 'bone', norm = plt.Normalize(vmin = np.min(halomvir), vmax = np.max(halomvir)))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = halomvir, s=50, alpha = 0.7, cmap = 'bone', vmin = np.min(halomvir), vmax = np.max(halomvir), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'red', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'log$_{10} ( Mass ) $')
#plt.xticks(labels, rotation = 45, ha = 'center')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_halomvir.png')
#plt.show()
plt.clf()
del sm
del cbar

#IRX vs. Beta, colored by the log of the Luminosity (Near infrared, 1.99 -> 2.31 micron)
sm = plt.cm.ScalarMappable(cmap = 'cool_r', norm = plt.Normalize(vmin = np.min(np.log10(lum)), vmax = np.max(np.log10(lum))))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = np.log10(lum), s=50, alpha = 0.7, cmap = 'cool_r', vmin = np.min(np.log10(lum)), vmax = np.max(np.log10(lum)), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'black', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'log$_{10}$(L) [log$_{10}$(L$_{\odot}$)]')
#plt.xticks(labels, rotation = 45, ha = 'center')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_lum.png')
#plt.show()
plt.clf()
del sm
del cbar

#IRX vs. Beta, colored by the log of the mass of the stars divided by the mass of the sun.
sm = plt.cm.ScalarMappable(cmap = 'bone', norm = plt.Normalize(vmin = np.min(haloMstars), vmax = np.max(haloMstars)))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = haloMstars, s=50,  alpha = 0.7, cmap = 'bone', vmin = np.min(haloMstars), vmax = np.max(haloMstars), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'red', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'$log_{10} ( Mass_{stars} ) $')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_Mstars.png')
#plt.show()
plt.clf()
del sm
del cbar

#Plotting the raw star formation rate and calculating the average star formation rate over the last 100 Myrs. for each halo.
SFR = []
for i in numbers:
    hn_SFR = step1.halos[i-1]['SFR_histogram']
    plt.hist(hn_SFR)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/raw_SFR/SFR_' + str(i) + '.png')
    plt.clf()
    
    string = '"cosmo25%/%8192/' + str(i-1) + '"'
    print 'string is ', string
    halo_call = string[1:-1]
    halo_SFR = db.get_halo(halo_call)
    raw_SFR = halo_SFR.calculate("raw(SFR_histogram)")/(1e9) #Msun/yr
    #Taking SFR for the last 100 Myrs (from the raw data) (in bins of 10 Myr)
    SFR_100 = np.sum(raw_SFR[-10:])
    avg_SFR = SFR_100 / 10
    print 'avg_SFR = ', avg_SFR
    SFR.append(avg_SFR)
    plt.hist(raw_SFR, bins = range(11))
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/final_IRX/z_0/IRX_b/test_IRX/raw_SFR/SFR_hist_' + str(i) + '.png')
    plt.clf()
SFR = np.array(SFR)
print 'SFR = ', SFR
print 'np.min(SFR) = ', np.min(SFR)
print 'np.max(SFR) = ', np.max(SFR)
print 'np.min(np.log10(SFR)) = ', np.min(np.log10(SFR))
print 'np.max(np.log10(SFR)) = ', np.max(np.log10(SFR))

#IRX vs. Beta, colored by the log of the SFR (caluclated by averaging over the last 100 Myr)
sm = plt.cm.ScalarMappable(cmap = 'cool_r', norm = plt.Normalize(vmin = np.min(SFR), vmax = np.max(SFR)))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = SFR, s=50, alpha = 0.7, cmap = 'cool_r', vmin = np.min(SFR), vmax = np.max(SFR), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'black', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'SFR')
#plt.xticks(labels, rotation = 45, ha = 'center')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_SFR.png')
#plt.show()
plt.clf()
del sm
del cbar

#IRX vs. Beta, colored by the log of the avg age of the total stars.
sm = plt.cm.ScalarMappable(cmap = 'cool_r', norm = plt.Normalize(vmin = np.min(np.log10(agestars)), vmax = np.max(np.log10(agestars))))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = np.log10(agestars), s=50, alpha = 0.7, cmap = 'cool_r', vmin = np.min(np.log10(agestars)), vmax = np.max(np.log10(agestars)), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'black', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'log$_{10}$(Avg. Stellar Age) [log$_{10}$(Yr)]')
#plt.xticks(labels, rotation = 45, ha = 'center')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_avg_age.png')
#plt.show()
plt.clf()
del sm
del cbar

#IRX vs. Beta, colored by the average stellar metallicity
sm = plt.cm.ScalarMappable(cmap = 'bone', norm = plt.Normalize(vmin = np.min(Z_stars), vmax = np.max(Z_stars)))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = Z_stars, s=50, alpha = 0.7, cmap = 'bone', vmin = np.min(Z_stars), vmax = np.max(Z_stars), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'red', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'$ log_{10}( \frac{Z_{Stars,Avg}}{Z_{\odot}} )$')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_Zstars.png')
#plt.show()
plt.clf()
del sm
del cbar

#IRX vs. Beta, colored by the average gas metallicity
sm = plt.cm.ScalarMappable(cmap = 'bone', norm = plt.Normalize(vmin = np.min(Z_gas), vmax = np.max(Z_gas)))
sm.set_array([])
plt.plot(B, y, label ='Fit from Forrest et al')
plt.scatter(beta, IRX, c = Z_gas, s=50, alpha = 0.7, cmap = 'bone', vmin = np.min(Z_gas), vmax = np.max(Z_gas), label = 'Romulus, z=0')
plt.scatter(c_beta, c_IRX, s=50, marker='*', c = 'red', alpha = 0.55, label = 'Forrest et al')
cbar = plt.colorbar(sm)
cbar.set_label(r'$ log_{10}( \frac{Z_{Gas,Avg}}{Z_{\odot}} )$')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 3.0)
plt.ylim(-2,6)
plt.legend(loc=2, prop={'size':10})
plt.savefig('IRXb_Zgas.png')
#plt.show()
plt.clf()
del sm
del cbar

#Plotting numbers
'''
fig, ax = plt.subplots()
plt.scatter(beta, IRX, s = 50)
plt.plot(B,y, label = 'Fit from Forrest et al')
plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
for i,txt in enumerate(numbers):
    ax.annotate(txt, (beta[i], IRX[i]))
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
#plt.xlim(-2.5, 2.5)
plt.ylim(-6.5,6)
plt.title('z_0')
plt.legend(loc=2)
plt.show()
plt.savefig('numbers_z0.png')
plt.clf()
'''

'''
fig, ax = plt.subplots()
plt.plot(B,y, label = 'Fit from Forrest et al')
plt.scatter(c_beta, c_IRX, s=50, marker = '*', c = 'black', alpha = 0.65, label = 'Forrest et al')
plt.xlabel(r'$\beta$')
plt.ylabel(r'log$_{10}$(IRX)')
plt.ylim(-6.5,6)
plt.title('z_0')
plt.legend(loc=2)
for i in numbers:
    x = data[data['halo'] == str(i)]['beta']
    v = np.log10(data[data['halo'] == str(i)]['IRX'])
    plt.scatter(x, np.log10(v), s = 50)
    ax.annotate(str(i), (x, v))
    del x
    del v
plt.show()
'''
