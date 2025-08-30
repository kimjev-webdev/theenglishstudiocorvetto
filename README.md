<h1 align="center"> Welcome to The English Studio </h1>
<p align="center">
   <img src="staticfiles/compressed/logofull.webp" alt="Learn English with The English Studio" width="10%" style="margin: 0 auto; display: block;"/>
</p>

The English Studio is a fully functioning, full-stack web application built for a real client launching a new English language school in Corvetto, Milan. Designed to support both public users and administrative staff, the site offers a clean, modern user experience with powerful backend functionality tailored to real educational needs.

Key features include:
* A fully integrated blog system that allows staff to create, edit, and delete posts through a custom frontend portal.
* A dynamic class and events scheduling system with full CRUD (Create, Read, Update, Delete) operations, enabling administrators to manage weekly lessons, special events, and recurring activities via an intuitive interface.
* A flyer upload system that allows staff to create, read, update, delete and reorder the flyers.
* An administrator profile for the owner which allows them to create further staff profiles via their portal login. 
* A secure staff portal at /portal, providing private access to internal tools without exposing Django’s admin interface.
* Seamless frontend-backend integration, with JavaScript fetch requests powering smooth, interactive updates to blog posts and schedule entries.
* All data is stored in a PostgreSQL database hosted on Render, with a clean, normalized schema designed to reflect complex user stories and relationships between classes, events, and recurring schedules.
* The resulting application demonstrates professional-grade quality, both in functionality and design, and is ready to be deployed and used by the business.

<h2>UX - GOALS</h2>

<h3>1. Business Goals</h3>

<h3>Primary Goal</h3>

The primary objective of The English Studio website is to establish a strong and credible online presence from the school’s foundation, giving prospective students clear information that is easy to find and digest, which builds immediate trust — reflecting that the school can teach English in an easy, non-intimidating way.

The site should provide prospective students and administrative staff with clear, engaging information and fully functional backend tools to manage classes, events, and blog content efficiently.

By combining professional design with custom backend development, the platform empowers staff to run the school independently while offering potential students an accessible, user-friendly introduction to the school's values, activities, and educational offerings.

<h3>Further Business Goals</h3>

* Enable Internal Autonomy by providing staff with an easy-to-use portal to manage blog content, flyers, and scheduled events without relying on developers.
* Support School Growth by ensuring the site can scale with new features (e.g. optional future student logins).
* Deliver a Professional First Impression through a polished, modern design and clear messaging.
* Promote Local and International Visibility with an optimized structure, engaging content, and a clear public calendar.
* Ensure Data Security and Stability by storing and managing data with PostgreSQL and Django, and restricting staff access via a private portal.
* Streamline Communication through a categorized contact form and optional newsletter sign-up (Mailchimp).
* Uphold Accessibility and Responsiveness so the site is usable across devices and considerate of diverse user needs.

<h3>2. User Profiles</h3>

#### Parents of Young Learners (Primary Audience)
Adults seeking fun, safe, and educational after-school activities for children aged 6–10.
- <b>Needs</b>: A clear, visual schedule with fun event listings and details.
- <b>Goals</b>: Help children engage joyfully with English while managing family schedules.

#### Adult English Learners
Students preparing for <b>IELTS</b>, improving <b>Business English</b>, or seeking <b>private lessons</b>.
- <b>Needs</b>: Course/event information, flexible options, accessible contact.
- <b>Goals</b>: Quickly find a path that fits professional or immigration requirements.

#### School Owner / Director
Administrator overseeing the school’s public image and day-to-day updates.
- <b>Needs</b>: A unified portal to manage posts, flyers, classes, and events (without Django admin exposure to the public).
- <b>Goals</b>: Keep content fresh and ensure the public calendar is accurate.

#### English School Teacher / Club Organisers
Internal users managing recurring lessons, prep courses, and events.
- <b>Needs</b>: A secure portal to add/edit class schedules and event details.
- <b>Goals</b>: Keep the public calendar current with minimal friction.

#### Sponsors & Professional Partners
Visitors evaluating collaboration or support.
- <b>Needs</b>: Clear mission, professionalism, and evidence of community engagement.
- <b>Goals</b>: Assess credibility and fit before offering support.

