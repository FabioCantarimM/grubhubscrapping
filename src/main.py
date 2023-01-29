from crawlers.general import GeneralCrawler
from tools.AWS.sqs import Queue
from tools.CSV.csv import createFile
import json

#todo: START FROMA LAMBDA TRIGGER - DONE
#todo: GET DATA FPOM GRUBHUB - DONE
#todo: CONVERT DATA INTO A DICT - DONE
#todo: CREATE FILE - DONE
#todo: UPLOAD INTO S3 - X
#todo: SEND MESSAGE TO NEXT STEP - X

def lambda_handler(event, context):
  messages = []
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
