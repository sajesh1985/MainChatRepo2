import boto3, uuid
from datetime import datetime

DYNAMO_REGION = "us-east-2"
TABLE_NAME = "chat-response-d"

dynamodb = boto3.resource("dynamodb", region_name=DYNAMO_REGION)
table = dynamodb.Table(TABLE_NAME)

def save_chat(prompt: str, response: str):
    item = {
        "id": str(uuid.uuid4()),
        "interactionId": str(uuid.uuid4()),
        "input": prompt,
        "response": response,
        "createdAt": datetime.utcnow().isoformat()
    }
    table.put_item(Item=item)
    return item
