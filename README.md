


# 🚀 User Lambda - Joguinho da Vida

Lambda responsável por gerenciar usuários e missões no projeto **Joguinho da Vida**, integrando:
- **Amazon Cognito** (criação automática de usuários no DynamoDB ao cadastrar no User Pool)
- **Amazon DynamoDB** (persistência de dados de usuários e missões)
- **API Gateway** (exposição de endpoints REST para operações CRUD)

---

## 📂 Estrutura do projeto

```

.
├── service/
│   └── user\_service.py      # Regras de negócio e integração com DynamoDB
├── repository/
│   └── user\_repository.py   # Acesso ao DynamoDB
├── utils/
│   └── response.py          # Helpers de formatação de respostas
├── model/
│   └── user\_model.py        # Classe de usuário (mapeamento JSON <-> DynamoDB)
├── lambda\_function.py       # Handler principal da Lambda
└── requirements.txt         # Dependências Python

````

---

## ⚙️ Funcionalidades

### 🔑 Integração com Cognito
- Trigger executado no **PostConfirmation**.
- Cria automaticamente um registro no DynamoDB com estrutura padrão:
```json
{
  "id": "cognito-user-id",
  "email": "email@exemplo.com",
  "name": "Nome do Usuário",
  "age": 0,
  "missoesAtivas": []
}
````

### 🌐 Endpoints via API Gateway

| Método | Caminho              | Descrição                        |
| ------ | -------------------- | -------------------------------- |
| POST   | `/users`             | Cria um usuário                  |
| POST   | `/users/add-mission` | Adiciona uma missão a um usuário |
| GET    | `/users`             | Lista todos os usuários          |
| GET    | `/users/{id}`        | Busca um usuário por ID          |
| PUT    | `/users`             | Atualiza um usuário              |
| DELETE | `/users/{id}`        | Remove um usuário                |

---


## 🛠️ Tecnologias usadas

* **Python 3.9+**
* **AWS Lambda**
* **Amazon DynamoDB**
* **Amazon Cognito**
* **Amazon API Gateway**

