import numpy as np
from numpy.linalg import solve,norm
import pygame as pg
from math import *
import sys
import csv

xmax = 1000 #pixels  
ymax = 800  #pixels
maxelev = 10.0 #deg - max elevation angle looking up from center
d_elev = radians(maxelev)
pz = (ymax/2)/tan(radians(maxelev)) #pixels
ourpos = np.array([[-1850.]
                   ,[0.],
                   [-100.]]) #meters
pg.init()
screen = pg.display.set_mode((xmax,ymax))

def runway():
    raw = np.genfromtxt("runway_lights.dat", delimiter = ",", skip_header = 1)        
    lightpos = raw[:,:3]
    x= lightpos[:,1]
    y= lightpos[:,0]
    z= np.zeros(697).T
    lightpos = np.column_stack((x,y,z))
    lightpos = lightpos.T
    lightcol = raw[:,2:]
    lightcol = lightcol.astype(int)
    return lightpos, lightcol

def drawhorizon(x1,y1,xr,yr):
    black = (0,0,0)
    white = (255,255,255)
    screen.fill((black))
    pg.draw.line(screen, white,(x1,y1),(xr,yr))
    #pg.display.update()

def drawlights(xscreen, yscreen, zscreen, lightcol):
    if zscreen <= 5000:
        r=int(max(1,(5000-zscreen)/1500))
        pg.draw.circle(screen, lightcol, (xscreen,yscreen), r)
    else:
        pg.Surface.set_at(screen, (xscreen,yscreen), lightcol)
    

def rotate(A,phi,theta,psi):
    phi=-phi/57.2958
    theta=theta/57.2958
    psi=-psi/57.2958
    Rx=np.array([[1.,0.,0.],
                 [0.,np.cos(phi),-np.sin(phi)],
                 [0.,np.sin(phi),np.cos(phi)]])
    Ry=np.array([[np.cos(theta),0.,np.sin(theta)],
                 [0.,1.,0.],
                 [-np.sin(theta),0.,np.cos(theta)]])
    Rz=np.array([[np.cos(psi),-np.sin(psi),0.],
                 [np.sin(psi),np.cos(psi),0.],
                 [0.,0.,1.]])
    Rtot=np.matmul(Rz,A)
    Rtot=np.matmul(Ry,Rtot)
    Rtot=np.matmul(Rx,Rtot)
    return Rtot
    
    
def closescr(running=False):
    pg.display.quit()
    pg.quit()

d_eelv  = maxelev
d_azim  = maxelev*xmax/ymax
diagonal= np.sqrt(xmax**2 + ymax**2)

phi = 0.0 #deg --bank angle
theta = 3.0 #deg --pitch angle
psi =0.0 #deg --yawing angle
v= 65 #m/s
omega = 15. #deg/s --angular rate around axis due to controls
a = 0. #m/s^2

T0 = pg.time.get_ticks() *0.001
t0 = pg.time.get_ticks()*0.001
t0=t0-T0
max_dt=0.5
dphi=0
lightpos,lightcol = runway()
running = True
while running:
    t=0.001*pg.time.get_ticks()-T0
    dt = min(t-t0,max_dt)
    t0=t

    xc=-theta/57.2958 *np.sin(phi/57.2958)*(xmax/2)/d_azim + xmax/2
    yc=-theta/57.2958 *np.cos(phi/57.2958)*(ymax/2)/d_elev +ymax/2
    
    dx=diagonal*np.cos(phi/57.2958)  
    dy=-diagonal*np.sin(phi/57.2958)

    xl=xc-dx
    xr=xc+dx
    yl=yc-dy
    yr=yc+dy
    drawhorizon(xl,yl,xr,yr)

    ourpos[0]+= v*dt* np.cos(psi/57.2958) * np.cos(theta/57.2958)
    ourpos[1]+= v*dt* np.sin(psi/57.2958) * np.cos(theta/57.2958)
    ourpos[2]+= v*dt* np.sin(theta/57.2958)
    psi+=omega*dt *np.tan(phi/57.2958)
    #v=v+a*dt

    pg.event.pump()
    keys = pg.key.get_pressed()
    
    
    relpos = lightpos-ourpos
    #print("")
    #print(relpos[0][0])
    #print(relpos[1][0])
    #print(relpos[2][0])

    rotated_pos=rotate(relpos,phi,theta,psi)
    
    x_lights=rotated_pos[0,:]
    y_lights=rotated_pos[1,:]
    z_lights=rotated_pos[2,:]
    
    xscreen=y_lights
    yscreen=z_lights
    zscreen=x_lights
    xs= xmax/2 + pz * xscreen/zscreen
    ys= ymax/2 + pz * yscreen/zscreen

    for i in range(len(xscreen)):
        if zscreen[i]>0:
            drawlights(int(xs[i]),int(ys[i]),int(zscreen[i]),lightcol[i])
    pg.display.flip()
    
    if keys[pg.K_w]:
        theta+=0.02
        
    if keys[pg.K_s]:
        theta-=0.02
        
    if keys[pg.K_d]:
        phi+=0.1  
        
        
    if keys[pg.K_a]:
        phi-=0.1
         
    if keys[pg.K_UP]:
            v=v+2
    if keys[pg.K_DOWN]:
        if v>0:
            v=v-2

    for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                closescr()
    if keys[pg.K_ESCAPE]:
        running = False
        closescr()





