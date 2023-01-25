from crawlers.general import GeneralCrawler
from tools.AWS.sqs import Queue
import json


def lambda_handler(event, context):
    messages = [];
    for message in event["Records"]:
        messages.append({
            "receiptHandle": message['receiptHandle'],
            "body": json.loads(message['body'])
        })
    print(messages)

    for task in messages:
      crawler = GeneralCrawler()
      cname = task["body"]["crawlerName"]
      url =  task["body"]["storeUrl"]
      result = crawler.find_crawler(cname,url)
      print(result)
