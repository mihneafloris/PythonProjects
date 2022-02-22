from numpy import *

table = genfromtxt("actable.dat", skip_header=4)
ft = 0.3048
minute = 60
kts=0.514444
lat = table [:,0]
lon = table [:,1]
alt = table [:,2]
spd = table [:,3]*kts
crs = table [:,4]
vs= table[:,5]*ft/minute

#print(alt[lat>50])

"""
temp = []
for i in range(len(lat)):
    if lat[i]>50:
        temp.append(alt[i])
print(temp)
"""

#print(alt*(lat>50))

#select values using a condition by multiplication
k = 500.*(spd<200*kts) +50.*(spd>=200*kts)


#Select
k = where(spd<200*kts,500.,50.)  #if-else logic
lst = where(spd<200) #different syntax
print(lst)
