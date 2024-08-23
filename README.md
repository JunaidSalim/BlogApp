# BlogApp



## About

Our Blog Management Platform is a dynamic web application designed to empower users to create, edit, and manage their blogs with ease. The platform offers a seamless experience by integrating a robust backend built with Django and a responsive frontend crafted using React. It caters to both novice and experienced bloggers, providing an intuitive interface for managing blog content and interacting with readers.

## Key Features

- **User Authentication:** Easily register and log in to the platform, with secure authentication managed using JWT tokens. Personal data is protected with robust security measures.
  
- **Dashboard:** Personalized dashboard displaying all your blog posts, including details such as title, content, author, and publication date.

- **Blog Management:** Comprehensive tools for creating, editing, and deleting blog posts. The ReactQuill editor provides a smooth, user-friendly writing experience.

- **Comments Section:** Engage with readers through a dedicated comments section. Readers can leave comments, with each comment displaying relevant user information.

- **Responsive Design:** Built with a responsive design to ensure optimal performance across all devices, from mobile phones to desktop monitors.

## Technology Stack

- **Frontend:** React and Bootstrap for building the user interface.
- **Backend:** Django, powered by Django REST Framework, to manage server-side logic and API endpoints.
- **Database:** PostgreSQL for reliable and scalable data storage.
- **Authentication:** Secure user authentication is managed through JSON Web Tokens (JWT).

## Installation and Setup

### Prerequisites

- Node.js (for frontend)
- Python (for backend)
- PostgreSQL (for database)

### Frontend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JunaidSalim/BlogApp
    ```
2. Navigate to the frontend directory:
    ```bash
   cd BlogApp/frontend
    ```
3. Install dependencies:
    ```bash
   yarn install
    ```
4. Start the development server:
    ```bash
   yarn start
    ```
### Backend Setup
1. Navigate to the backend directory:
    ```bash
   cd BlogApp/backend
    ```
2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   venv\Scripts\activate # On Windows
   source venv/bin/activate # On Mac & Linux
   ```

3. Install dependencies:
    ```bash
   pip install -r requirements.txt
    ```

4. Configure the PostgreSQL database:
   <br> Update the database settings in backend/settings.py.

5. Apply migrations:
    ```bash
   python manage.py migrate
    ```

6. Create a superuser:
    ```bash
   python manage.py createsuperuser
    ```

5. Start the Django development server:
    ```bash
   python manage.py runserver
    ```

## Contributing

Feel free to submit issues, fork the repository, and make pull requests. We welcome contributions and feedback from the community.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

For any questions or support, please reach out to junaidsaleem986@gmail.com.
