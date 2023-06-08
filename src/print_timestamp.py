import datetime
from flask import Flask
import time
import logging
from prometheus_flask_exporter import PrometheusMetrics
from waitress import serve
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Configure logging
log_level = os.environ.get('LOG_LEVEL', 'error').upper()
numeric_level = getattr(logging, log_level, logging.INFO)
logging.basicConfig(level=numeric_level)
logger = logging.getLogger(__name__)

@app.route('/')
def get_timestamp():
    try:
        ts = time.time()
        dt = datetime.datetime.fromtimestamp(ts)
        month = dt.strftime("%B")
        logger.info("Timestamp requested: %s", ts)
        logger.debug("Debug message: current running month is %s", month)
        return f"{ts}"
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return "Error occurred"

@app.route('/health')
@metrics.do_not_track()
def health_check():
    return "OK"

if __name__ == '__main__':
    logger.info("Starting Flask application...")
    serve(app, host='0.0.0.0', port=5001)
