
class Cuneyd(object):

    id_list = []

    def __init__(self,x,y,th,ID,p = 1):
	self.x = x
	self.y = y
	self.th = th
	self.ID = str(ID)
	self.p = p
	self.id_list.append(ID)
	self.points = []

    def set(self,x,y,th,ID,p):
        if x:
            self.x = float("%.3f" % x)
        if y:
            self.y = float("%.3f" % y)
        if th:
            self.th = float("%.3f" % th)
        if ID:
            self.ID = ID
        if p:
            self.p = p

    def add_point(self,x,y,th,p):
	self.points.append((x,y,th,p))

    def __str__(self):
	return "ID: {0}\nx,y,th: {1}\nprobability: {2}".format(self.ID,(self.x,self.y,self.th),self.p)		
	
