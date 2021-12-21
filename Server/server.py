#!/usr/bin/env python3
import os
import sys
sys.dont_write_bytecode = True

from ev3dev.ev3 import *
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from flask import Flask
from time import sleep

app = Flask(__name__)
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

@app.route("/A")
def forward():
    tank_pair.on(left_speed=50, right_speed=50)
    return ''

@app.route("/B")
def backward():
    tank_pair.off()
    return ''

if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True, use_evalex=False, use_reloader=False)