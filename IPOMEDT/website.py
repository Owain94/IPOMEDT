from flask import Flask, request, render_template, url_for
from util.Logger import Logger

import os

app = Flask(__name__)
logger = Logger()


@app.route('/')
@app.route('/index.html')
def index():
    bootstrapcss = url_for('static', filename='css/bootstrap.min.css')
    bootstrapjs = url_for('static', filename='js/bootstrap.min.js')
    jquery = url_for('static', filename='js/jquery-1.12.0.min.js')
    cosmo = url_for('static', filename='css/cosmo.css')
    fontawesome = url_for('static', filename='css/font-awesome.min.css')
    events = url_for('static', filename='js/events.js')
    sweetalertcss = url_for('static', filename='css/sweetalert.css')
    sweetalertjs = url_for('static', filename='js/sweetalert.min.js')
    style = url_for('static', filename='css/style.css')

    logger.append('index.html loaded')

    return render_template('index.html', bootstrapcss=bootstrapcss,
                           bootstrapjs=bootstrapjs, jquery=jquery,
                           sweetalertcss=sweetalertcss, sweetalertjs=sweetalertjs,
                           cosmo=cosmo,
                           fontawesome=fontawesome, events=events,
                           style=style)


@app.route('/shutdown.html')
def shutdown():
    os.system('echo raspberry | sudo -S poweroff')


@app.route('/reboot.html')
def reboot():
    os.system('echo raspberry | sudo -S reboot')


@app.route('/log.html')
def log():
    return logger.read_file()


def main():
    logger.empty_file()

    app.run(host='0.0.0.0', debug=True, threaded=True)

if __name__ == '__main__':
    main()
