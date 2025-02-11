# MindCare Burundi

![image](https://github.com/user-attachments/assets/3185023a-261d-44c0-a634-da654600586d)


# MindCare - Mental Health Support Platform

## Overview
MindCare is a digital mental health platform designed to provide users with accessible mental health resources, expert guidance, interactive tools, and a safe space for self-improvement. The application aims to bridge the gap between mental health support and those in need through a combination of self-help tools, professional consultations, and community engagement.

## Features
- **Personalized Mental Health Dashboard** – Users can track their mental well-being, set personal goals, and access relevant resources.
- **Therapist Consultation** – Schedule sessions with licensed mental health professionals for personalized support.
- **Self-Help Resources** – Access articles, videos, and exercises for stress management, anxiety relief, and emotional well-being.
- **Interactive Mental Health Tools** – Includes mood tracking, guided meditation, journaling, and cognitive exercises.
- **Community Support** – Join a safe and moderated community where users can share experiences, seek advice, and provide support to others.
- **Emergency Support** – Provides crisis intervention information and direct contact with professional helplines.
- **Daily Mental Health Tips** – Provides curated content to promote well-being and positive mental habits.
- **Privacy and Security** – Ensures user confidentiality with secure authentication and encrypted data storage.

## Technologies Used

Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: PostgreSQL

## Intended Platform of Deployment
MindCare is designed to be deployed on **Netlify**, a modern deployment platform optimized for frontend applications. Netlify provides continuous deployment, serverless functions, and a global CDN for fast performance.

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
2. **Create a Virtual Environment and Activate It**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Database**
   ```sh
   python manage.py migrate
   ```
5. **Run the Application**
   ```sh
   python manage.py runserver
   ```
6. **Access the Application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage Guide
- **Sign up/Login** to access mental health resources.
- **Schedule therapy sessions** with professionals.
- **Use self-help tools** such as journaling, mood tracking, and guided meditation.
- **Engage in the community** for peer support and discussions.
- **Chat with the AI-powered chatbot** for instant mental health assistance.
- **Read daily mental health tips** to improve emotional well-being.

## Contribution
We welcome contributions from the community! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to your branch: `git push origin feature-branch-name`.
5. Open a Pull Request.

## Contact
For any inquiries, suggestions, or feedback, feel free to open an issue on GitHub or contact us via email at nshimirimanaerica@gmail.com.

