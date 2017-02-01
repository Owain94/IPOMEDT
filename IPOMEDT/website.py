from flask import Flask, render_template, url_for, jsonify

import RPi.GPIO as GPIO

from util.Logger import Logger
from classes.Light import Light

from Runner import Runner

import os

app = Flask(__name__)
logger = Logger()
runner = Runner()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

headlights = Light([21, 20])


@app.route("/")
@app.route("/index.html")
def index():
    bootstrapcss = url_for('static', filename='css/bootstrap.min.css')
    bootstrapjs = url_for('static', filename='js/bootstrap.min.js')
    jquery = url_for('static', filename='js/jquery-1.12.0.min.js')
    fontawesome = url_for('static', filename='css/font-awesome.min.css')
    events = url_for('static', filename='js/events.js')
    sweetalertcss = url_for('static', filename='css/sweetalert.css')
    sweetalertjs = url_for('static', filename='js/sweetalert.min.js')
    style = url_for('static', filename='css/style.css')

    logger.append('index.html loaded')

    return render_template('index.html', bootstrapcss=bootstrapcss,
                           bootstrapjs=bootstrapjs, jquery=jquery,
                           sweetalertcss=sweetalertcss, sweetalertjs=sweetalertjs,
                           fontawesome=fontawesome, events=events,
                           style=style)


@app.route("/shutdown.html")
def shutdown():
    os.system('echo raspberry | sudo -S poweroff')
    return jsonify(result=True)


@app.route("/reboot.html")
def reboot():
    os.system('echo raspberry | sudo -S reboot')
    return jsonify(result=True)


@app.route("/start.html")
def start():
    logger.append("Started the main script")
    runner.start_runner()
    return jsonify(result=True)


@app.route("/headlights_on.html")
def headlights_on():
    logger.append("Headlights turned on")
    headlights.turn_on()
    return jsonify(result=True)


@app.route("/headlights_off.html")
def headlights_off():
    logger.append("Headlights turned off")
    headlights.turn_off()
    return jsonify(result=True)


@app.route("/sirene_on.html")
def sirene_on():
    logger.append("Sirene turned on")
    headlights.start_sirene()
    return jsonify(result=True)


@app.route("/sirene_off.html")
def sirene_off():
    logger.append("Sirene turned off")
    headlights.stop_sirene()
    headlights.turn_off()
    return jsonify(result=True)


@app.route("/log.html")
def log():
    return logger.read_file()


def main():
    logger.empty_file()

    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
