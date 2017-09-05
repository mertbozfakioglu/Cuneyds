import pygame
import cuneyd
import math
import point

#TO-DO: ADD ALPHA VALUES INSTEAD OF THICKNESS, ADD ADJUST_SIZE FUNCTION, ADD UI (SELECTING SPECIFIC CUNEYDS), ADD GRID

class Simulator(object):

	colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),
	(255,0,255),(255,102,0),(153,51,255),(0,102,0),(153,102,51)]

	def __init__(self, w = 900, h = 900, background_color = (0,0,0)):
		self.w = w
		self.h = h
		self.background_color = background_color
		self.screen = pygame.display.set_mode((self.w, self.h))
		self.screen.fill(background_color)
		self.cuneyds = []
		pygame.font.init() 
		self.def_font = pygame.font.SysFont('Ariel', 25)
		pygame.display.update()

	def check_quit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
		return True

	def update_screen(self):
		self.screen.fill(self.background_color)
		self.draw_points()
		self.draw_cuneyds()
		self.legand()
		pygame.display.update()

	def create_cuneyd(self,x,y,t,ID,p):
		self.cuneyds.append(cuneyd.Cuneyd(x,y,t,ID,p))

	def add_cuneyd(self,cuneyd):
		self.cuneyds.append(cuneyd)

	def draw_cuneyd(self,cuneyd,color):
		x = cuneyd.x + self.w/2
		y = cuneyd.y + self.h/2
		t = cuneyd.t
		scale = 10
		thickness = 7*cuneyd.p
		def turn(x,y): return (x*math.cos(t) - y*math.sin(t), x*math.sin(t) + y*math.cos(t))
		c1,c2,c3 = turn(-1.5*scale,-1*scale), turn(0*scale,2*scale), turn(1.5*scale,-1*scale)
		pygame.draw.lines(self.screen, color, True, [(c1[0]+x,c1[1]+y),(c2[0]+x,c2[1]+y),(c3[0]+x,c3[1]+y)], int(thickness))
		#pygame.draw.circle(self.screen, color, (x,y), scale, 2)
		#draw the specific cuneyd

	def draw_cuneyds(self):
		for i in range(len(self.cuneyds)):
			self.draw_cuneyd(self.cuneyds[i],self.colors[i%len(self.colors)])
		pass

	def draw_points(self):
		#draw all point with respective color
		r = 5
		thickness = 0
		for i in range(len(self.cuneyds)):
			for point in self.cuneyds[i].points:
				pygame.draw.circle(self.screen, self.colors[i%len(self.colors)], (point[0],point[1]), r, thickness)

	def legand(self):
		y_pos = 0
		for i in range(len(self.cuneyds)):
			text = self.def_font.render('ID: '+self.cuneyds[i].ID, False, self.colors[i%len(self.colors)])
			self.screen.blit(text,(0,y_pos))
			y_pos+=20
			text = self.def_font.render('x,y,t,p: '+str((self.cuneyds[i].x,self.cuneyds[i].y,self.cuneyds[i].t,self.cuneyds[i].p)),
				False, self.colors[i%len(self.colors)])
			self.screen.blit(text,(0,y_pos))
			y_pos+=30

	def adjust_size(self):
		#if map is too small for all cuneyds, zoom out
		pass

