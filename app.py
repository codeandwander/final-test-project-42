from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    technologies = db.Column(db.String(200), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        projects = Project.query.all()
        return jsonify([{
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'image': project.image,
            'technologies': project.technologies.split(',')
        } for project in projects])
    elif request.method == 'POST':
        data = request.get_json()
        project = Project(
            title=data['title'],
            description=data['description'],
            image=data['image'],
            technologies=','.join(data['technologies'])
        )
        db.session.add(project)
        db.session.commit()
        return jsonify({'message': 'Project added successfully'}), 201

@app.route('/api/projects/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def project(id):
    project = Project.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'image': project.image,
            'technologies': project.technologies.split(',')
        })
    elif request.method == 'PUT':
        data = request.get_json()
        project.title = data['title']
        project.description = data['description']
        project.image = data['image']
        project.technologies = ','.join(data['technologies'])
        db.session.commit()
        return jsonify({'message': 'Project updated successfully'})
    elif request.method == 'DELETE':
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    contact = Contact(
        name=data['name'],
        email=data['email'],
        message=data['message']
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/api/admin/contacts', methods=['GET'])
def admin_contacts():
    contacts = Contact.query.all()
    return jsonify([{
        'id': contact.id,
        'name': contact.name,
        'email': contact.email,
        'message': contact.message
    } for contact in contacts])

if __name__ == '__main__':
    app.run(debug=True)

FILENAME: frontend/src/App.js