from dataclasses import dataclass

import requests
from sqlalchemy import UniqueConstraint
from flask import (Flask, jsonify, abort, )

from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

import os

from config import Config

from producer import publish

app = Flask(__name__)
CORS(app)

# Environment Variables
conf = Config()
HOST = "db-flask"
USER = Config.USER
DEVDB = Config.DEVDB
PASS = Config.PASS

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASS}@{HOST}/{DEVDB}"

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    user_id: int
    prod_id: int
    user_id = db.Column(db.Integer, primary_key=True)
    prod_id = db.Column(db.Integer, primary_key=True)
    UniqueConstraint('user_id', 'prod_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    # req = requests.get("http://docker.for.mac.localhost:8000/api/user")
    req = requests.get("http://host.docker.internal:8000/api/user")
    json = req.json()

    try:
        productUser = ProductUser(
            user_id=json['id'],
            prod_id=id
        )
        db.session.add(productUser)
        db.session.commit()

        # event
        publish('product_liked', id)
    except BaseException as e:
        print(e)

        abort(400, 'You already liked this product.')

    print(req)
    return jsonify({
        'message': 'success',
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
