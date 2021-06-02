class DevelopmentConfig:
    # Amazon RDS DBへ接続


    username = 'admin'
    db_pasword = '**@*'
    endpoint = '****.rds.amazonaws.com'
    db_instance = 'lambdaTestDB'
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(username, db_pasword, endpoint, db_instance)
    # TRACK_MODIFICATION機能を無効化
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemyからRDSへの同時接続の最大数
    SQLALCHEMY_MAX_OVERFLOW = 10000
    # JSONレスポンス日本語表示対応
    JSON_AS_ASCII = False
    # Swaggerのデフォルト表示形式をListにする
    SWAGGER_UI_DOC_EXPANSION = 'list'
    # Validationの有効化
    RESTX_VALIDATE = True


Config = DevelopmentConfig
