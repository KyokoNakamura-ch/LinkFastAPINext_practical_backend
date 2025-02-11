import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# SSL証明書のパス設定（相対パスを使用）
ssl_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DigiCertGlobalRootCA.crt.pem')

# データベース接続情報
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# MySQLのURL構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# エンジンの作成
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={"ssl": {"ca": ssl_path}}  # SSL証明書を相対パスで指定
)