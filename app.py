from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    technologies = db.Column(db.String(200), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        projects = Project.query.all()
        return jsonify([project.serialize() for project in projects])
    elif request.method == 'POST':
        data = request.get_json()
        new_project = Project(
            title=data['title'],
            description=data['description'],
            image_url=data['image_url'],
            technologies=','.join(data['technologies'])
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.serialize()), 201

@app.route('/api/projects/<int:project_id>', methods=['GET', 'PUT', 'DELETE'])
def project(project_id):
    project = Project.query.get(project_id)
    if request.method == 'GET':
        return jsonify(project.serialize())
    elif request.method == 'PUT':
        data = request.get_json()
        project.title = data['title']
        project.description = data['description']
        project.image_url = data['image_url']
        project.technologies = ','.join(data['technologies'])
        db.session.commit()
        return jsonify(project.serialize())
    elif request.method == 'DELETE':
        db.session.delete(project)
        db.session.commit()
        return '', 204

@app.route('/api/messages', methods=['POST'])
def messages():
    data = request.get_json()
    new_message = Message(
        name=data['name'],
        email=data['email'],
        message=data['message']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.serialize()), 201

@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([message.serialize() for message in messages])

if __name__ == '__main__':
    app.run(debug=True)

FILENAME: frontend/src/App.js