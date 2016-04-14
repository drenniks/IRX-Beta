import pynbody
import numpy as np
import gc
import sys 
import pdb

#sys.settrace()
pynbody.config['number_of_threads'] = 1
s = pynbody.load('cosmo25p.768sg1bwK1BHe75.001945')
halos = s.halos()
numbers = [314]

for i in range(len(numbers)):
    print 'you are on halo ', numbers[i]
    hn = halos.load_copy(numbers[i])
    hn.physical_units()
    center = pynbody.analysis.halo.shrink_sphere_center(hn)
    hn['pos'] = hn['pos'] - center
    print 'you have centered halo ', numbers[i]
    vel_center = pynbody.analysis.halo.center_of_mass_velocity(hn)
    hn['vel'] = hn['vel']-vel_center
    print 'you have vel_centered halo ', numbers[i]

    x = hn.gas['x'].in_units('pc')
    y = hn.gas['y'].in_units('pc')
    z = hn.gas['z'].in_units('pc')
    print 'you have found all positions for halo ', numbers[i]
    h = hn.gas['smooth'].in_units('pc')
    print 'you found the smoothing length for halo ', numbers[i]
    mass = hn.gas['mass'].in_units('Msol')
    print 'you found the mass for halo ', numbers[i]
    metals = hn.gas['metals']
    print 'you have found the metallicity for halo ', numbers[i]
    temp = hn.gas['temp'].in_units('K')
    print 'you have found temp for halo ', numbers[i]

    allarrays = np.vstack((x, y, z, h,  mass, metals, temp)).T
    print 'you are about to save your text for halo ', numbers[i]
    np.savetxt('gas_' + str(numbers[i]) + '.dat', allarrays, delimiter=' ', fmt = '%1.6f')
    print 'you have saved your text for halo ', numbers[i]
    del hn
    gc.collect()
    print 'time to start over'

