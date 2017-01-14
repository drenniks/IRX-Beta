import matplotlib
matplotlib.use('Agg')
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
import numpy as np

pynbody.config['number_of_threads'] = 1
s = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.008192')
halos = s.halos(dosort=True)
#numbers = [18, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 186, 187, 188, 189, 190, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 213, 214, 215, 216, 218, 219, 222, 223, 224, 225, 226, 229, 230, 232, 233, 234, 235, 236, 237, 239, 242, 244, 245, 247, 249, 252, 253, 254, 258, 260, 264, 265, 266, 273, 276, 283, 304, 310, 335]
numbers = [38]

for i in range(len(numbers)):
    h = halos.load_copy(i)
    h.physical_units()
    
    pynbody.analysis.halo.center(h, mode='hyb')
    pynbody.plot.stars.render(h, width='40 kpc')
    plt.savefig('stars_' + str(i) + '.png')
    plt.close()

    sph.image(h.g, qty="rho", units="g cm^-3", cmap="Greys")
    plt.savefig('gas_density_' + str(i) + '.png')
    plt.close()


