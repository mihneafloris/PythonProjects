import numpy as np
from numpy.linalg import solve,norm
import pygame 
import sys
from random import randint

def updateObject(line, Ball):
	#vertices for line and ball position
	a = np.array(line.vertices[0])
	b = np.array(line.vertices[1])
	p = np.array(Ball.pos)
	q = np.array(Ball.nextpos)

	abn = (b-a)/norm(b-a) 

	
	A = np.zeros([2,2])
	A[:,0]=b-a
	A[:,1]=p-q
	
	try:
		
		lam,mu = solve(A,p-a)
	except:
		return False, Ball.nextpos, Ball.v

	
	eps = 0.01
	if (-eps<lam<1+eps and 0<mu<1):
		print()
	else:
		return False, q, Ball.v

	#intersection point
	S = p + mu*(q-p)
	#normal
	n = np.array([abn[1],-abn[0]])
	if np.dot(q-p,n) > 0:
		n*=-1

	
	v = np.array(Ball.v)
	vn = (abn*abn.dot(v)-n*n.dot(v))
	return True, S+abn*abn.dot(q-S)-n*n.dot(q-S), vn/norm(vn)*norm(v)


class Line:
	def __init__(self, pos1, pos2):
		self.vertices = [np.array(pos1),np.array(pos2)]

	def render(self, screen):
		pygame.draw.line(screen,(0,255,255),(self.vertices[0][0],self.vertices[0][1]),(self.vertices[1][0],self.vertices[1][1]))

class Ball:
	def __init__(self, pos, v, radius, colour):
		self.pos = np.array(pos)
		self.v = np.array(v)
		self.radius = radius
		self.colour = colour

	def update(self, screen, lines, dt,t):
		self.nextpos = self.pos + self.v *dt
		
		for line in lines:
			bounce, tmppos, tmpv = updateObject(line, self)
			
			if bounce:
				
				self.pos = tmppos
				self.v = tmpv
				break
			
			elif line is lines[-1]:
				self.pos = tmppos
				self.v = tmpv

		
		p = self.pos 
		pygame.draw.circle(screen, self.colour, (int(p[0]),int(p[1])), self.radius)


#------------------------------Main Code--------------------------------

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


surfs = []

surfs.append(Line((1,1),(1,height-1)))
surfs.append(Line((1,height-1),(width-1,height-1)))
surfs.append(Line((width-1,height-1),(width-1,1)))
surfs.append(Line((1,1),(width-1,1)))

surfs.append(Line((width/3,height/3),(width/3, 2*height/3)))
surfs.append(Line((2*width/3,height/3),(2*width/3, 2*height/3)))
surfs.append(Line((width/3,height/3),(2*width/3, height/3)))
surfs.append(Line((width/3,2*height/3),(width/2, 3*height/4)))
surfs.append(Line((2*width/3,2*height/3),(width/2, 3*height/4)))


balls = []


for i in range(100):
	balls.append(Ball((randint(10,width-10),randint(10, height-10)),(randint(-250,250),randint(-250,250)),5,(randint(0,255),randint(0,255),randint(0,255))))

#Framerate counter
myfont = pygame.font.SysFont("monospace", 30)


lastt = pygame.time.get_ticks()
while True:
	
	currentt =pygame.time.get_ticks()
	dt = (currentt-lastt)/1000
	screen.fill((0,0,0))

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	
	for i in range(len(balls)):
		
		balls[i].update(screen,surfs,dt,currentt/1000)

	
	for sf in surfs:
		sf.render(screen)

	
	lastt = currentt
	
	screen.blit(myfont.render(str(round(1/dt if dt > 0 else 60)), 1, (255,255,0)), (50, 50))
	pygame.display.update()
	
