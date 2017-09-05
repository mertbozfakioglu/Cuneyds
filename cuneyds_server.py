from flask import Flask, render_template, request

from simulator import Simulator

sim = Simulator(width = 1024, height = 720, background_color = (225,225,225))
app = Flask(__name__)

sim.update_screen()
c_id = 0
@app.route('/')
def hello_world():
    return "Congratulations. You have reached the Cuneyds Server"

@app.route('/health', methods = ["POST", "GET"])
def health_check():
    return "Health Check NYI"

@app.route('/add_point', methods = ["POST"])
def add_point():
    return "NYI"

@app.route('/create_cuneyd', methods = ["POST"])
def create_cuneyd():
    global c_id
    ups = request.json
    if not ups:
        ups = dict()
    if not ups.get('ID', False):
        ups['ID'] = c_id
        c_id += 1
    sim.create_cuneyd(ups.get('x', 0),
                      ups.get('y', 0),
                      ups.get('t', 0),
                      ups.get('ID', c_id),
                      ups.get('p', 0.5))
    sim.update_screen()
    return sim.print_cuneyd(ups['ID'])

@app.route('/update_cuneyd', methods = ["POST"])
def update_cuneyd():
    ups = request.json
    sim.update_cuneyd(ups["ID"], ups.get('x',None), 
                                 ups.get('y',None),
                                 ups.get('t',None),
                                 ups.get('N_ID', None),
                                 ups.get('p', None))
    sim.update_screen()
    return "NYI"

@app.route('/update_point', methods = ["POST"])
def update_point():
    return "NYI"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
