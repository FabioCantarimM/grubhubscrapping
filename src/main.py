from crawlers.general import GeneralCrawler
from tools.AWS.sqs import Queue
from tools.AWS.s3 import upload_files
from tools.CSV.csv import createFile
import json

#todo: START FROM LAMBDA TRIGGER - DONE
#todo: GET DATA FROM GRUBHUB - DONE
#todo: CONVERT DATA INTO A DICT - DONE
#todo: CREATE FILE - DONE
#todo: UPLOAD INTO S3 - DONE
#todo: SEND MESSAGE TO NEXT STEP - DONE

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


  resp = upload_files(paths)

  sqs = Queue()
  if all(resp):
    for message in messages:
      sqs.sendMessage(message["body"])
  else:
    for message in messages:
      sqs.sendErrorMessage(message["body"])
