from flask import Flask, request, render_template, redirect
from  flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://MyDB.sqlite'
db = SQLAlchemy(app)
login_manager=LoginManager(app)

#dont know if i need a DB
class User(UserMixin, db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error inserting user: {e}")

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
'''

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

app.run(debug=True)