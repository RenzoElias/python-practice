import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = os.getenv("FLASK_ENV")

HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASS')

# AWS CREDENTIALS
AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"