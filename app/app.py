from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import Router

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:username@localhost:5432/assignment'


db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'hello_world'

Router.run(app);

if __name__ == "__main__":
    app.run(debug=True)