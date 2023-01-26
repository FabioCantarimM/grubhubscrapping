from crawlers.general import GeneralCrawler
from tools.AWS.sqs import Queue
from tools.CSV.csv import createFile
import json

def lambda_handler(event, context):
  messages = [];
  for message in event["Records"]:
      messages.append({
          "receiptHandle": message['receiptHandle'],
          "body": json.loads(message['body'])
      })

  paths = []
  for task in messages:
    crawler = GeneralCrawler()
    cname = task["body"]["crawlerName"]
    url =  task["body"]["storeUrl"]
    result = crawler.find_crawler(cname,url)
    paths.append(createFile(result))
    
  print(paths)
