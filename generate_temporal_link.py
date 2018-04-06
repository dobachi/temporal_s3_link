#!/usr/bin/env python

import boto3
import sys
import argparse
 
parser = argparse.ArgumentParser(description='Generates an pre-signed_url of the S3 object')
parser.add_argument('bucket',
                    help='Bucket name')
parser.add_argument('key',
                    help='Key name')
parser.add_argument('duration',
                    help='Duration of publication [sec]')

args = parser.parse_args()

bucket = args.bucket
key = args.key
duration = args.duration
 
s3 = boto3.client('s3')

print(s3.generate_presigned_url(
  ClientMethod = 'get_object',
  Params = {'Bucket' : bucket, 'Key' : key},
  ExpiresIn = duration,
  HttpMethod = 'GET'))
