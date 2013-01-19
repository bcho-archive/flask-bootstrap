#coding: utf-8

from flask import Blueprint

app = Blueprint('foo', __name__, template_folder='templates')
