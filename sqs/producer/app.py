import os
from time import sleep

import boto3

# https://sqs.<aws_region>.amazonaws.com/111111111111/my-queue
QUEUE_URL = os.environ.get('SQS_QUEUE_URL')

def main():
    # Create SQS client
    sqs = boto3.client('sqs')

    while True:
        send_message(sqs)
        sleep(5)

def send_message(sqs_client):
    # Send message to SQS queue
    response = sqs_client.send_message(
        QueueUrl=QUEUE_URL,
        DelaySeconds=1,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )
    print(response['MessageId'])


if __name__ == "__main__":
    main()
