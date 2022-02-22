import pygame as pg
pg.init() #initialize all pygame modules
#colours
black = (0,0,0)
white = (255,255,255) #R G B

#create a window with a given resolutin
xmax=600 
ymax=800

scr = pg.display.set_mode([xmax,ymax])

ballpic = pg.image.load("ball.gif")
ballrect = ballpic.get_rect()


#initialize simulation

x=300.
y=400.
vx = 100. #pixels/seconds
vy = 200. #pixels/seconds
t = pg.time.get_ticks()*0.001 # time in seconds
t0=t

running = True
while t<15. and running:

    #Hnadle events

    pg.event.pump()
    
    # Get variable time step
    t = pg.time.get_ticks()*0.001
    dt= t -t0
    t0=t
    
    # Integrate
    x=x+vx*dt
    y=y+vy*dt

    # Bounce off the edges
    if x>=xmax:
        vx= -vx
        x = xmax - (x-xmax)
    elif x<0:
        vx = -vx
        x= -x
        
    if y>=ymax:
        vy= -vy
        y = ymax - (y-ymax)
    elif y<0:
        vy = -vy
        y= -y    

    #Get kets to check for escape key
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False

    #Close your window when user presses close windows buttn

    for event in pg.event.get():
        if event.type==pg.QUIT:
            running = False
            
    
    #Clear screen
    scr.fill(black)

    # Paste (blit)  the bitmap to the position
    ballrect.center = (x,y)
    scr.blit(ballpic, ballrect)

    # Basic drawing commands
    pg.draw.line(scr,white,(10,10),(400,200),2)
    
    # Update screen with our drawing in video memory
    pg.display.flip()
    
pg.quit() # closes window 
