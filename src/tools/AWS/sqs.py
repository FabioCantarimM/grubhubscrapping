import boto3
import os
import json

class Queue:

    def __init__(self) -> None:
        self.__sqs = boto3.client('sqs', region_name="us-west-2")
        self.__queue = os.getenv('QUEUE_NAME')
        self.__queueError = f"{os.getenv('QUEUE_NAME')}_Error"
        self.__nextQueue = os.getenv('NEXT_QUEUE_NAME')
    
    def getQueueUrl(self, queueName):
        response =  self.__sqs.get_queue_url(QueueName=queueName)
        return response["QueueUrl"]

    def getMessage(self):
        messages = self.__sqs.receive_message(QueueUrl=self.getQueueUrl(self.__queue), MaxNumberOfMessages=1)
        return messages['Messages']

    def sendMessage(self, message):
        self.deleteMessage(message['receiptHandle'])
        return self.__sqs.send_message(QueueUrl= self.getQueueUrl(self.__nextQueue), MessageBody=json.dumps(message['body']))

    def sendErrorMessage(self, message):
        self.deleteMessage(message['receiptHandle'])
        return self.__sqs.send_message(QueueUrl= self.getQueueUrl(self.__queueError), MessageBody=json.dumps(message['body']))

    def deleteMessage(self, receipt_handle):
        return self.__sqs.delete_message(QueueUrl= self.getQueueUrl(self.__queue), ReceiptHandle=receipt_handle)
    