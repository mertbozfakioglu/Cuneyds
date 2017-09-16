import math
import random
import sensor
class CuneydBot(object):
    def __init__(self,x,y,th,id,p = 1,sensors_xyt = [(-1,1,math.pi),(1,1,0),(0,1,math.pi/2)]):
        self.x = x
        self.y = y
        self.th = th
        self.ID = ID
        self.p = p
        self.sensors = []
    def diff_drive(self,v,w):
        #CHECK MATH
        x = math.tan(w*t)*v*t
        y = v*t
        return (x,y)

    def noisefy(self,data,percent_error):
		#noisefies input by percent_error
        return data + data*(2*random.random()-1)*percent_error

    def add_sensor(self,x,y,th,sensor_type = sensor.ProximitySensor):
        #adds sensor to the according place
        self.sensors.append(Sensor.sensor_type(x,y,th))
        pass

    def diff_drive_overtime(self,t,dt,v,w):
        #calculates the robots position with respect to itself after t seconds,
        #with dt in miliseconds, with the selected drive method and updates it
        #relative to cardinal coordinates
        x,y = 0
        for i in range(0,int(t*1000/dt)):
            dx,dy = diff_drive(v,w)
            x += dx
            y += dy
        #write the update dunction MATHMATHIHHICALLYY
        #self.x =
        #self.y =








