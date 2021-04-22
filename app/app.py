from flask import Flask, render_template
import logging
import sys


main_logger = logging.getLogger()
l = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(threadName)s :: %(message)s')
l.setFormatter(formatter)
main_logger.addHandler(l)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def summary():
    response = app.response_class(
        response="healthy",
        status=200,
    )
    return response
