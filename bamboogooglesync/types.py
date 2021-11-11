
import json
import os

import boto3
import click


class Secret(click.ParamType):
    def __init__(self, type=None) -> None:
        self.type = type
        
    def convert(self, value, param, ctx):
        if os.environ.get("IS_LAMBDA"):
            client = boto3.client(
                'secretsmanager'
            )
            response = client.get_secret_value(
                SecretId=value
            )            
            try:
                value = json.loads(response["SecretString"])
            except ValueError:
                value = response["SecretString"]  
        if self.type:
            value = self.type(value, param, ctx)
        return value
    
    @property
    def name(self):
        return self.type.name
