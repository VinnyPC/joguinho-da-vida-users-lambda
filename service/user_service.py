import json
from repository.user_repository import UserRepository
from model.user_model import UserModel
from decimal import Decimal


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    @staticmethod
    def decimal_default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError

    def create_user(self, body):
        user = UserModel.from_json(body)
        self.repo.put(user.to_item())
        return {
            "message": "Usuário criado com sucesso",
            "user": user.to_item()
        }

    def get_user(self, user_id):
        item = self.repo.get(user_id)
        if not item:
            raise Exception("Usuário não encontrado")
        return json.loads(json.dumps(item, default=self.decimal_default))

    def list_users(self):
        users = self.repo.scan()
        return json.loads(json.dumps(users, default=self.decimal_default))

    def update_user(self, body):
        user = UserModel.from_json(body)
        self.repo.put(user.to_item()) 
        return {
            "message": "Usuário atualizado",
            "user": user.to_item()
        }

    def delete_user(self, user_id):
        self.repo.delete(user_id)
        return {"message": "Usuário deletado"}

    def add_missao(self, body):
        if isinstance(body, str):
            body = json.loads(body)

        user_id = body["id"]
        missoes = body.get("missoesAtivas", [])

        if not missoes:
            raise Exception("Nenhuma missão fornecida")

        missao = missoes[0]

        updated = self.repo.add_missao(user_id, missao)
        return {
            "message": "Missão adicionada com sucesso",
            "user": json.loads(json.dumps(updated, default=self.decimal_default))
        }
#criar usuário no dynamo quando for criado no cognito
    def handle_cognito_event(self, event):
        try:
            user_id = event["userName"]
            email = event["request"]["userAttributes"].get("email")
            name = event["request"]["userAttributes"].get("name", "")

            item = {
                "id": user_id,
                "email": email,
                "name": name,
                "age": 0,
                "missoesAtivas": []  
            }

            self.repo.put(item)

            print(f"[Cognito] Usuário {user_id} inserido no Dynamo com sucesso")

        except Exception as e:
            print(f"[Cognito] Erro ao inserir usuário no Dynamo: {str(e)}")

        return event
