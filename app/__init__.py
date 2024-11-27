from flask import Flask

app = Flask(__name__) #(__name__, template_folder='view') faria o nome da pasta template ser view

from app import admin
from app import cliente