#### Prospective Student / Newsletter Subscriber
Visitors who want periodic updates rather than checking the site frequently.
- <b>Needs</b>: Simple newsletter opt-in and reassurance on data handling.
- <b>Goals</b>: Receive timely updates on new classes, events, and announcements.

<h3>3. User Stories</h3>

* As <i>a teacher</i>, I want to create and update a monthly schedule with weekly lessons and one-off events, so the calendar always reflects the latest plan.
* As <i>a parent</i>, I want to browse upcoming events with my child (e.g., Halloween party, Art Workshop), so we can choose activities and prepare.
* As <i>the owner</i>, I want to manage blog posts, flyers, and event entries from an internal portal, so I don’t need developer help or the public Django admin.
* As <i>a student planning to study in the UK</i>, I want to find IELTS prep and contact the school for private lesson availability tailored to my needs.
* As <i>a working professional</i>, I want to quickly see Business English options (group or private) so I can prepare for meetings or team training.
* As <i>a prospective sponsor/partner</i>, I want to see a professional, well-organised site with examples of work, so I feel confident collaborating.
* As <i>a visitor</i>, I want to select a category in the contact form (e.g., general inquiry, private lesson, event booking) so my message reaches the right staff member.
* As <i>a prospective student or parent</i>, I want to sign up for the newsletter so I can receive updates on classes and events without checking the site manually.

<h2> UX - VISUAL DESIGN </h2>

SECTION WITH WIREFRAMES, BRANDING (FONTS, ICONS, COLOURS)

<h2> FEATURES - ALL PAGES (loaded by base.html) </h2>

<h3> 1. Navbar </h3>
<h3> 2. Footer </h3> 

<h2> FEATURES - TECHNICAL </h2>

1. Language Switching: Internationalization (i18n) enabled, with Italian and English support.
2. Custom form handling: Both blog and schedule management use Django forms enhanced with JavaScript fetch for interactive validation and smooth submission.
3. Environment variables: Sensitive settings (e.g., Cloudinary, Mailchimp API keys) are stored securely and never hard-coded.
4. Media Handling: Cloudinary used for image/video hosting.
5. Security: Portal routes are protected from public access.
6. Deployment: Live site hosted on Render with PostgreSQL, secure API keys, and Mailchimp integration managed via environment variables.
7. Custom Recurrence Logic: Event scheduling logic uses datetime and calendar modules to calculate all valid recurrence dates dynamically.

<h2> FEATURES - PUBLIC </h2>
<h3> 1. Homepage (index.html) </h3>

* Professionally designed landing page includes hero carousel with AI generated images to match the schools clean aesthetic. The hero carousel uses overlay formed of headings and a single sentence description to highlight class options and ‘LEARN MORE’ CTA on each slide link to the details on ‘WHAT WE OFFER’ section further down the page. 
* A personal feel is instantly created by introducing the teacher in the ‘LEARN ENGLISH WITH LEANNE’ section below - trust is gained through displaying notable experience. A signature to sign of the paragraph instills that personal feeling. 
* After formal introduction the user can browse the class selection. AI generated icons offer supplement to the information in a table format which highlight the selection of classes and events on offer.
* All content on the homepage can be translated between English and Italian via the flags located in the navigation bar. 

<h3> 2. Blog (blog_list.html / blog_detail.html) </h3>

* Upon navigating to the blog users are met with the ‘list’ of blog enteries. 
* Each blog entry is displayed as a ‘card’ with a feature image, title, and date.
* When users click on a ‘card’ to read a blog post they navigate to a page on which the feature image is enlarged and presented next to the text content of the blog.
* Blog posts can also support video alongside the text content. 
* Previous/Next navigation appears at the bottom of each post so that users may browse through the available posts in chronological order 
* Alternatively users can return to the ‘blog list’ view via a button underneath each post. 
* URLs are SEO-friendly via auto-generated slugs.
* Just like the homepage all content on the blog can be translated between English and Italian via the flags located in the navigation bar.

<h3> 3. Interactive Schedule Calendar (calendar.html)</h3>

