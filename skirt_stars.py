import pynbody
import numpy as np
import gc

pynbody.config['number_of_threads'] = 1
s = pynbody.load('cosmo25p.768sg1bwK1BHe75.001945')
halos = s.halos()
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 172, 173, 174, 175, 176, 178, 181, 183, 184, 185, 186, 187, 188, 189, 190, 192, 193, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 214, 215, 216, 218, 219, 220, 223, 226, 227, 228, 229, 230, 231, 232, 235, 238, 243, 244, 245, 247, 249, 252, 254, 255, 259, 

numbers = [261, 277, 281, 314]

for i in numbers:
    hn = halos.load_copy(i)
    hn.physical_units()
    center = pynbody.analysis.halo.shrink_sphere_center(hn)
    hn['pos'] = hn['pos'] - center
    vel_center = pynbody.analysis.halo.center_of_mass_velocity(hn)
    hn['vel'] = hn['vel']-vel_center
    stars = hn.stars[hn.stars['tform'] >=0.]
    x = stars['x'].in_units('pc')
    y = stars['y'].in_units('pc')
    z = stars['z'].in_units('pc')
    h = stars['smooth'].in_units('pc')
    mass = np.zeros(len(x)) + 42416.4033
    metals = stars['metals']
    age = stars['age'].in_units('yr')
    allarrays = np.vstack((x, y, z, h,  mass, metals, age)).T
    np.savetxt('stars_' + str(i) + '.dat', allarrays, delimiter=' ', fmt = '%1.6f')
    del hn
    gc.collect()
