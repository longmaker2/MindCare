# MindCare Burundi

![image](https://github.com/user-attachments/assets/3185023a-261d-44c0-a634-da654600586d)


# MindCare - Mental Health Support Platform

## Overview
MindCare is a comprehensive mental health platform designed to support users in managing their well-being. It offers educational resources, access to professional support, and self-assessment quizzes. The platform enables users to take quizzes to evaluate their mental health, schedule appointments with mental health professionals, and explore curated content related to mental wellness. MindCare aims to provide a safe and accessible space for individuals to gain insights into their mental health and seek guidance when needed.

## Features
- **Personalized Mental Health Dashboard** – Users can track their mental well-being, set personal goals, and access relevant resources.
- **Book Appointment** – Schedule sessions with licensed mental health professionals for personalized support.
- **Mental Health Quizzes** – Quizzes about mental health organize in each category
- **Mental health support space** – Join a safe and moderated community where users can share experiences, seek advice, and provide support to others.
- **Contact** – Provides crisis intervention information and direct contact with professional helplines.
- **Mental Health Ressource Center** – Provides curated content to promote well-being and positive mental habits.
  
# Screenshots of the app interface can be found this the **designs folder** of this repository

https://github.com/Ericanshimir/MindCare/tree/main/MindCare/designs

# Link to the video showcasing MindCare App functionalities.

https://youtu.be/P6tB0ob5rhE

# Link to the github Repository

https://github.com/Ericanshimir/MindCare
## Technologies Used

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Database: PostgreSQL

## Installation and Setup
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- PostgreSQL
- Docker (optional for containerized deployment)

### Steps to Install
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Ericanshimir/MindCare.git
   cd MindCare
   ```
2. # Install dependencies
```bash
 pip install -r requirements.txt
```
3. **Create a Virtual Environment and Activate It**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
5. **Set Up Database**
   ```sh
   python manage.py migrate
   ```
6. **Run the Application**
   ```sh
   python manage.py runserver
   ```
7. **Access the Application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

8.  # Navigation & UI Details

**Home Page**: Overview of the platform.

**Dashboard**: Personalized user experience and tracking.

**Quizzes Page**: Take self-assessment quizzes.

**Appointment Booking**: Schedule a session with a professional.

## Usage Guide
- **Sign up/Login** to access mental health resources.
- **Schedule appointment** with professionals.
- **Use MindCare Ressource Center meaterials** such as books, articles and videos
- **Engage in the community** for peer support and discussions.
- **Take quizzes** to see your improvemnt.

# Database Schema:
 ![database image](https://github.com/user-attachments/assets/1003a339-3ea5-478d-b4e7-53446eecc30b)


# Deployment Plan for MindCare

# Overview

This deployment plan outlines the steps to deploy the MindCare application, which consists of a Django backend and a JavaScript (HTML, CSS) frontend. The chosen deployment stack ensures scalability, security, and ease of maintenance.

# Deployment Stack

**Backend (Django + API)**: Render provides a simple and scalable hosting solution with a free-tier PostgreSQL database, making it ideal for deploying and managing Django applications.

**Frontend (HTML, JavaScript, and CSS)**: Vercel offers fast, reliable, and free static hosting, making it the best choice for deploying the MindCare frontend efficiently.

**Database (PostgreSQL)**: Render also manages PostgreSQL databases, ensuring secure and optimized database performance for the backend.

# Step-by-Step Deployment Plan

**Step 1**: Deploy Backend on Render

1️. Sign up on Render

2️. Create a New Project → Click Deploy from GitHub

3️. Select Your MindCare Backend Repo (Django)

4️. Add Environment Variables:
```bash
DJANGO_SECRET_KEY=my-secret-key
DATABASE_URL=my-postgres-url
ALLOWED_HOSTS=my-railway-app-url
```
5️. Run Migrations:
```bash
python manage.py migrate
```
6️. Run the Server:
```bash
python manage.py runserver
```
7️. Copy the Render Backend URL for frontend use.

**Step 2**: Deploy Frontend on Vercel

1️. Sign up on Vercel

2️. Click 'New Site from Git' → Select Frontend GitHub Repo

3️. Set API URL in Frontend (fetch() calls should use your Render backend URL)

4️. Deploy & Test:
```bash
Simply upload static HTML, CSS, and JavaScript files
```

# Final Steps

1. Test API Calls from Frontend → Backend
2. Ensure CORS is Configured in Django (settings.py)
3. Monitor Performance & Logs on Render and Vercel

## Contribution
To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to your branch: `git push origin feature-branch-name`.
5. Open a Pull Request.

## Contact
For any inquiries, suggestions, or feedback, feel free to open an issue on GitHub or contact us via email at nshimirimanaerica@gmail.com.