* Events and classes are displayed in a custom calendar view via the ‘SCHEDULE’ button in the sites navigation. 
* The calendar on the site utlizes Emoji-based icons are used to represent different types of classes (e.g., 🎨 Art Workshop, 🎃 Halloween Party), for several reasons
1. It is fun! Appealing to the primary audience (parents & school children)
2.  It is designed so that children are encouraged to invest in their English learning and plan activities with their parents. Involving the children in the decision making progress to instill their sense of autonomy and actively promoting engagement. 
3. Emojis allow the schedule to be really dynamic - the text information is then displayed within a tooltip which appears when a date field is hovered or tapped.

* To improve UX a date which contains mutliple events/ emojis - shows details for all of the events on that day within a single tooltip. This also improves accessibility by creating a larger touch target.
* Calendar includes month-switching logic with dynamic date navigation, so users can see what has happened in previous months, but also plan way ahead into the future/look at what events start happening during term time. 

<h3> 4.  Contact Form with Mailchimp Integration (contact.html) </h3>

* Accessible form collects name, email, phone, subject, and message.
* Emails are sent with reply_to headers to the school address.
* Users can opt in to a newsletter via Mailchimp API integration.
* Google Maps API is embedded to show the school’s location with a custom pin which uses the schools branding. 

<h2> FEATURES - STAFF PORTAL (/portal) </h2>

<h3> 1. Login Page (portal/login) </h3>

* Secure, password-protected login view built using Django’s authentication system.
* Customised frontend styling for a consistent user experience.
* On successful login, users are redirected to the main dashboard.

<h3> 2. Dashboard (portal) </h3>

* Acts as a central hub for navigating between blog and schedule management.
* Accessible via /portal/ after login.
* Includes super quick links and visual cues to streamline admin workflows.

<h3> 3. Blog Post Management </h3>

Staff can:
* Create new posts with sections to populate in English and Italian so the site remains bilingual.
* Upload images and video to Cloudinary.
* Edit or delete posts.
* Backdate posts
* Toggle post status between draft and published.
* Posts are updated asynchronously using JavaScript fetch requests for a smooth experience.

<h3> 4. Schedule Management </h3>

* Full CRUD support for both models:
1. Classes can be created with a name and emoji, and translated into Italian.
2. Events can be created, edited, or deleted and linked to any class.

* Events support multiple recurrence options: One time, weekly, biweekly, monthly or custom days. Recurrence options are fully customisable via the portal.
* Admins can specify recurrence exceptions (e.g., no class during holidays) this also drastically improves the UX as it prevents a lot of admin in the backend - otherwise  reoccurring events would need to be deleted due to calendar clashes with a one off event.
* Form validation ensures valid date/time input and prevents scheduling conflicts.

<h3> 5. Upcoming Events Flyers Management </h3>
Staff can:  
* Create new flyers with bilingual fields (EN/IT).  
* Upload flyer images and optional PDF attachments.  
* Toggle flyer visibility and reorder flyers using `sort_order`, so the homepage displays them in the desired sequence.  
* Edit or delete flyers directly from the portal.  

<h3> 6. User Management </h3>
Staff with the correct privileges can:  
* Create new user accounts.  
* Delete users or reset their passwords.  
* Assign or update user roles and permissions (staff/superuser).  
* Manage access rights without exposing the public Django admin.  

<h2> INFORMATION ARCHITECTURE </h2>

<h3>1. Database Structure</h3>
The English Studio website uses a PostgreSQL database hosted via Render.  
The schema reflects real-world relationships between classes, events, flyers, and blog content.

Key relationships:
- Each Event is linked to a Class via a ForeignKey.  
- Events support advanced recurrence logic with exceptions.  
- BlogPosts are multilingual and media-rich, linked to the User model.  
- Flyers store bilingual descriptions and control homepage ordering.  

The primary custom models are: `Class`, `Event`, `BlogPost`, and `Flyer`.  

<h3>2. Database Models</h3>

#### Class Model
| Field Name | Field Type | Info |
|------------|------------|------|
| name_en    | CharField  | English name |
| name_it    | CharField  | Italian name (optional) |
| emoji      | CharField  | Emoji icon for calendar |
| __str__()  | Method     | Returns name in current language with emoji |

