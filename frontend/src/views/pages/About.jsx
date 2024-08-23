import React from "react";
import Header from "../partials/Header";
import Footer from "../partials/Footer";
function About() {
    return (
        <>
            <Header />

            <section class="container mt-5">
        <div class="row">
            <div class="col-lg-12">
                <h2 class="text-center mb-4">About Blog Management Platform</h2>
                <p class="lead">
                    Our Blog Management Platform is a dynamic web application designed to empower users to create, edit, and manage their blogs with ease. The platform offers a seamless experience by integrating a robust backend built with Django and a responsive frontend crafted using React. The application is designed to cater to both novice and experienced bloggers, providing an intuitive interface for managing blog content and interacting with readers.
                </p>
            </div>
        </div>

        <div class="row mt-4">
            <div class="col-lg-12">
                <h4>Key Features</h4>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                        <strong>User Authentication:</strong> Users can easily register and log in to the platform, with their authentication state securely managed using JWT tokens. The platform ensures secure access and personal data protection.
                    </li>
                    <li class="list-group-item">
                        <strong>Dashboard:</strong> Upon logging in, users are greeted with a personalized dashboard displaying all their blog posts. Here, they can quickly view details such as the title, content, author, and publication date of each post.
                    </li>
                    <li class="list-group-item">
                        <strong>Blog Management:</strong> The platform provides comprehensive tools for creating, editing, and deleting blog posts. Users can compose rich-text content using the ReactQuill editor, offering a smooth and user-friendly writing experience.
                    </li>
                    <li class="list-group-item">
                        <strong>Comments Section:</strong> Interaction is key, and the platform allows users to engage with their audience through a dedicated comments section. Readers can leave comments on blogs, with each comment displaying the relevant user information.
                    </li>
                    <li class="list-group-item">
                        <strong>Responsive Design:</strong> The application is built with a responsive design, ensuring it looks great and functions flawlessly on devices of all sizes, from mobile phones to desktop monitors.
                    </li>
                </ul>
            </div>
        </div>

        <div class="row mt-4">
            <div class="col-lg-12">
                <h4>Technology Stack</h4>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                        <strong>Frontend:</strong> React for building the user interface, Redux for efficient state management, and Axios for handling API calls.
                    </li>
                    <li class="list-group-item">
                        <strong>Backend:</strong> Django, powered by the Django REST Framework, to manage the server-side logic and API endpoints.
                    </li>
                    <li class="list-group-item">
                        <strong>Database:</strong> PostgreSQL for reliable and scalable data storage.
                    </li>
                    <li class="list-group-item">
                        <strong>Authentication:</strong> Secure user authentication is managed through JSON Web Tokens (JWT), ensuring secure and persistent login sessions.
                    </li>
                </ul>
            </div>
        </div>
    </section>

            <Footer />
        </>
    );
}

export default About;
