import unittest
from unittest.mock import patch
from app import app, db, Project, Message
from datetime import datetime

class TestHomepage(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Freelance Developer', response.data)
        self.assertIn(b'About', response.data)
        self.assertIn(b'Skills', response.data)
        self.assertIn(b'Contact', response.data)

    def test_dark_mode_toggle(self):
        response = self.app.get('/')
        self.assertNotIn(b'dark', response.data)

        response = self.app.get('/?theme=dark')
        self.assertIn(b'dark', response.data)

class TestProjectsGallery(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

        self.project1 = Project(
            title='Project 1',
            description='Description 1',
            image='project1.jpg',
            technologies=['React', 'Python']
        )
        self.project2 = Project(
            title='Project 2',
            description='Description 2',
            image='project2.jpg',
            technologies=['Vue', 'Flask']
        )
        db.session.add(self.project1)
        db.session.add(self.project2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_projects_gallery(self):
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Project 1', response.data)
        self.assertIn(b'Project 2', response.data)

    def test_filter_projects(self):
        response = self.app.get('/projects?technology=React')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Project 1', response.data)
        self.assertNotIn(b'Project 2', response.data)

class TestContactForm(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('app.send_email')
    def test_contact_form_submission(self, mock_send_email):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello, I would like to discuss a project.'
        }
        response = self.app.post('/contact', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for your message!', response.data)
        mock_send_email.assert_called_once_with(
            'john@example.com', 'New Message from Portfolio Website'
        )

        message = Message.query.first()
        self.assertEqual(message.name, 'John Doe')
        self.assertEqual(message.email, 'john@example.com')
        self.assertEqual(message.message,