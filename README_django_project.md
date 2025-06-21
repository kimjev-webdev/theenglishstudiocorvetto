# 🏫 The English Studio – Django School Website

A full-stack Django web application for an independent language school in Milan. The site provides a bilingual (English/Italian) interface with a responsive design, public blog, contact form, event calendar, and a secure staff portal. This README reflects both frontend and backend development with a strong emphasis on database design, CRUD operations, and security — all in line with the assessment rubric for distinction.

---

## 📚 Table of Contents

- [About the Project](#about-the-project)
- [User Stories](#user-stories)
- [Features](#features)
- [Wireframes and Design Rationale](#wireframes-and-design-rationale)
- [Database Design](#database-design)
- [Models Overview](#models-overview)
- [Portal & CRUD](#portal--crud)
- [Authentication & Permissions](#authentication--permissions)
- [Manual Testing](#manual-testing)
- [Bug Log](#bug-log)
- [Security & Deployment](#security--deployment)
- [Technologies Used](#technologies-used)
- [Version Control](#version-control)
- [Credits & Attribution](#credits--attribution)

---

## 📖 About the Project

This Django site was created to meet the real-world needs of a local language school. It provides a modern online presence with enhanced admin capabilities and a user-friendly interface for parents, students, and staff. 

The application combines frontend polish with backend power, leveraging Django's ORM for scalable content management and secure form handling.

---

## 👤 User Stories

### Visitors
- As an Italian parent, I want my child to learn English, but I need to browse the site in Italian.
- As a prospective student, I want to easily view class options, and then look at upcoming events on my mobile.
- As a new visitor, I want to find contact details for the school easily.

### Staff
- As a teacher, I want to post blog entries without needing full admin access.
- As a manager, I want to create and cancel recurring events.

---

## ✨ Features

### Frontend
- Hero image carousel
- Bilingual interface
- Visual calendar with emojis
- Responsive layout (Bootstrap)
- Contact form with email routing and Mailchimp opt-in

### Backend / Django
- BlogPost model with multilingual fields and media
- Event model with recurrence and exception support
- ContactSubmission model with category and email handling
- Secure staff-only portal for managing content
- Cloudinary integration for media hosting

---

## 🖍️ Wireframes and Design Rationale

Design emphasizes accessibility and mobile-friendliness. Features are grouped into clear sections for ease of navigation.

*Include screenshots or wireframe sketches here.*

---

## 🧱 Database Design

This site uses Django's ORM with a PostgreSQL backend. Models include:

- `BlogPost`: multilingual content, media fields, publication status
- `Event`: supports recurrence rules and visual calendar icons
- `ContactSubmission`: tracks user messages and newsletter preferences
- `HeroImage`: manages carousel content

All models were built using migrations and validated via Django Admin and the portal interface.

---

## 🧩 Models Overview

```python
class BlogPost(models.Model):
    title_en, title_it = ...
    body_en, body_it = ...
    featured_image = CloudinaryField(...)
    slug = SlugField(...)
    author = ForeignKey(User)
```

*Models support full CRUD operations and are localized using `gettext_lazy`.*

---

## 🖥️ Portal & CRUD

The `/portal/` route provides staff with a login-protected dashboard.

### Blog Management
- CreateView, UpdateView, DeleteView
- Custom `BlogPostForm` using CKEditor and media fields
- Staff-only access with Django mixins

### Event Management (in progress)
- Recurrence logic with exceptions
- Admin toggle for cancellation and rescheduling

---

## 🔐 Authentication & Permissions

- Superusers and staff use the Django backend
- Staff use the `/portal/` dashboard
- Custom mixins and `user_passes_test()` to protect all views
- CSRF tokens and login protection enabled on all forms

---

## 🧪 Manual Testing

- ✅ Blog CRUD via portal
- ✅ Contact form submission + email confirmation
- ✅ Calendar emoji and recurrence
- ✅ Responsive views across devices
- ✅ Multilingual rendering
- ✅ Login and logout flows
- ✅ Form errors and validation messages

---

## 🐞 Bug Log

The full log can be viewed here: 
---

## 🔒 Security & Deployment

- Environment variables managed via `.env` and Render secrets
- Django `DEBUG=False` in production
- Cloudinary media storage
- Input validation on all forms
- Deployment via Render using `gunicorn`

---

## ⚙️ Technologies Used

- Python 3.13
- Django 5.x
- PostgreSQL
- HTML5 / CSS3 / Bootstrap 5
- JavaScript
- Cloudinary for images/videos
- Git, GitHub, Render.com

---

## 🧾 Version Control

- GitHub repo with over 50 commits
- Clear commit messages

---

## 🙏 Credits & Attribution

- Site and content design by Kim
- Calendar recurrence logic adapted from open-source examples
- Logo and images designed by Kim for The English Studio

