import boto3
import json
import logging
import os
import numpy
from botocore.exceptions import ClientError

from myapp import app

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def main(event, context):
    logging.info(event)

    s3 = boto3.client('s3')

    try:
        for record in event['Records']:
            s3_bucket_name = record['s3']['bucket']['name']
            s3_object_key = record['s3']['object']['key']
            logging.info('s3_bucket_name: %s' % s3_bucket_name)
            logging.info('s3_object_key: %s' % s3_object_key)

            response = s3.get_object(Bucket=s3_bucket_name, Key=s3_object_key)
            data = (json.loads(response['Body'].read()))
            print(data)

    except ClientError as ex:
        if ex.response['Error']['Code'] == 'NoSuchKey':
            logging.info('No existing file found')
        raise ex

    #print("Your numpy array: %s" % numpy.arange(15).reshape(3, 5))


def now(event, context):
    stats = dict()
    with open('stats.json') as f:
        stats = json.load(f)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "The current time is %s" % app.now(),
            "input": event,
            "s3_bucket": os.environ.get('S3_BUCKET_NAME'),
            "stats": stats
        })
    }


if __name__ == "__main__":
    main('', '')
    print(now('', ''))
