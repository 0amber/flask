from flask_restx import Namespace, fields, Resource
from app.models import Todo

# Namespaceの初期化
todo_namespace = Namespace("todos", description="Todoのエンドポイント")

# JSONモデルの定義
todo = todo_namespace.model(
    "Todo",
    {
        "id": fields.Integer(required=True, description="Todoを登録したユーザーID", example="0"),
        "todo": fields.String(required=True, description="やること", example="zerotodo"),
    },
)


@todo_namespace.route("/")
class TodoList(Resource):
    # todoモデルを利用して結果をパースしてリストで返す
    @todo_namespace.marshal_list_with(todo)
    def get(self):
        """
        Todoモデル全件取得

        Returns
        -------
        id : int
        タスクのID
        todo : String
        タスクの内容
        """
        return Todo.query.all()
