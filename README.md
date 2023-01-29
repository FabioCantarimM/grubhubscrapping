# Example of Crawler - Using AWS environment

[![Card](https://img.shields.io/badge/Git%20Hub%20-%23323330.svg?&style=for-the-badge&logo=cards%20estrelas&logoColor=black&color=FFB800)](https://github.com/FabioCantarimM/webscrapping)
[![Badge](https://img.shields.io/badge/LinkedIn%20-%23323330.svg?&style=for-the-badge&logo=badges&logoColor=black&color=006DEC)](https://www.linkedin.com/in/fabiocmelo/)

An example of web scraping collecting data from GrubHub, using AWS environment, by receiving Lambda trigger from AWS SQS, and saving CSVs into AWS S3; It could work in a production environment, but it needs a little more enforce to turn generic the way to extract data from JSON and send alerts when schema changes.

**GrubHub** - Two steps are required to collect data from it: First, obtain Bearer Token authorization, and then collect restaurant information by using the ID included in the URL.

## ✅ TODO

Refact Extract Function - The solution could easily collect data from a new schema by using a dictionary of rules pattern. (24 hours of work)

Implement Proxy -  To avoid get blocked by the service is a good practice implements a proxy system to improve performance and reduce error in high volume requests situation (16 hours of work)

Create logging System - To keep an eye on that solution A logging solution based on AWS Opensearch could be a good option for tracking problems and creating dynamic maps to understand data and proxy problems. ( 40 hours of work)

CD/CI - Creating a pipeline with Terraform or a GitHub action to deploy it to AWS automatically (6 hours of work)

Test It - Create unitary tests to validate. (24 hours of work)

## 📃 AWS Architecture

- AWS SQS
- AWS Lambda
- AWS S3

## How to run a debug mode

In debug.py, you can replace URLs in message bodies.

```bash
python src/debug.py
```

## Message Example

The message has two properties: crawler Name and store Url. The first informs what crawler will be running, and the second what store will be collected.

```JSON
{
  "crawlerName":"GrubHub",
  "storeUrl":"https://www.grubhub.com/restaurant/mezeh-optimist-hall-340-e-16th-st-unit-r201-charlotte/2809951"
}
```
## Files Example

Every store generates two files:

1 - Menu information

```CSV
  id| category_name| item_name| item_description| item_price
```

2 - Optional information

```CSV
  product_id| modifier_id| group_name| modifier_min| modifier_max|options
```

## Development

Create 3 Queues in AWS SQS:

  1 - Queue that will activate AWS Lambda

  2 - Error Queue to receive any unfinished tasks
  
  3 - The following queue will receive completed tasks.

Make an AWS Lambda function that calls main.lambda handler. Set the first queue as a trigger;

To receive into AWS S3, create a bucket or add a folder to an existing bucket.