#### Event Model
| Field Name            | Field Type           | Info |
|-----------------------|----------------------|------|
| class_instance        | ForeignKey(Class)    | Links event to a class |
| date                  | DateField            | Date of the event |
| start_time            | TimeField            | Start time |
| end_time              | TimeField            | End time |
| recurrence            | CharField (choices)  | One-time, weekly, biweekly, monthly, custom_days |
| days_of_week          | CharField            | Stores weekdays if recurrence = custom_days |
| recurrence_exceptions | ArrayField           | Dates to skip for recurring events |
| __str__()             | Method               | Returns readable event summary |

#### BlogPost Model
| Field Name      | Field Type        | Info |
|-----------------|-------------------|------|
| title_en        | CharField         | English title |
| title_it        | CharField         | Italian title (optional) |
| slug            | SlugField         | SEO-friendly URL |
| body_en         | RichTextField     | English content |
| body_it         | RichTextField     | Italian content |
| featured_image  | CloudinaryField   | Header image |
| video           | CloudinaryField   | Optional video |
| author          | ForeignKey(User)  | Blog post author |
| status          | CharField         | Draft or Published |
| created_at      | DateTimeField     | Creation time |
| updated_at      | DateTimeField     | Last update |
| published_at    | DateTimeField     | Publication control |
| get_absolute_url() | Method          | Returns URL based on slug |

#### Flyer Model
| Field Name     | Field Type       | Info |
|----------------|------------------|------|
| title_en       | CharField        | English title |
| title_it       | CharField        | Italian title |
| description_en | CharField        | English description |
| description_it | CharField        | Italian description |
| image          | CloudinaryField  | Flyer image |
| file           | CloudinaryField  | PDF upload (optional) |
| event_date     | DateField        | Event date |
| publish        | BooleanField     | Controls visibility |
| sort_order     | IntegerField     | Controls homepage order |
| created_at     | DateTimeField    | Creation timestamp |

<h3>3. Entity Relationship Diagram (ERD)</h3>

The following ERD visualizes the relationships between the primary models in the project (`Class`, `Event`, `BlogPost`, `Flyer`, and `User`).  

<img src="docs/erd.png" alt="Entity Relationship Diagram for The English Studio" width="800"/>

*The diagram above was generated automatically using SchemaCrawler from the live PostgreSQL database.*

<h2> TECHNOLOGIES USED </h2>

<h3> 1. LANGUAGES </h3>
- Python: Primary programming language for backend development using Django.  
- HTML: Used for markup and templating in all site pages.  
- CSS: Used for styling, layout adjustments, and custom visual design.  
- JavaScript: Enables dynamic user interactions, form handling, and calendar logic.  

<h3> 2. FRAMEWORKS </h3>
- Django (v5.2.1): Full-stack web framework used to build models, views, templates, forms, and the custom portal interface.  
- Bootstrap 5: CSS framework for responsive grid layout and form components.  
- CKEditor (via django-ckeditor): Rich text editor integrated into the blog system for staff content creation.  

<h3> 3. DJANGO / PYTHON PACKAGES </h3>
- cloudinary: Handles image and video uploads to a cloud-hosted media CDN.  
- django-cloudinary-storage: Connects Django's storage system to Cloudinary.  
- django-ckeditor: Enables WYSIWYG blog content editing.  
- dj-database-url: Parses database connection strings from environment variables.  
- gunicorn: WSGI server for production deployment on Render.  
- pillow: Image processing library required by Django for image fields.  
- psycopg2-binary: PostgreSQL database adapter.  
- python-decouple / python-dotenv: Manages environment variables and API keys securely.  
- python-dateutil: Provides advanced date and time utilities, used in scheduling recurring classes and events.  
- requests: Used to send subscriber data to the Mailchimp API from the contact form.  
- whitenoise: Efficient static file serving in production.  
- sqlparse: Used by Django for admin and shell readability.  
- asgiref, certifi, idna, charset-normalizer, tzdata, urllib3: Required dependencies for secure networking and timezone-aware apps.  

<h3> 4. THIRD-PARTY SERVICES </h3>
- Cloudinary: Manages and hosts all uploaded blog media (images and videos).  
- Mailchimp: Stores newsletter subscribers when users opt-in via the contact form.  
- Google Maps API: Displays the school’s Corvetto location with a custom map pin.  
- ChatGPT: Assisted in generating carousel images and class description icons.  
- GoDaddy: Provides domain registration and hosting for the site’s custom domain.  

