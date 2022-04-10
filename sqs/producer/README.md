# SQS producer

Send messages to an AWS SQS Queue.

## Configuration

Set the `SQS_QUEUE_URL` environment variable to the value of the SQS Queue
that will be used as the target.

## Usage

```console
docker run -e SQS_QUEUE_URL="https://sqs.<aws_region>.amazonaws.com/111111111111/my-queue" \
  -it ghcr.io/tbobm/apps:sqs-producer-latest
```
