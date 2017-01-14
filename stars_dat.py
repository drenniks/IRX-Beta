import pynbody
import numpy as np
import gc

pynbody.config['number_of_threads'] = 1
s = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.008192')
halos = s.halos(dosort=True)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 211, 213, 214, 215, 218, 220, 221, 223, 224, 225, 228, 229, 230, 231, 232, 233, 234, 236, 238, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 255, 256, 257, 258, 259, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 272, 273, 275, 276, 278, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 302, 303, 304, 305, 308, 310, 311, 313, 315, 316, 317, 318, 321, 322, 324, 325, 328, 331, 332, 334, 335, 336, 339, 340, 341, 346, 352, 355, 356, 360, 363, 364, 366, 372, 380, 387, 389, 418]

for i in numbers:
    try:
        hn = halos.load_copy(i)
        hn.physical_units()
    #center = pynbody.analysis.halo.shrink_sphere_center(hn)
    #hn['pos'] = hn['pos'] - center
    #vel_center = pynbody.analysis.halo.center_of_mass_velocity(hn)
    #hn['vel'] = hn['vel']-vel_center
        stars = hn.stars[hn.stars['tform'] >=0.]
        pynbody.analysis.angmom.faceon(hn)
    
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

    except ValueError:
        print 'not enough particles in halo ', numbers[i], '!'
        pass
