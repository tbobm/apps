# tbobm/apps

[![Build Containers](https://github.com/tbobm/apps/actions/workflows/main.yaml/badge.svg)](https://github.com/tbobm/apps/actions/workflows/main.yaml)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A centralized collection of containers to use as example apps.

## API

### HTTP

#### Hello World

Path: [`./api/http/hello/`](./api/http/hello/)

Example usage:
```console
$ docker run -p 8000:5000 -d --rm ghcr.io/tbobm/apps:api-http-hello-latest
$ curl localhost:8000/health
OK
```

## SQS

### Producer

Path: [`./sqs/producer/`](./sqs/producer/)

Example usage:
```console
$ docker run -e SQS_QUEUE_URL="https://sqs.eu-west-1.amazonaws.com/111111111111/my-queue" \
  -it ghcr.io/tbobm/apps:sqs-producer-latest
```
