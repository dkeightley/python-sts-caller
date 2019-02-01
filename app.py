from flask import Flask, jsonify, Response
import boto3
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)
client = boto3.client('sts')

@app.route('/')
def index():
  try:
    response = client.get_caller_identity()["Arn"]
  except NoCredentialsError:
    response = "Unable to locate credentials"
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
