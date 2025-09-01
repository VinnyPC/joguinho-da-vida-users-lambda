import json
import uuid

class UserModel:
    def __init__(self, email, name, age, missoesAtivas=None, id=None):
        self.id = id or str(uuid.uuid4())
        self.email = email
        self.name = name
        self.age = age
        self.missoesAtivas = missoesAtivas or []  

    def to_item(self):
        return {
            "id": self.id,
            "email": self.email,  
            "name": self.name,
            "age": self.age,
            "missoesAtivas": self.missoesAtivas
        }

    @staticmethod
    def from_json(body):
        if isinstance(body, str):
            body = json.loads(body)
        return UserModel(
            id=body.get("id"),   
            email=body["email"],
            name=body["name"],
            age=body.get("age"),
            missoesAtivas=body.get("missoesAtivas", [])
        )
