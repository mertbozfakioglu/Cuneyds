import simulator
import cuneyd
import time

sim = simulator.Simulator(background_color = (210,210,210))
sim.create_cuneyd(-100,200,3,"baban",0.8)
sim.create_cuneyd(200,-150,1.6,"anan",1)
sim.create_cuneyd(242,23,2.5,"kayinvaliden",0.2)

sim.create_cuneyd(124,270,0,"emmi oglun",0.3)

sim.create_cuneyd(-120,-343,23,"bacanagin",0.7)

baldiz = cuneyd.Cuneyd(260,254,2.7,"baldizin",0.2)
sim.add_cuneyd(baldiz)
baldiz.add_point(754,450,2,250)
baldiz.add_point(746,453,2,200)
baldiz.add_point(734,370,2,100)
baldiz.add_point(772,465,2,100)
baldiz.add_point(725,443,2,1)

print sim.cuneyds[0]
print cuneyd.Cuneyd.id_list

x = 0
t = 0
while sim.check_quit():
	x+=0.5
	t+=0.1
	baldiz.set(x,baldiz.y,t,baldiz.ID,baldiz.p)
	sim.update_screen()
