import os

import time

import boto3

# https://sqs.<aws_region>.amazonaws.com/111111111111/sqs-keda-demo
QUEUE_URL = os.environ.get('SQS_QUEUE_URL')

def main():
    # Create SQS client
    sqs = boto3.client('sqs')

    # Receive message from SQS queue
    while True:
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        messages = response.get('Messages', None)
        if messages is None:
            print('no message, sleeping')
            time.sleep(1)
            continue

        message = messages[0]
        receipt_handle = message['ReceiptHandle']

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )
        print('Received and deleted message: %s' % message)

if __name__ == '__main__':
    main()
