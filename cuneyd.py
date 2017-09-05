
class Cuneyd(object):

	id_list = []

	def __init__(self,x,y,t,ID,p = 1):
		self.x = x
		self.y = y
		self.t = t
		self.ID = ID
		self.p = p
		self.id_list.append(ID)
		self.points = []

	def set(self,x,y,t,ID,p):
		self.x = float("%.3f" % x)
		self.y = float("%.3f" % y)
		self.t = float("%.3f" % t)
		self.ID = ID
		self.p = p

	def add_point(self,x,y,t,p):
		self.points.append((x,y,t,p))

	def __str__(self):
		return "ID: {0}\nx,y,t: {1}\nprobability: {2}".format(self.ID,(self.x,self.y,self.t),self.p)		
	
