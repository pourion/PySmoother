"""
Example to read snapshot from FIRE simulation
Author: Pouria A. Mistani
email: p.a.mistani@gmail.com
October 2015
"""
import numpy as np
import matplotlib.pyplot as plt
import snapHDF5 as snap
import pdb
import PySmoother as PyS
import matplotlib.pyplot as plt








filename1 = './m10_hr_Dec9_2013/snapshot_440'	#1e10
filename2 = '../../snapshot_440'   #1e11
filename3 = './m12qq_hr_Dec16_2013/snapshot_440'  #1e12

offset = 200



## -- read stellar components ---

'''
mass = snap.read_block(filename, "MASS", parttype=4)
print 'pase mass'
age = snap.read_block(filename, "AGE ", parttype=4)
print 'pase age'
metal = snap.read_block(filename, "Z   ", parttype=4)
print 'pase metal'
## -- read some gas-exclusive info ----- ##
sfr = snap.read_block(filename, "SFR ", parttype=0)
print 'pase sfr'
'''


print '1e10'

pos = snap.read_block(filename1, "POS ", parttype=1) #Notice that to read POS and VEL of gas and DM, only change parttype=0 or 1, respectively
print 'pase pos'
vel = snap.read_block(filename1, "VEL ", parttype=1)
print 'pase vel'
print 'done reading',pos.shape
X = pos[:,0]
Y = pos[:,1]
Z = pos[:,2]
Vx = vel[:,0]
Vy = vel[:,1]
Vz = vel[:,2]
mass = np.ones(len(X))

image = PyS.PyS(X, Y, Z, mass, Vx, Vy,Vz, r=2, w=1000, h=1000, offset=50)
M_Vir = image.Virial_Cut(45)
img = image.smooth(plane='xy')
extent = image.extent()			
plt.figure(figsize=(21,7))			
ax1 = plt.subplot(131)
ax1.imshow(img, extent = extent)


ax1.plot([30, 40], [-40, -40], linewidth=3, color='w')
ax1.annotate(r'$M_{200} = 1e10$', xy=(20, 40),color='w', fontsize=15)
ax1.annotate('10 kpc', xy=(30, -35),color='w', fontsize=15)
ax1.set_xlabel('X', fontsize=20)
ax1.set_ylabel('Y', fontsize=20)
ax1.set_xlim([extent[0],extent[1]])
ax1.set_ylim([extent[2], extent[3]])



print '1e11'
#######
pos = snap.read_block(filename2, "POS ", parttype=1) #Notice that to read POS and VEL of gas and DM, only change parttype=0 or 1, respectively
print 'pase pos'
vel = snap.read_block(filename2, "VEL ", parttype=1)
print 'pase vel'
print 'done reading',pos.shape
X = pos[:,0]
Y = pos[:,1]
Z = pos[:,2]
Vx = vel[:,0]
Vy = vel[:,1]
Vz = vel[:,2]
mass = np.ones(len(X))

image = PyS.PyS(X, Y, Z, mass, Vx, Vy,Vz, r=2, w=1000, h=1000, offset=88)
M_Vir = image.Virial_Cut(80.)
img = image.smooth(plane='xy')
extent = image.extent()	
ax2 = plt.subplot(132)
ax2.imshow(img, extent = extent)
ax2.plot([70, 80], [-70, -70], linewidth=3, color='w')
ax2.annotate(r'$M_{200} = 1e11$', xy=(35, 70),color='w', fontsize=15)
ax2.annotate('10 kpc', xy=(65, -62),color='w', fontsize=15)
ax2.set_xlabel('X', fontsize=20)
ax2.set_ylabel('Y', fontsize=20)
ax2.set_xlim([extent[0],extent[1]])
ax2.set_ylim([extent[2], extent[3]])




#######
print '1e12'
#######
pos = snap.read_block(filename3, "POS ", parttype=1) #Notice that to read POS and VEL of gas and DM, only change parttype=0 or 1, respectively
print 'pase pos'
vel = snap.read_block(filename3, "VEL ", parttype=1)
print 'pase vel'
print 'done reading',pos.shape
X = pos[:,0]
Y = pos[:,1]
Z = pos[:,2]
Vx = vel[:,0]
Vy = vel[:,1]
Vz = vel[:,2]
mass = np.ones(len(X))

image = PyS.PyS(X, Y, Z, mass, Vx, Vy,Vz, r=2, w=1000, h=1000, offset=220)
M_Vir = image.Virial_Cut(200.)
img = image.smooth(plane='xy')
extent = image.extent()	
ax3 = plt.subplot(133)
ax3.imshow(img, extent = extent)
ax3.plot([130, 140], [-176, -176], linewidth=3, color='w')
ax3.annotate(r'$M_{200} = 1e12$', xy=(80, 170),color='w', fontsize=15)
ax3.annotate('10 kpc', xy=(130, -154),color='w', fontsize=15)
ax3.set_xlabel('X', fontsize=20)
ax3.set_ylabel('Y', fontsize=20)
ax3.set_xlim([extent[0],extent[1]])
ax3.set_ylim([extent[2], extent[3]])
#######

for ax in [ax1, ax2, ax3]:
        plt.setp(ax.get_yticklabels(), visible=False)
      	plt.setp(ax.get_yticklines(), visible=False)
        plt.setp(ax.get_xticklabels(), visible=False)
    	plt.setp(ax.get_xticklines(), visible=False)
    	ax.xaxis.set_major_formatter(plt.NullFormatter())
    	ax.yaxis.set_major_formatter(plt.NullFormatter())
plt.tight_layout()
plt.savefig('test.png')



#ax.imshow(img)		
#ax.set_xlim(extent[0], extent[1])
#ax.set_ylim(extent[2], extent[3])
			

#r, g, b = img.split()

pdb.set_trace()
