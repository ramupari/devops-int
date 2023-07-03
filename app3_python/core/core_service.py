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


def authenticate_token_on_database(token):
    print('core - authenticating token')

    time.sleep(random.uniform(0.5, 2))  # Simulate database call.

    if token == '123':
        return True
    return False



def call_bootstrap_service(user):
    print(f"core - calling bootstrapsvc endpoint with {user}")

    with tracer.span(name='Call Bootstrap Service'):
        response = requests.post(
            "http://bootstrapservice.azurewebsites.net/bootstrap",
            json={'user': user}
        )


def update_database():
    time.sleep(random.uniform(0.5, 3))  # Simulate database call.

    with tracer.span(name='Update Database'):
        # Update database logic here
        pass


@app.route("/bootstrap-user", methods=['POST', 'GET'])
def bootstrap_user():
    print("core - Starting bootstrap operation.")
    token = request.args.get('token')
    user = request.args.get('user')

    with tracer.span(name='Authenticate Token'):
        if not authenticate_token_on_database(token):
            return "core - Wrong Token!", 401

    try:
        call_bootstrap_service(user)
    except Exception as e:
        print(e)
        return "core - Error sending req to bootstrapservice", 503

    # simulate a call to update database.
    update_database()

    return "core - user has been bootstrapped", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
