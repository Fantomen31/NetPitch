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
10. [License](#license)
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