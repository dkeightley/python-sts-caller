from flask import Flask
import boto3
import signal
import sys
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)
client = boto3.client('sts')

def exit_gracefully(signumber, frame):
  print("Received signal", signumber, "cleaning up...")
  sys.exit(0)

@app.route('/')
def index():
  try:
    response = client.get_caller_identity()["Arn"]
  except NoCredentialsError:
    response = "Unable to locate credentials"
  return response

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, exit_gracefully)
    app.run(host='0.0.0.0',port=80,threaded=True)
