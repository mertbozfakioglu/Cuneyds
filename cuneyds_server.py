from flask import Flask, render_template, request

from simulator import Simulator

sim = Simulator(width = 1024, height = 720, background_color = (225,225,225))
app = Flask(__name__)

sim.update_screen()

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
    sim.create_cuneyd(p=0.2)
    sim.update_screen()
    return "NYI"

@app.route('/update_cuneyd', methods = ["POST"])
def update_cuneyd():
    print request.json
    print request.json["ID"]
    return "NYI"

@app.route('/update_point', methods = ["POST"])
def update_point():
    return "NYI"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
