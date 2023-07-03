import time
from flask import Flask, request
import requests
import random
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace import config_integration
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

app = Flask(__name__)
connection_string = "InstrumentationKey=d7fb7c8a-b0d3-4cec-be52-b00aaf23fe7f;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/"
exporter = AzureExporter(connection_string=connection_string)
tracer = Tracer(exporter=exporter, sampler=ProbabilitySampler(rate=1.0))
middleware = FlaskMiddleware(app, exporter=exporter, sampler=ProbabilitySampler(rate=1.0))

def get_user_information_from_external_vendor_api():
    print("bootstrapsvc - extvendorapi")
    with tracer.span(name='Get User Information from External Vendor API'):
        # Perform API call to external vendor
        pass

def get_user_information_from_external_vendor_api_404_error():
    print("bootstrapsvc - 404")
    with tracer.span(name='Get User Information from External Vendor API 404 Error'):
        # Perform API call to external vendor that returns a 404 error
        pass

def do_some_redis_operations():
    print("bootstrapsvc - redis op")
    with tracer.span(name='Do Some Redis Operations'):
        # Perform some Redis operations
        pass

@app.route("/bootstrap", methods=['POST', 'GET'])
def boot_strap_user():
    print(f'Received data with {request.data}')

    get_user_information_from_external_vendor_api()
    get_user_information_from_external_vendor_api_404_error()
    do_some_redis_operations()

    return "bootstrapsvc - bootstrapped", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
