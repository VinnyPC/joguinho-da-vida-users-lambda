import json
from service.user_service import UserService
from utils.response import success, error

service = UserService()

def lambda_handler(event, context):
    try:
        if "triggerSource" in event and "userPoolId" in event:
            print("Evento Cognito detectado:", event["triggerSource"])
            return service.handle_cognito_event(event)


        method = event.get("httpMethod")
        path = event.get("path", "")
        body = event.get("body")

        if "triggerSource" in event and "userPoolId" in event:
            print("Evento Cognito detectado:", event["triggerSource"])




        if body and isinstance(body, str):
            body = json.loads(body)

        if method == "POST":
            if path.endswith("/add-mission"):

                return success(service.add_missao(body), 200)
            else:

                return success(service.create_user(body), 201)

        elif method == "GET":
            path_params = event.get("pathParameters") or {}
            user_id = path_params.get("id")
            if user_id:
                return success(service.get_user(user_id))
            else:
                return success(service.list_users())

        elif method == "PUT":
            return success(service.update_user(body))

        elif method == "DELETE":
            path_params = event.get("pathParameters") or {}
            user_id = path_params.get("id")
            if not user_id:
                return error("Id não informado", 400)
            return success(service.delete_user(user_id))

        else:
            return error("Método não suportado", 405)

    except Exception as e:
        return error(str(e), 500)
