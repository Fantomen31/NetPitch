# **NetPitch**

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation & Setup](#installation--setup)
5. [Usage](#usage)
6. [Database Schema](#database-schema)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [Credits](#credits)

## **Project Overview**

**NetPitch** is a platform that facilitates collaboration between writers and producers on media projects such as films and TV shows. The platform allows users to create profiles, submit pitch decks, request collaborations, and manage project details, creating a seamless workflow for professionals in the entertainment industry.

### **Purpose**
NetPitch aims to bridge the gap between writers and producers by providing a collaborative space where creative ideas can be shared, pitched, and developed into full-scale media projects.

### **Target Audience**
NetPitch is designed specifically for film and TV writers who want to pitch their ideas to producers, as well as for producers and production companies who are look to discover and collaborate on new projects.

### **Core Features**
- **User Profiles**: Writers and producers can create and manage their professional profiles.
- **Pitch Deck Submission**: Writers can submit pitch decks to showcase their project ideas.
- **Collaboration Requests**: Producers can send collaboration requests to writers, and writers can manage those requests.
- **Project Management**: Users can view and manage all submitted pitch decks and collaboration statuses.
  
### **Technologies Used**
NetPitch leverages a variety of modern web technologies to deliver a robust and scalable platform:
- **Django**: Web framework for building the backend logic and managing data.
- **Bootstrap**: For responsive UI design and layout.
- **PostgreSQL**: Database system used to store user profiles, pitch decks, and collaboration requests.
- **Cloudinary**: Used for managing and storing media files such as profile images and pitch deck visuals.
- **Heroku**: Platform used for deploying the live version of the application.
- **Code Validation**: Python code is validated using **flake8**, and HTML/CSS validation is done through **W3C Validator**.

### **Live Demo**
You can check out the live version of NetPitch at [NetPitch Live Demo](https://netpitch-4fea66f5e2b7.herokuapp.com/).

## **Features**

NetPitch offers a variety of features tailored to the needs of both writers and producers in the film and TV industry. Below is an overview of the key features:

### **1. User Authentication & Profile Management**
- **Signup/Login/Logout**: Users can create accounts, log in, and log out securely.
- **User Profiles**: Each user (whether a writer or producer) has a personalized profile page that includes their bio, profile picture, and user type (Writer or Producer). Profiles are customizable, allowing users to update their information at any time.

### **2. Pitch Deck Management**
- **Submit Pitch Decks**: Writers can submit pitch decks detailing their film or TV show ideas. Each pitch deck includes fields like title, synopsis, genre, and the type of project (Film or TV Show).
- **Edit/Delete Pitch Decks**: Writers can manage their submissions by editing or deleting pitch decks if needed.
- **Media Integration**: Each pitch deck submission supports images (such as cover art or concept visuals) via Cloudinary integration.

### **3. Collaboration Requests**
- **Request Collaboration**: Producers can view submitted pitch decks and request to collaboration with writers.
- **Manage Requests**: Writers can accept, decline, or clear collaboration requests. This ensures control over which projects they want to move forward with. Producers can clear collaboration requests as well.
- **Status Tracking**: Collaboration requests have a status indicator (Pending, Accepted, or Declined) to track the progress of each request.

### **4. Profile Image Management**
- **Cloudinary Integration**: Users can upload and manage their profile pictures using Cloudinary, ensuring efficient and scalable media storage.

### **5. Rich-Text Editor for Pitch Decks**
- **Django Summernote**: Writers can format their pitch deck details using a rich-text editor, allowing for visually appealing submissions with text formatting, bullet points, and more.

### **6. Admin Panel (Django Admin)**
- **User & Pitch Deck Management**: Admins can manage user accounts, pitch decks, and collaboration requests from the Django admin panel.
- **Search & Filters**: Admins can search and filter pitch decks, profiles, and collaboration requests for easier management.

### **7. Responsive Design**
- **Mobile-Friendly**: Built with Bootstrap, NetPitch provides a fully responsive experience, ensuring seamless usage across desktops, tablets, and mobile devices.

---

### **Future Features (Planned Updates)**

1. **Project Portfolio**: 
   - A dedicated section where users (writers and producers) can showcase their previously completed projects, giving collaborators insights into their past work.

2. **Dark Mode**: 
   - Implement a dark mode toggle for users who prefer a darker theme for browsing. This will enhance the user experience, especially for those who work in low-light environments.

3. **Communication Feature**: 
   - A secure communication feature that allows writers and producers to continue discussions beyond the initial collaboration request. This feature will include private messaging and notifications for ongoing project discussions.

4. **Fund Rounds Submission**: 
   - A feature that automates and guides users (specifically producers) through the process of submitting their media projects to various film funds globally. This will include a dynamic form that adapts based on the user’s location and project type.

5. **Co-Producers Search**: 
   - A dedicated search feature that allows production companies and producers to find secure co-producers in other countries, fostering international collaborations. The feature will offer filtering based on country, project type, and budget size.

6. **Monetization & Payment Structure**: 
   - Introduce a monetization structure for premium features, such as advanced collaboration tools or exposure to a broader network of producers and writers. This will also include a secure payment feature, allowing for subscription-based models or one-time payments.

 ### **Key Benefits of these Future Features**

- **Expanded Collaboration Opportunities**: Co-producer search and communication tools make it easier for users to connect and collaborate beyond initial requests.
- **Global Access to Funding**: By streamlining the submission process for film funds, you allow users to tap into a global network of financial support for their media projects.
- **Enhanced User Experience**: Dark mode and secure messaging will improve overall usability and satisfaction.
- **Monetization for Sustainability**: The monetization feature will ensure the platform’s financial viability and growth while providing premium tools for serious users.

---

With these additional features listed in the **Future Features** section, it gives users and contributors a forward-looking vision for how the platform will evolve and provides a clear path for growth.

## **Technologies Used**

NetPitch leverages several modern technologies and tools to ensure scalability, security, and a seamless user experience. Below is a breakdown of the key technologies used in the project:

### **Backend Technologies:**
- **Django**: Django is the primary web framework used for developing the backend of NetPitch. It handles data processing, authentication, and the management of models such as user profiles, pitch decks, and collaboration requests.
- **PostgreSQL**: PostgreSQL is the database management system that stores all of NetPitch’s data, including user information, pitch decks, and collaboration requests. It offers a scalable and secure database solution.
- **Gunicorn**: Gunicorn is a Python WSGI HTTP server used to serve the Django application on Heroku. It ensures efficient handling of HTTP requests in production environments.

### **Frontend Technologies:**
- **Bootstrap**: Bootstrap is used to ensure a fully responsive and mobile-friendly user interface. It allows the platform to be accessed seamlessly across various screen sizes and devices.
- **Django Templates**: Django’s template system is used to render dynamic content on the frontend, making sure data from the backend is presented in a clean, user-friendly manner.

### **Media & File Storage:**
- **Cloudinary**: Cloudinary is used for the storage and management of media files such as profile images and pitch deck visuals. Its integration with Django ensures that media is handled efficiently and delivered quickly across the globe.
- **dj3-cloudinary-storage**: This package integrates Cloudinary storage with Django, allowing for easy upload and retrieval of media files such as images and documents.

### **Deployment & Hosting:**
- **Heroku**: Heroku is the platform used to deploy the live version of NetPitch. It supports scalable web applications and ensures that NetPitch remains accessible to users around the world.
- **Whitenoise**: Whitenoise is used to manage and serve static files directly from the web server. It is particularly useful in production to ensure that CSS, JavaScript, and image files are efficiently served.

### **Database Configuration:**
- **dj-database-url**: This package is used to easily configure the PostgreSQL database for production environments by parsing the `DATABASE_URL` from the environment variables.

### **Code Validation:**
- **flake8**: This Python linter is used for code quality checks. It helps enforce PEP 8 compliance and identifies potential issues in the codebase.
- **W3C Validator**: Used to validate the HTML and CSS of the project, ensuring that the frontend is clean and standards-compliant.

### **Image & File Processing:**
- **Pillow**: Pillow is a Python Imaging Library (PIL) fork that adds image processing capabilities to the platform. It allows the application to handle image uploads and manipulation efficiently.

### **Rich Text Editing:**
- **Django Summernote**: Provides a rich-text editing interface, allowing writers to format their pitch deck submissions with ease. It ensures that users can include various formatting options like bullet points and text styles in their submissions.

---

These technologies come together to create a robust, responsive, and scalable platform that caters to both writers and producers in the media industry.

## **Installation & Setup**

To run the NetPitch project locally, follow these steps to get the application up and running on your machine.

### **Prerequisites:**
Before starting, ensure you have the following installed on your machine:
- **Python 3.x**: Required to run the Django application.
- **PostgreSQL**: The database system used by the project.
- **Cloudinary Account**: If you want to handle media files as in the production version.

### **1. Clone the Repository**
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/your-username/netpitch.git
cd netpitch

# On macOS/Linux
python3 -m venv env
source env/bin/activate

# On Windows
python -m venv env
env\Scripts\activate

pip install -r requirements.txt

SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
CLOUDINARY_URL=cloudinary-url
DEBUG=True  # Set this to False in production

# Access PostgreSQL
psql

# In the PostgreSQL shell, create a new database
CREATE DATABASE netpitch_db;

DATABASE_URL=postgres://username:password@localhost:5432/netpitch_db

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

#You can also deploy the project to Heroku for a live production environment.

	1.	Create a Heroku account at Heroku.
	2.	Install the Heroku CLI:

#bash
curl https://cli-assets.heroku.com/install.sh | sh

heroku login

heroku create your-app-name

git push heroku main

#Set the environment variables on Heroku (replace values with your own):

heroku config:set SECRET_KEY=your-secret-key
heroku config:set DATABASE_URL=your-database-url
heroku config:set CLOUDINARY_URL=your-cloudinary-url

#Migrate the database on Heroku:

heroku run python manage.py migrate

#Collect static files:
heroku run python manage.py collectstatic --noinput
```

---



## **Usage**

Once NetPitch is set up and running, both writers and producers can interact with the platform's key features. Below is an overview of how to use the main functionalities of the application.

### **1. User Registration and Login**
- **Signup**: Navigate to the signup page from the homepage or the user dropdown menu. Fill in the necessary details, including your user type (Writer or Producer), email, username, and password.
- **Login**: If you already have an account, log in by entering your username and password on the login page.
- **Profile Management**: Once logged in, users can access their profile page from the menu. Here, they can update their bio, profile image, and view any pitch decks they have submitted, as well as their sent or recieved collaboration requests. 

### **2. Creating a Pitch Deck (For Writers)**
- Writers can submit new pitch decks by navigating to the "Submit Pitch Deck" section on their profile menu, by clicking the "Submit New Pitch Deck" button.
- **Form Fields**: Provide the required details, including the project title, synopsis, genre, and pitch type (Film or TV Show).
- **Uploading Images**: Writers can upload cover art or visual aids for their pitch deck, which will be stored via Cloudinary.
- **Text Formatting**: The platform uses a rich text editor (Django Summernote), allowing writers to format their synopsis and add emphasis using bullet points, bold text, etc.
- **Submission**: Once submitted, the pitch deck will be available for producers & other writers to view.

### **3. Viewing and Requesting Collaboration (For Producers)**
- Producers can browse all submitted pitch decks by navigating to the **Pitch Deck Gallery** either from their Profile page or through the home page links. 
- **Viewing a Pitch Deck**: Producers can click on a specific pitch deck to view the full synopsis, title, genre, and images associated with it.
- **Request Collaboration**: If a producer is interested in a project, they can submit a collaboration request directly from the pitch deck’s page. The writer will then be notified of the request.

### **4. Managing Collaboration Requests (For Writers)**
- **Accept/Decline Requests**: Writers can view all collaboration requests from producers on their profile dashboard. Each request has an option to accept, decline, or clear the request.
- **Collaboration Status**: Once a request is accepted, the status changes to **Accepted**, and communication between the writer and producer can continue via external channels. (Something I'd like to change to internal channels in the future.)

### **5. Updating Profiles**
- **Edit Profile**: Both writers and producers can update their profile information by visiting their profile page. This includes updating their bio, profile picture, and any other details about themselves.
- **Profile Image Management**: Profile images are uploaded and stored via Cloudinary, and users can change or remove their profile pictures at any time.

### **6. Admin Features**
- **Admin Panel**: Admins have access to the Django admin panel, where they can manage users, pitch decks, and collaboration requests.
- **Search and Filtering**: Admins can search for specific users or projects and filter by status, pitch type, or user role (Writer/Producer).
- **Moderation**: Admins have the ability to edit or delete pitch decks, collaboration requests, and user profiles to maintain the integrity of the platform.

---

### **Live Demo**
To see the platform in action, visit the live demo of NetPitch [here](https://netpitch-4fea66f5e2b7.herokuapp.com/). 
- **Sign up** as a writer or producer to explore the full functionality of the platform.
- **Test Features**: Submit a pitch deck, request collaborations, and manage your profile just as you would in a real-world setting.

## **Database Schema**

The database schema for NetPitch consists of several key models that represent the core functionality of the platform, including users, profiles, pitch decks, and collaboration requests. Below is an overview of the most important models and their relationships:

### **1. User**
- **Description**: This model is inherited from Django’s built-in `User` model. It handles user authentication and stores basic user information like username, password, and email.
  
  **Fields**:
  - `username`: The unique identifier for a user.
  - `email`: The user's email address.
  - `password`: A hashed version of the user's password.

### **2. Profile**
- **Description**: The `Profile` model extends the user model with additional fields for writers and producers. It stores information specific to the type of user.
  
  **Fields**:
  - `user`: One-to-one relationship with Django’s built-in `User` model.
  - `bio`: A short biography written by the user.
  - `profile_image`: Stores the user's profile image, uploaded via Cloudinary.
  - `user_type`: A choice field that defines whether the user is a writer or a producer.

  **Relationships**:
  - One-to-one relationship with the `User` model.

### **3. PitchDeck**
- **Description**: This model represents a pitch deck submitted by a writer. Each pitch deck contains detailed information about a media project, such as a film or TV show idea.
  
  **Fields**:
  - `title`: The title of the pitch deck.
  - `synopsis`: A brief description or overview of the project.
  - `genre`: A foreign key linking to the `Genre` model.
  - `theme`: An optional field where writers can add the project’s theme.
  - `pitch_type`: A choice field to specify whether the project is a film or TV show.
  - `writer`: A foreign key linking to the `User` model (specifically writers).
  - `image`: An optional field for uploading a pitch deck image via Cloudinary.

  **Relationships**:
  - Foreign key relationship with the `User` model (one writer can have multiple pitch decks).
  - Foreign key relationship with the `Genre` model (each pitch deck belongs to one genre).

### **4. Genre**
- **Description**: This model represents the genre of a media project (e.g., Drama, Comedy, Thriller). It helps categorize pitch decks.
  
  **Fields**:
  - `name`: The name of the genre (e.g., "Drama", "Comedy").
  
  **Relationships**:
  - One-to-many relationship with the `PitchDeck` model (one genre can apply to many pitch decks).

### **5. CollaborationRequest**
- **Description**: This model tracks collaboration requests sent by producers to writers. Producers can submit requests to work on specific pitch decks.
  
  **Fields**:
  - `pitch`: Foreign key linking to the `PitchDeck` model.
  - `producer`: Foreign key linking to the `Profile` model (specifically producers).
  - `message`: A text field where producers can write a personalized message.
  - `status`: A choice field that tracks the request status (Pending, Accepted, Declined).
  
  **Relationships**:
  - Foreign key relationship with the `PitchDeck` model (each request belongs to a specific pitch).
  - Foreign key relationship with the `Profile` model (each request is sent by a producer).

---

### **Relationships Summary**

1. **User and Profile**: One-to-one relationship. Each user has one associated profile (either as a writer or a producer).
2. **Profile and PitchDeck**: One-to-many relationship. A writer (via their profile) can submit multiple pitch decks.
3. **Genre and PitchDeck**: One-to-many relationship. One genre can apply to multiple pitch decks.
4. **PitchDeck and CollaborationRequest**: One-to-many relationship. A pitch deck can have multiple collaboration requests.
5. **Profile (Producer) and CollaborationRequest**: One-to-many relationship. A producer can submit multiple collaboration requests to different writers.

---

### **Diagram Representation**

Here’s a simplified diagram of the relationships:

User ––> Profile
|          |
|          V
|       PitchDeck ––> Genre
|
V
CollaborationRequest

In this diagram:
- Each `User` has one `Profile`, which can either be a writer or producer.
- A `Profile` (as a writer) can submit multiple `PitchDecks`.
- Each `PitchDeck` can belong to one `Genre`.
- A `Profile` (as a producer) can submit multiple `CollaborationRequests` to different pitch decks.

---

This schema showcases how the data is structured within NetPitch, allowing for scalable management of users, pitch decks, and collaborations.