from flask import Flask
import time
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def get_timestamp():
    ts = time.time()
    return f"{ts}"

@app.route('/health')
@metrics.do_not_track()
def health_check():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
