import pynbody
import numpy
import tangos as db

#Pynbody data
z_2 = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.001945')
z_0 = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.008192')
halos_0 = z_0.halos(dosort=True)
halos_2 = z_2.halos(dosort=True)

#database
db_0 = db.get_timestep('cosmo25%/%8192')
db_2 = db.get_timestep('cosmo25%/%1945')

#Empty lists
numbers_2_pynbody = []
numbers_0_pynbody = []
numbers_2_db = []
numbers_0_db = []
file = open('sim_numbers.dat',"w")

'''
#Pynbody z_0
print 'pynbody_0 \n'
file.write('numbers_0_pynbody = \n')
for i in range(len(halos_0)):
    dark = len(halos_0[i].dark)
    stars = len(halos_0[i].stars)
    gas = len(halos_0[i].gas)
    if (dark >= 100000) and (stars + gas >= 100000) and (gas >= 5000):
        numbers_0_pynbody.append(i)
        print i
    else:
        continue
for item_1 in numbers_0_pynbody:
    file.write("%s\n" % item_1)
'''
#Pynbody z_2
print 'pynbody_2 \n'
file.write('numbers_2_pynbody = \n')
for j in range(len(halos_2)):
    darkm = len(halos_2[j].dark)
    starsm = len(halos_2[j].stars)
    gasm = len(halos_2[j].gas)
    if (darkm >= 100000) and (starsm + gasm >= 100000) and (gasm >= 5000):
        numbers_2_pynbody.append(j)
        print j
    else:
        continue
for item_2 in numbers_2_pynbody:
    file.write("%s\n" % item_2)
'''
#DB z_0
print 'db_0 \n'
file.write('db_0 = \n')
print range(len(db_0.halos))
for k in range(len(db_0.halos)):
    ndm = len(db_0.halos[k].NDM)
    ngas = len(db_0.halos[k].Ngas)
    nstars = len(db_0.halos[k].Nstars)
    if (ndm >= 100000) and (nstars + ngas >= 100000) and (ngas >= 5000):
        numbers_0_db.append(k)
        print k
    else:
        continue
for item_3 in numbers_0_db:
    file.write("%s\n" % item_3)

#DB z_2
print 'db_2 \n'
file.write('db_2 = \n')
print range(len(db_2.halos))
for k in range(len(db_2.halos)):
    ndm = len(db_2.halos[l].NDM)
    ngas = len(db_2.halos[l].Ngas)
    nstars = len(db_2.halos[l].Nstars)
    if (ndm >= 100000) and (nstars + ngas >= 100000) and (ngas >= 5000):
        numbers_2_db.append(l)
        print l
    else:
        continue
for item_4 in numbers_2_db:
    file.write("%s\n" % item_4)
'''
