from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='45919d4f6d40ac95fbf5d4c200b51be3'
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:@localhost/details"
db= SQLAlchemy(app)

from Flask_App  import views