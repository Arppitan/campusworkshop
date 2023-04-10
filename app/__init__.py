"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqulou9tun42u4u680-a.oregon-postgres.render.com",
        database="campusworkshop",
        user="campusworkshop_user",
        password="y9QCg2xgwzUqyjiseMNmsP9lLjUmZbUZ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
