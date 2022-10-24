import random
import time
from flask import Flask
import requests

app = Flask(__name__)


def metric_generator(endpoint, return_message):
    start = time.time()
    time.sleep(random.randint(0, 6))
    code = random.choice([200, 201, 202, 404, 503, 400])
    payload = {'time': time.time() - start, 'status': code, 'endpoint': endpoint}
    try:
        requests.post('http://localhost:5000/metric-receiver', json=payload)
    except:
        app.logger.error("Can't push metrics")
    return return_message, code


@app.route('/random_metrics_endpoint')
def show_analytics():
    return metric_generator('/random_metrics_endpoint', {'result': 'some metrics'})

