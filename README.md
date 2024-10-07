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
9. [Agile](#Agile)
10. [Wireframe](#Wireframe)
11. [Credits](#credits)

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

![NetPitch Homepage](./assets/readme.media/features/homescreen.png)

## **Features**

NetPitch offers a variety of features tailored to the needs of both writers and producers in the film and TV industry. Below is an overview of the key features:

### **1. User Authentication & Profile Management**
- **Signup/Login/Logout**: Users can create accounts, log in, and log out securely.
- **User Profiles**: Each user (whether a writer or producer) has a personalized profile page that includes their bio, profile picture, and user type (Writer or Producer). Profiles are customizable, allowing users to update their information at any time.

**Home Page**
![NetPitch Homepage](./assets/readme.media/features/homescreen.png)

**Log in &  Sign Up**

![NetPitch Homepage](./assets/readme.media/features/login-signup.png)

**Home Page Logged In**
![NetPitch Homepage](./assets/readme.media/features/homepage-log-in.png)

**Login Form**
![NetPitch Homepage](./assets/readme.media/features/log-in-form.png)

**Sign-up Form**
![NetPitch Homepage](./assets/readme.media/features/signup-form.png)

**Producer Page**
![NetPitch Homepage](./assets/readme.media/features/producer-profile.png)

**Writer Page**
![NetPitch Homepage](./assets/readme.media/features/writers-profile.png)


### **2. Pitch Deck Management**
- **Submit Pitch Decks**: Writers can submit pitch decks detailing their film or TV show ideas. Each pitch deck includes fields like title, synopsis, genre, and the type of project (Film or TV Show).
- **Edit/Delete Pitch Decks**: Writers can manage their submissions by editing or deleting pitch decks if needed.
- **Media Integration**: Each pitch deck submission supports images (such as cover art or concept visuals) via Cloudinary integration.

**Submit Pitch Deck**
![NetPitch Homepage](./assets/readme.media/features/submit-deck-button.png)

![NetPitch Homepage](./assets/readme.media/features/submit-deck-form.png)

**Edit Pitch Deck**
![NetPitch Homepage](./assets/readme.media/features/edit-delete-deck.png)

![NetPitch Homepage](./assets/readme.media/features/edit-form.png)

### **3. Collaboration Requests**
- **Request Collaboration**: Producers can view submitted pitch decks and request to collaboration with writers.
- **Manage Requests**: Writers can accept, decline, or clear collaboration requests. This ensures control over which projects they want to move forward with. Producers can clear collaboration requests as well.
- **Status Tracking**: Collaboration requests have a status indicator (Pending, Accepted, or Declined) to track the progress of each request.

**Collaborate** 
![NetPitch Homepage](./assets/readme.media/features/collaborate.png)

![NetPitch Homepage](./assets/readme.media/features/collaboration-form.png)

**Manage Requests**
![NetPitch Homepage](./assets/readme.media/features/writer-collaboration.png)

![NetPitch Homepage](./assets/readme.media/features/producer-collaboration.png)

### **4. Profile Image Management**
- **Cloudinary Integration**: Users can upload and manage their profile pictures using Cloudinary, ensuring efficient and scalable media storage.

### **5. Rich-Text Editor for Pitch Decks**
- **Django Summernote**: Writers can format their pitch deck details using a rich-text editor, allowing for visually appealing submissions with text formatting, bullet points, and more.

### **6. Admin Panel (Django Admin)**
- **User & Pitch Deck Management**: Admins can manage user accounts, pitch decks, and collaboration requests from the Django admin panel.
- **Search & Filters**: Admins can search and filter pitch decks, profiles, and collaboration requests for easier management.

**Admin**
![NetPitch Homepage](./assets/readme.media/features/admin.png)

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

**Update Profile Form**
![NetPitch Homepage](./assets/readme.media/features/update-profile-form.png)

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

## **Testing**


### **1. Automated Testing**

I have not performed any automated tesing throughout this project other then testing the code with w3c and/or flake8, which was done at the end of the project and will be previewed later down the testing section.

---

### **2. Manual Testing**

Below is a detailed list of manual tests that were conducted during development, documenting the input, expected output, and actual results.

#### **User Registration and Login**
- **Signup**:
    - **Tested**: Registering as a new user (Writer/Producer).
    - **Expected Outcome**: User should be able to register successfully and be redirected to the profile page.
    - **Actual Outcome**: Initially, the sign-up functionality only created a basic user profile without distinguishing between a Writer or Producer profile. This resulted in the creation of generic user profiles without any association to the selected profile type.
    - **Issue**: The issue arose when extending Django’s User model to include distinct profile types (Writer and Producer). While the initial extension worked, after introducing additional models and views, the system encountered a problem where it only referenced the base user profile during sign-up. It failed to associate users with the correct profile type, causing errors in the profile creation process. Additionally, with DEBUG=False enabled, the system produced errors that made the page inaccessible, further complicating the troubleshooting process.
    - **Solution**: To resolve the issue, I modified the sign-up process to ensure that the correct profile type (Writer or Producer) was created immediately upon user registration. I adjusted the sign-up form to explicitly capture and store the user’s selected profile type, and updated the logic in the views to ensure the extended profile data was retrieved and correctly linked to the user. Additionally, I temporarily switched DEBUG=True during testing to better track the errors and identify the root cause. Once the solution was in place and thoroughly tested, I reverted to DEBUG=False for production, ensuring the system was now correctly handling the user profiles without any further issues.
    - **Status**: Fixed and functioning as expected. Users can now register successfully, and their selected profile type (Writer or Producer) is correctly associated with their account upon sign-up.

- **Login**:
    - **Tested**: Logging in with correct and incorrect credentials.
    - **Expected Outcome**: Users should log in with valid credentials and receive error messages for invalid credentials.
    - **Actual Outcome**: The default Django authentication system worked seamlessly for both valid and invalid login attempts. Users were able to log in successfully with the correct credentials, and the system correctly displayed error messages for invalid logins.
    - **Status**: No significant issues encountered during testing. The default Django model handled the login functionality as expected, and no additional debugging or troubleshooting was required.

- **Profile Management**:
    - **Tested**: Updating profile information and uploading a profile image.
    - **Expected Outcome**: Users should be able to update their bio and successfully upload a profile image.
    - **Actual Outcome**:  Initially, profile updates worked well in the production environment. However, after integrating Cloudinary for media management, the profile image uploads stopped working, and the page became inaccessible.
    - **Issue**: The issue arose because the Cloudinary storage backend was not fully configured in the environment variables. Specifically, the CLOUDINARY_URL was missing or incorrectly set, which caused the system to fail when trying to upload and retrieve images.
    - **Solution**: To resolve this, I ensured that the CLOUDINARY_URL was correctly added to the environment variables in both local and production environments. Additionally, I verified that the cloudinary and dj3-cloudinary-storage packages were installed and correctly integrated into the INSTALLED_APPS section of the settings.py file. After these changes, the profile image uploads functioned as expected, and users were able to manage their profiles without any issues.
    - **Status**: Fixed and working as expected.

#### **Pitch Deck Management (For Writers)**
- **Submit Pitch Deck**:
    - **Tested**: Submitting a pitch deck with all required fields.
    - **Expected Outcome**: Writers should be able to submit a new pitch deck and view it in their profile.
    - **Actual Outcome**: Initially, the submission process allowed for pitch decks to be created, but there were two issues: the default image was not being utilized when no image was uploaded, and the genre selection field appeared blank, with no options to choose from.
    - **Issue**: Default Image Issue: The issue with the default image stemmed from an incorrect file path configuration in the settings, which caused the system to fail to locate the default image when one wasn’t provided. The genre selection field was empty because I had not populated the Genre model with any genre entries. As a result, writers were unable to select a genre for their pitch decks.
    - **Solution**: Solution:
	•	For the default image issue, I corrected the pathing in the settings.py file to point to the correct default image location. This ensured that when a writer did not upload an image, the system would automatically display the default image.
	•	To resolve the genre options issue, I populated the Genre model with a set of predefined genres (e.g., Drama, Comedy, Thriller), allowing writers to select from a range of options when submitting their pitch decks.
    - **Status**: Both issues were resolved. Writers can now submit pitch decks with or without an image, and the genre options are available for selection during submission. The system correctly associates the pitch decks with the writer’s profile and displays them as expected.

- **Edit/Delete Pitch Deck**:
    - **Tested**: Editing and deleting an existing pitch deck.
    - **Expected Outcome**: Writers should be able to update details and remove their pitch decks.
    - **Actual Outcome**: Initially, the pitch deck editing feature worked for text fields (title, synopsis, etc.), but I encountered an issue when attempting to update the image associated with the pitch deck. Additionally, the delete function was not fully removing the pitch deck and its associated media files from the system.
    - **Issue**: Image Update Issue: The system allowed text updates (title, synopsis, genre), but when trying to update the image, it failed to replace the existing image file with the new one. This was due to a missing check for file replacement in the view handling the pitch deck updates. Deletion Issue: While the pitch deck was being removed from the database, the associated media (e.g., images stored in Cloudinary) were not being deleted, leaving orphaned files in storage.
    - **Status**: For the image update issue, I modified the view handling the pitch deck updates to properly check for and replace the old image with the new one. This ensured that the image associated with a pitch deck was correctly updated during the edit process. To resolve the deletion issue, I updated the deletion logic to not only remove the pitch deck from the database but also delete the associated image from Cloudinary when the pitch deck was deleted. This ensured that no unnecessary media files were left behind in storage.
    - **Status**: Both the edit and delete functionalities are now working as expected. Writers can update any field in their pitch deck, including the image, and delete pitch decks along with their associated media without leaving orphaned files in storage.

#### **Collaboration Requests (For Producers)**
- **Request Collaboration**:
    - **Tested**: Producers requesting collaboration on a pitch deck.
    - **Expected Outcome**: Producers should be able to submit requests to collaborate with writers.
    - **Actual Outcome**: Initially, producers were able to submit collaboration requests, but writers encountered problems when managing these requests. The form lacked the necessary buttons to accept or decline collaboration requests, and even after a request was accepted or declined, there was no option to delete or clear the request from the interface.
    - **Issue**: Missing Accept/Delete Buttons: The collaboration request form did not include buttons for writers to accept or decline the requests. This made it impossible for writers to manage the incoming requests properly. Post-Decision Management: After writers accepted or declined a request, they were unable to clear or delete the request, leaving the request in an unresolved state.
    - **Solution**: I updated the collaboration request management interface by adding Accept and Decline buttons to allow writers to properly handle incoming requests. Additionally, I implemented a Clear/Delete option, enabling writers to remove requests from their dashboard once they had accepted or declined them. This ensured that completed requests could be fully managed and removed from the system.
    - **Status**: The collaboration request functionality is now working as expected. Writers can accept, decline, or clear collaboration requests, and the process is fully manageable from the writer’s interface. But there is a missing feature of how to connect with each other, I'd like to add a direct request through e-mail or other communcation signal. One issue I haven't had time to troubleshoot is to only place one request per/producer per/pitchdeck. 

- **Manage Requests (For Writers)**:
    - **Tested**: Writers accepting or declining collaboration requests.
    - **Expected Outcome**: Writers should be able to view incoming requests and update their status.
    - **Actual Outcome**: Initially, writers were able to view incoming collaboration requests, but they couldn’t effectively manage them. The interface lacked buttons to accept or decline the requests, and even after accepting or declining, the requests couldn’t be deleted or cleared from the system, causing clutter and confusion on the dashboard.
    - **Issue**: Missing Accept/Decline Buttons: Writers could see the collaboration requests but had no way to accept or decline them due to the absence of appropriate buttons in the interface. Post-Decision Management: After accepting or declining a request, writers could not clear or delete the request, leaving it stuck on the dashboard in an unresolved state.
    - **Solution**: I updated the request management interface to include Accept and Decline buttons, allowing writers to handle incoming collaboration requests properly. I also added functionality for clearing or deleting requests after a decision had been made, ensuring that writers could manage their requests efficiently and remove completed or declined requests from the dashboard.
    - **Status**: Fully resolved. Writers can now accept, decline, and clear collaboration requests. The interface is fully functional, allowing for smooth request management. But there is a missing feature of how to connect with each other, I'd like to add a direct request through e-mail or other communcation signal. 

#### **Admin Features**
- **Manage Users**:
    - **Tested**: Admins editing, deleting, and viewing users via the Django admin panel.
    - **Expected Outcome**: Admins should be able to perform all CRUD operations on user profiles.
    - **Actual Outcome**: Initially, only basic user accounts were created through the admin panel, but the associated extended profiles (Writer or Producer) were not generated automatically. As a result, while the user accounts appeared in the system, their extended profile data (such as bio, user type, and profile images) were missing, making the profiles incomplete.
    - **Issue**: Missing Profile Creation: The admin panel successfully created users, but the extended profile types (Writer/Producer) were not being created alongside the user accounts. This led to incomplete user profiles that lacked the necessary information and association with the Writer/Producer roles.
    - **Solution**: I updated the user creation logic in the admin panel to automatically generate the associated Profile for each user upon creation. This ensured that whenever a new user is created, an extended profile (either Writer or Producer) is also created and linked to the user. Additionally, I ensured that admins could edit and delete both the user and their extended profile, keeping the system consistent and avoiding incomplete data.
    - **Status**: Resolved. Admins can now fully create, edit, and delete users, including their associated Writer/Producer profiles. The system correctly handles the creation of extended profiles upon user creation in the admin panel.

- **Manage Pitch Decks**:
    - **Tested**: Admins editing and deleting pitch decks from the admin panel.
    - **Expected Outcome**: Admins should be able to manage all pitch decks in the system.
    - **Actual Outcome**: 
    - **Status**: 


---

### **3. Code Validation**

The code for NetPitch was validated using various tools to ensure that it met coding standards and was free of syntax errors.

#### **Python Code Validation**
- **flake8** was used to ensure compliance with PEP 8 standards.
- **Command Used**:
    ```bash
    flake8
    ```
- **Validation Result**: (Document whether any issues were found, or if the code passed validation.)

**Flake8**

![NetPitch Homepage](./assets/readme.media/testing/flake8.png)

**Python Test**

![NetPitch Homepage](./assets/readme.media/testing/python-test.png)

**Python Test Errors**

![NetPitch Homepage](./assets/readme.media/testing/python-test-error.png)

#### **HTML/CSS Validation**
- The HTML and CSS files were validated using the **W3C Validator**.
- **URL Tested**: (You can list the URLs or specific HTML files tested here.)
- **Validation Result**: At first I tested all the coded through URL, and not no issues or errors which I felt good about but new couldn't be true. So I copied all teh code for each page instead and got the following errors. (Document any errors or warnings and how they were resolved.)

**HTML Test**

![NetPitch Homepage](./assets/readme.media/testing/html-checker.png)

**HTML Test Error**

![NetPitch Homepage](./assets/readme.media/testing/html-checker-error.png)

**CSS Test**

![NetPitch Homepage](./assets/readme.media/testing/css-checker.png)

**CSS Test Error**

![NetPitch Homepage](./assets/readme.media/testing/css-checker-error.png)
---

### **4. Browser and Device Testing**

Manual testing was done to ensure the application works across different browsers and screen sizes.

#### **Browsers Tested**:
- Google Chrome
- Safari

#### **Devices Tested**:
- Mobile (iOS)
- Desktop and google inspect dimension responsiveness. 

**Results**:
- **Browser Compatibility**: Worked well.
- **Responsive Design**: Worked well.

---

### **5. Lighthouse Performance Testing**

Google Lighthouse was used to assess the performance and accessibility of the application.

- **Platform**: Google Chrome (Lighthouse)


- **Result**: 

![NetPitch Homepage](./assets/readme.media/testing/lighthouse-test.png)


### **7. Static Files Issue (DEBUG=False)**

During the deployment process, an issue arose when setting `DEBUG=False`. The static files, including CSS, JavaScript, and images, were not being properly served, which caused changes in the layout and styling of the website (such as color changes and missing assets).

#### **Issue**:
- When `DEBUG=False`, Django does not automatically serve static files in production. This led to missing CSS and other static files when the site was accessed, resulting in broken styles and incomplete functionality.

#### **Solution**:
- The issue was resolved by running the `collectstatic` command to gather all the static files into the `STATIC_ROOT` directory for production use:
    ```bash
    python manage.py collectstatic
    ```
- After running this command, the static files were correctly served, and the layout and design of the site were restored. 
- Additionally, Whitenoise was used to ensure static files were properly served in production.

With this fix, the site works as expected when `DEBUG=False`, and all static assets are correctly loaded.
---

## **Deployment**

NetPitch is deployed on Heroku, and this section provides instructions for both local development deployment and deploying the project to a live environment like Heroku.

### **1. Local Deployment**

To deploy NetPitch locally on your own machine:

#### **Prerequisites**:
- Ensure you have Python and PostgreSQL installed.
- Install necessary libraries (as specified in the `requirements.txt` file).
- Set up a Cloudinary account for media storage if needed.

#### **Steps**:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/netpitch.git
    cd netpitch
    ```

2. **Set Up Virtual Environment**:
    It is recommended to use a virtual environment to manage dependencies.
    ```bash
    # Create a virtual environment
    python3 -m venv env

    # Activate the virtual environment
    source env/bin/activate  # On macOS/Linux
    env\Scripts\activate  # On Windows
    ```

3. **Install Dependencies**:
    Install the required packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create an `.env` file in the root of your project and add the following:
    ```plaintext
    SECRET_KEY=your-secret-key
    DATABASE_URL=your-database-url
    CLOUDINARY_URL=your-cloudinary-url
    ```

5. **Set Up PostgreSQL**:
    Create a PostgreSQL database and configure it in the `.env` file under `DATABASE_URL`.

6. **Apply Migrations**:
    Run the following command to apply the necessary database migrations:
    ```bash
    python manage.py migrate
    ```

7. **Create Superuser** (Optional):
    Create a superuser to access the admin panel.
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the Development Server**:
    Start the local server using:
    ```bash
    python manage.py runserver
    ```

    You should now be able to access the application at the local develoepr enivronent host, for me it was 'https://8000-fantomen31-netpitch-y8c92sz8q4w.ws-eu116.gitpod.io'.

---

### **2. Deployment to Heroku**

To deploy NetPitch to Heroku, follow these steps:

#### **Prerequisites**:
- Create an account at [Heroku](https://heroku.com).
- Install the Heroku CLI on your machine.
- Ensure that PostgreSQL and Cloudinary are set up for production.

#### **Steps**:

1. **Log into Heroku**:
    Log into your Heroku account using the CLI:
    ```bash
    heroku login
    ```

2. **Create a New Heroku App**:
    Create a new Heroku app for the project:
    ```bash
    heroku create your-app-name
    ```

3. **Set Up Environment Variables**:
    Configure the necessary environment variables in Heroku:
    ```bash
    heroku config:set SECRET_KEY=your-secret-key
    heroku config:set DATABASE_URL=your-database-url
    heroku config:set CLOUDINARY_URL=your-cloudinary-url
    ```

4. **Add Heroku Postgres**:
    Add the Heroku Postgres add-on for database management:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

5. **Prepare Static Files for Deployment**:
    Collect static files to serve them via Whitenoise:
    ```bash
    python manage.py collectstatic --noinput
    ```

6. **Push Code to Heroku**:
    Deploy the application by pushing your code to Heroku:
    ```bash
    git push heroku main
    ```

7. **Apply Migrations on Heroku**:
    Run the following command to apply database migrations on Heroku:
    ```bash
    heroku run python manage.py migrate
    ```

8. **Create Superuser on Heroku** (Optional):
    If you need admin access on your live site, create a superuser:
    ```bash
    heroku run python manage.py createsuperuser
    ```

9. **Launch the App**:
    Once deployed, your app will be live on Heroku at the URL provided by the platform. You can access it using:
    ```bash
    heroku open
    ```

---

### **3. Additional Deployment Notes**

- **Debug Mode**: 
  Ensure that `DEBUG=False` is set in your production environment for security purposes.
  
- **Static and Media Files**: 
  - Heroku uses **Whitenoise** to serve static files.
  - Cloudinary is used for managing and serving media files (e.g., profile images, pitch deck images).
  
- **Database Configuration**: 
  Heroku uses its own Postgres add-on for production databases. Make sure your `DATABASE_URL` is correctly configured both locally and on Heroku.

- **Gunicorn**: 
  Ensure you are using **Gunicorn** as the WSGI server for production. It's already included in the `requirements.txt` file.

---

### **4. Live Demo**

The live version of NetPitch can be accessed at:  
[NetPitch Live on Heroku](https://netpitch-4fea66f5e2b7.herokuapp.com/)

## **AGILE Methodology**

The development of NetPitch followed an Agile methodology, ensuring flexibility and continuous feedback throughout the project. This approach helped in managing the complexity of the platform by breaking the work into smaller, manageable iterations (sprints). Below is an overview of the Agile processes used during development.

### **1. Sprint Planning**
- Each sprint was planned with clear objectives, focusing on delivering specific features or functionality in short time frames.
- Key tasks were identified and added to the project management board, ensuring "all" contributors had a clear understanding of the goals for each sprint.

![NetPitch Homepage](./assets/readme.media/project-board/project-board-1.png)

### **2. Project Management Tools**
- **GitHubs Project Board** was used to manage tasks and track progress. The board was organized with columns for "To Do", "In Progress", and "Done".
- The board was updated regularly to reflect the progress of each sprint.

![NetPitch Homepage](./assets/readme.media/project-board/project-board-2.png)

### **3. Sprint Cycles**
- Each sprint lasted approximately one day. At the beginning of each sprint, the MVP tasks were prioritized based on feedback from the previous sprint and ongoing project needs.
- Daily stand-ups were used to track progress and adjust the sprint scope if necessary.

![NetPitch Homepage](./assets/readme.media/project-board/project-board-4.png)

### **4. Continuous Feedback and Iteration**
- Throughout development, feedback was gathered after each sprint to improve functionality and fix bugs. User stories were updated regularly based on testing and feature development.
- Iteration was key to the Agile process. Features such as user profile management, pitch deck submissions, and collaboration requests were refined over multiple sprints, ensuring they met user needs and felt beter.

### **5. Retrospectives and Improvements**
- After each sprint, retrospectives were conducted to review what went well, what could be improved, and the lessons learned for the next sprint. 
- Challenges like initial issues with profile creation and static files were identified and addressed through this process.

### **6. Final Sprint and Release**
- The final sprint focused on polishing the user interface, optimizing performance, and ensuring all core features worked as expected in production.
- Testing was carried out to ensure the platform was stable and ready for deployment.


---

## **Credits**

NetPitch was made possible through the use of various technologies, tools, and resources. Special thanks to the following:

### **1. Technologies**
- **[Django](https://www.djangoproject.com/)**: Django is the main framework used to build the backend of this application, providing a robust and scalable structure.
- **[Bootstrap](https://getbootstrap.com/)**: Bootstrap was used for the frontend to ensure responsive design and a smooth user experience across all devices.
- **[PostgreSQL](https://www.postgresql.org/)**: PostgreSQL was the database system used to store and manage all project data, offering a reliable and secure backend.
- **[Cloudinary](https://cloudinary.com/)**: Cloudinary was used for media management, including storing and serving images such as profile pictures and pitch deck visuals.
- **[Heroku](https://www.heroku.com/)**: Heroku was the platform used for hosting and deploying the live version of NetPitch, ensuring a seamless deployment process.
- **[Django Summernote](https://summernote.org/)**: Django Summernote was used to provide a rich-text editing interface, making it easier for users to format their pitch deck submissions.
- **[Whitenoise](http://whitenoise.evans.io/)**: Whitenoise was used to serve static files efficiently in production, ensuring proper management of CSS and JS assets.
  
### **2. Code Validation**
- **[flake8](https://flake8.pycqa.org/)**: This tool was used to check for PEP 8 compliance and maintain code quality throughout the project.
- **[W3C Validator](https://validator.w3.org/)**: The W3C HTML/CSS Validator was used to ensure that the frontend code adhered to web standards.

### **3. Tutorials and Documentation**
- **[Django Documentation](https://docs.djangoproject.com/)**: The official Django documentation was an essential resource throughout the development process, providing guidance on best practices.
- **[Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)**: The official Bootstrap documentation helped with implementing responsive design and UI components.

### **4. Special Thanks**
- **Contributors**: A big thank you to my friends and my mentor who provided help with readibility for colorschems and alert warnings for NetPitch.
- **Community Support**: Special thanks to the Django and Stack Overflow communities for their insights and solutions to technical challenges encountered during development.

---

NetPitch is built on the shoulders of these incredible technologies and resources. Thank you to everyone who contributed directly or indirectly to coding before me!
