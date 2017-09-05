

class Point(object):

	def __init__(self,x,y,t,ID,p = 1):
		self.x = x
		self.y = y
		self.t = t
		self.ID = ID
		self.p = p


	def set_attriutes(self,x,y,t,ID,p):
		#gereksiz gibi
		self.x = x
		self.y = y
		self.t = t
		self,ID = ID
		self.p = p

	def __str__(self):
		return "ID: {0}\nx,y,t: {1}\nprobability: {2}".format(self.ID,(self.x,self.y,self.t),self.p)		
