# app.py

from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
import elasticapm
import logging

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'bem-flask-poc',
    'SECRET_TOKEN': '1v9Hxnp6FU4GljGiOB',
    'DEBUG': True,
    'SERVER_URL': 'https://3b0ac9ad96f6420e8e9c43d5dde81b66.apm.us-east-1.aws.cloud.es.io:443',
    'ENVIRONMENT': 'development',
}

apm = ElasticAPM(app, logging=logging.INFO)

@elasticapm.capture_span()
@app.route("/")
def hello():
    app.logger.info('Enter / route')
    return "Hello World!"

if __name__ == '__main__':
    app.run()
