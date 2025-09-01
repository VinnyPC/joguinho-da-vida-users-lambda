import boto3
import os

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.getenv("USERS_TABLE", "Users")

class UserRepository:
    def __init__(self):
        self.table = dynamodb.Table(TABLE_NAME)

    def put(self, item):
        self.table.put_item(Item=item)

    def get(self, user_id):
        response = self.table.get_item(Key={"id": user_id})
        return response.get("Item")

    def scan(self):
        response = self.table.scan()
        return response.get("Items", [])

    def delete(self, user_id):
        self.table.delete_item(Key={"id": user_id})

    
    def add_missao(self, user_id, missao):
        response = self.table.update_item(
            Key={"id": user_id},
            UpdateExpression="SET missoesAtivas = list_append(if_not_exists(missoesAtivas, :empty_list), :nova)",
            ExpressionAttributeValues={
                ":nova": [missao],      
                ":empty_list": []
            },
            ReturnValues="UPDATED_NEW"
        )
        return response.get("Attributes")
