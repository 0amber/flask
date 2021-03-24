from flask_restx import Api
from app.apis.todo import todo_namespace

# API情報を指定して初期化
api = Api(title="Test API", version="1.0", description="Swaggerを統合したREST APIのサンプル")

api.add_namespace(todo_namespace)
