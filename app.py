from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Initialize SQS and SNS clients
sqs_client = boto3.client('sqs', region_name='ap-southeast-2')
sns_client = boto3.client('sns', region_name='ap-southeast-2')

# SQS Queue URL
queue_url = 'https://sqs.ap-southeast-2.amazonaws.com/975049960102/sample_queue'

# SNS Topic ARN
topic_arn = 'arn:aws:sns:ap-southeast-2:975049960102:sample-sns'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']

    # Send message to SQS
    sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )

    # Publish message to SNS
    sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )

if __name__ == '__main__':
    app.run(debug=True)
