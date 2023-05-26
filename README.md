## Python Review

### Run ia_test

```bash
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate

pip3 install -r requirements.txt

python application.py

pip3 freeze > requirements.txt
```

### Virtual Env

```bash
pip3 install
    flask
    Flask-SQLAlchemy
    flask_marshmallow
    flask_cors
    python-dotenv
    pymysql
    marshmallow-sqlalchemy
```

## Credenciales

### Credenciales de desarrollo

```bash
FLASK_ENV="development"
FLASK_ENV = "development"

DATABASE_URI="mysql+pymysql://USER:PASSWORD@DB_HOST/DB_NAME"
DB_HOST="dadsrerws.shthdsfg.us-east-2.rds.amazonaws.com"
DB_NAME="db_ress"
DB_USER="sadds"
DB_PASS="345g4ghsfdgd

AWS_ACCOUNT_ID="58485852"
AWS_BUCKET_NAME="asdasd-dev"

# TWILIO
ACCOUNT_SID = ""
AUTH_TOKEN = ""
```