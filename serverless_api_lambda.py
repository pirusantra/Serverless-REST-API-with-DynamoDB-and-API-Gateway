import json
import boto3
import os
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    # Parse request body
    body = json.loads(event['body']) if event.get('body') else {}

    # CREATE
    if http_method == 'POST':
        table.put_item(Item=body)
        return respond(200, "Task created successfully")

    # READ
    elif http_method == 'GET':
        params = event.get('queryStringParameters')
        if params and 'id' in params:
            response = table.get_item(Key={'id': params['id']})
            return respond(200, response.get('Item', {}))
        else:
            response = table.scan()
            return respond(200, response.get('Items', []))

    # UPDATE
    elif http_method == 'PUT':
        if 'id' not in body:
            return respond(400, "Task ID is required for update")
        update_expression = "set "
        expr_attr = {}
        if 'title' in body:
            update_expression += "title=:t, "
            expr_attr[':t'] = body['title']
        if 'status' in body:
            update_expression += "status=:s, "
            expr_attr[':s'] = body['status']
        update_expression = update_expression.rstrip(', ')
        table.update_item(
            Key={'id': body['id']},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expr_attr,
            ReturnValues="UPDATED_NEW"
        )
        return respond(200, "Task updated successfully")

    # DELETE
    elif http_method == 'DELETE':
        if 'id' not in body:
            return respond(400, "Task ID is required for deletion")
        table.delete_item(Key={'id': body['id']})
        return respond(200, "Task deleted successfully")
    
    else:
        return respond(405, "Method not allowed")


def respond(status, message):
    return {
        'statusCode': status,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(message)
    }
