#!/usr/bin/env python

import boto3
import sys
import argparse
from boto3.session import Session
 
parser = argparse.ArgumentParser(description='Generates an pre-signed_url of the S3 object')
parser.add_argument('bucket',
                    help='Bucket name')
parser.add_argument('key',
                    help='Key name')
parser.add_argument('duration',
                    help='Duration of publication [sec]')
parser.add_argument('-p', '--profile', default='default',
                    help='Profile of aws credential')

args = parser.parse_args()

bucket = args.bucket
key = args.key
duration = args.duration
profile = args.profile
 
session = Session(profile_name=profile)
s3 = session.client('s3')

print(s3.generate_presigned_url(
  ClientMethod = 'get_object',
  Params = {'Bucket' : bucket, 'Key' : key},
  ExpiresIn = duration,
  HttpMethod = 'GET'))
