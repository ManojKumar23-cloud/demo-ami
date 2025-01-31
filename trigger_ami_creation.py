import boto3
import os

ssm = boto3.client('ssm')

def lambda_handler(event, context):
    response = ssm.start_automation_execution(
        DocumentName='golden-ami-ssm',
        Parameters={
            'BaseAmiId': ['ami-0c614dee691cbbf37'],  # Change to latest base AMI
            'SubnetId': ['subnet-006de4eb505674d0f'],
            'SecurityGroupId': ['sg-030b0f4d2dc7d18e6']
        }
    )
    return response