<h3> 5. DATABASE </h3>
- PostgreSQL: Relational database used for storing all project data.  

<h3> 4. DEPLOYMENT & DEV TOOLS </h3>

- Render: Hosting platform for both the Django backend and PostgreSQL database.
- GitHub: Used for version control and collaborative development.
- GitHub Codespaces: Cloud-based development environment.
Environment Variables (.env): Used to securely store all API keys, database credentials, and sensitive settings.

<h2> TESTING </h2> 

<h3>1. About Testing</h3>
The English Studio website has undergone extensive testing throughout development to ensure all functionality works as intended, is accessible to users, and meets modern usability standards.
A full breakdown of all tests can be found in TESTING.md. Additional debugging history is logged in detail in BUGLOG.md.

* Every time a feature was implemented or updated, the entire site was manually reviewed to confirm no regressions occurred across views, forms, and interactions.
* The project has been tested by non-technical users to simulate real-world interactions with the target audience.
* Features like the calendar, contact form, and blog were tested for performance, form validation, and response handling.
* A wide range of devices and screen sizes were tested manually to ensure responsive design and interactive stability.
* Colour contrast was checked and adjusted where needed to ensure WCAG 2.1 compliance.
* CSS code was validated using Jigsaw W3C Validator and passed without errors.

The document including a table with all tests can be found [here](TESTING.md).

<h3> 2. Validation </h3>
The validation section of the testing document can be found [here](TESTING.md#validation)

</h3> 3. Mobile & Desktop Testing </h3>
The mobile & desktop testing section of the testing document can be found [here](TESTING.md#mobiletesting)

<h3> 4. Manual Testing </h3>
The manual testing section of the testing document can be found [here](TESTING.md#manual)

<h3> 5. User Story Testing </h3>
The user story testing section of the testing document can be found [here](TESTING.md#user)

<h3> 6. Bugs </h3>
A comprehensive log of all debugging actions taken throughout the project timeline can be found [here](BUGLOG.md).

There is also a list of bugs which are yet to be resolved in the [testing document](TESTING.md).

<h2> DEPLOYMENT</h2

<h3> 1. LOCAL DEPLOYMENT </h3>
To run *The English Studio* project locally for development or testing purposes:

#### REQUIREMENTS:
- Python 3.9+ installed
- An IDE such as Visual Studio Code
- pip (Python package installer)
- Git
- PostgreSQL (or SQLite for local testing only)
- Accounts with Cloudinary and Mailchimp (optional but required for full feature support)
- A `.env` file with the correct environment variables

#### SETUP INSTRUCTIONS:
1. Clone the repository from GitHub:
   git clone https://github.com/kimjev-webdev/theenglishstudiocorvetto.git

2. Navigate into the project folder:
   cd theenglishstudiocorvetto

3. (Recommended) Set up and activate a virtual environment:
   python3 -m venv .venv  
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Create a `.env` file in the root directory and include the environment variables found inside env.example

6. Apply migrations and create a superuser:
   python manage.py migrate  
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

8. Visit http://127.0.0.1:8000 to access the site locally. The Django admin is accessible at `/admin`.

<h3> 2. PRODUCTION DEPLOYMENT (RENDER) </h3>

The project is deployed using **Render**, which manages the build process, static file hosting, and PostgreSQL database.

#### RENDER DEPLOYMENT STEPS:
1. Push your full project repository to GitHub.
2. Log in to https://render.com and create a new **Web Service**.
3. Select your GitHub repo and configure:
   - **Build Command**:  
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
   - **Start Command**:  
     gunicorn the_english_studio.wsgi:application
4. Under "Environment → Environment Variables", add the following config vars (matching your local `.env` - see env.example. 

5. Set up static file hosting in Render's "Static Files" section:
   - Path: /static
   - Directory: staticfiles

6. Once configured, click "Deploy" and wait for the build to finish.
7. Click "View Live" to access your live production site.

<h2> CREDIT & CONTACT </h2>
All content and structure were developed for a real-world client project. Media, blog posts, and calendar data are owned by the client.

For technical questions or collaboration inquiries, contact:
**Developer:**  
📧 kimjev.webdev@gmail.com  
🔗 https://github.com/kimjev-webdev/theenglishstudiocorvetto
