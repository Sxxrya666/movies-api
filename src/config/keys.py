import os
from dotenv import load_dotenv

load_dotenv()

jwt_key = os.getenv("JWT_KEY")
jwt_algo = os.getenv("JWT_ALGORITHM")
db_username = os.getenv("MYSQL_USERNAME")
db_password = os.getenv("MYSQL_PASSWORD")
db_name = os.getenv("MYSQL_DB_NAME")
API_VERSION = '1'