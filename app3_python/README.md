# Core and Bootstrap Services

These are two sample services that have been updated to include distributed tracing using OpenTelemetry and integrate with Azure Application Insights. The services demonstrate how to propagate span context between them using HTTP headers and capture and export the spans to Azure Application Insights for monitoring and analysis. Docker files have also been added to enable running the services in containers.

## Core Service

The Core Service is responsible for bootstrapping users. It includes the following changes:

- Added OpenTelemetry instrumentation to enable distributed tracing.
- Initialized a TracerProvider and set it as the tracer provider.
- Configured an AzureMonitorSpanExporter to send spans to Azure Application Insights.
- Added a BatchSpanProcessor to process and export spans in batches.
- Updated the code to use the TraceContextTextMapPropagator for propagating the span context in HTTP headers.
- Updated the error handling in the bootstrap_user function to print and handle exceptions properly.

## Bootstrap Service

The Bootstrap Service is responsible for performing the bootstrap operation. It includes the following changes:

- Added OpenTelemetry instrumentation to enable distributed tracing.
- Initialized a TracerProvider and set it as the tracer provider.
- Configured an AzureMonitorSpanExporter to send spans to Azure Application Insights.
- Added a BatchSpanProcessor to process and export spans in batches.
- Updated the code to use the TraceContextTextMapPropagator for propagating the span context in HTTP headers.
- Updated the error handling in the bootstrap function to print and handle exceptions properly.

## Docker Files

Docker files have been added for both the Core and Bootstrap services to facilitate running them in containers. The Docker files include the necessary steps to build the Docker images and run the services.

To build and run the services in Docker containers, follow these steps:

1. Make sure you have Docker installed on your machine.
2. Clone the repository.
3. Build the Docker image for the Core Service by executing the following command in the Core Service directory:


Please note that this is a simplified example, and you may need to customize the Docker files and configuration for your specific use case and Azure environment.


## Core Service
The Core Service is responsible for handling user requests and performing various operations. It authenticates tokens, calls the Bootstrap Service, and updates the database.

- Service URL:

Core Service: https://coreservice.azurewebsites.net/bootstrap-user?token=123&user=hello
Bootstrap Service
The Bootstrap Service is responsible for handling requests from the Core Service and interacting with external APIs and services.

- Service URL:

Bootstrap Service: https://bootstrapservice.azurewebsites.net/bootstrap

## Monitoring with Azure Application Insights
The services are monitored using Azure Application Insights, which provides valuable insights and telemetry data for troubleshooting and performance monitoring.








# app3_python

Simple 2 dummy microservices architecture using flask

## Services

### core_service

user request --> core_service --> authenticate token --> call_bootstrap_service --> update_database --> user

### bootstrap_service

request --> bootstrap_service --> extapi --> extapi404 --> redis --> return request

There is no real database, redis etc. Everything is just a simluation

## Getting started

`pip3 install -r requirements.txt`

Open 2 terminals

1. python3 core_service.py (8080 is open)
2. python3 bootstrap_service.py (8081 is open)

Your request should be something like this.
only token `123` is valid.

```bash
curl --location --request POST 'localhost:8080/bootstrap-user?token=123&user=hello'
```



