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

