# Final Test Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
5. [API Documentation](#api-documentation)
6. [User Guides](#user-guides)
    - [Frontend](#frontend)
    - [Backend](#backend)
7. [Deployment](#deployment)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview
This is a modern portfolio website for a freelance developer, built with React and Tailwind CSS for the frontend, and Python Flask for the backend API.

The main requirements for the project are:

1. **Homepage**:
   - Hero section with name and title
   - Brief introduction/about section
   - Skills showcase with icons
   - Contact form at the bottom

2. **Projects Gallery**:
   - Grid layout showing project cards
   - Each card has image, title, description
   - Click to view project details
   - Filter projects by technology

3. **Backend Features**:
   - API to manage projects (add, edit, delete)
   - Contact form submission handling
   - Store messages in database
   - Admin panel to view messages

4. **Design Requirements**:
   - Dark mode toggle
   - Fully responsive design
   - Smooth animations
   - Modern, clean aesthetic

## Features
- **Homepage**:
  - Hero section with name and title
  - Brief introduction/about section
  - Skills showcase with icons
  - Contact form at the bottom
- **Projects Gallery**:
  - Grid layout showing project cards
  - Each card has image, title, description
  - Click to view project details
  - Filter projects by technology
- **Backend**:
  - API to manage projects (add, edit, delete)
  - Contact form submission handling
  - Store messages in database
  - Admin panel to view messages
- **Design**:
  - Dark mode toggle
  - Fully responsive design
  - Smooth animations
  - Modern, clean aesthetic

## Technologies Used
- **Frontend**:
  - React
  - Tailwind CSS
- **Backend**:
  - Python Flask
  - SQLAlchemy (for database management)

## Getting Started

### Prerequisites
- Node.js (version 14 or later)
- Python (version 3.7 or later)
- PostgreSQL (for the database)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/final-test-project.git
```

2. Install frontend dependencies:
```bash
cd final-test-project/frontend
npm install
```

3. Install backend dependencies:
```bash
cd ../backend
pip install -r requirements.txt
```

4. Set up the database:
```bash
# Create a new PostgreSQL database
# Update the database connection string in the backend/config.py file

# Run database migrations
cd backend
flask db upgrade
```

5. Start the development servers:
```bash
# Start the frontend
cd frontend
npm start

# Start the backend
cd ../backend
flask run
```

The frontend will be available at `http://localhost:3000`, and the backend API at `http://localhost:5000`.

## API Documentation
The API documentation can be found in the [API Documentation](api-documentation.md) file.

## User Guides
### Frontend
The user guide for the frontend can be found in the [Frontend User Guide](frontend-user-guide.md) file.

### Backend
The user guide for the backend can be found in the [Backend User Guide](backend-user-guide.md) file.

## Deployment
The deployment instructions can be found in the [Deployment](deployment.md) file.

## Contributing
If you would like to contribute to this project, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License
This project is licensed under the [MIT License](LICENSE).