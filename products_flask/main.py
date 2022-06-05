from sqlalchemy import UniqueConstraint
from flask import Flask

from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://devuser:kalman@db-flask/devdb'

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    prod_id = db.Column(db.Integer, primary_key=True)
    UniqueConstraint('user_id', 'prod_id', name='user_product_unique')


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
