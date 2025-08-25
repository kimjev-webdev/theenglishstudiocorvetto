<h1 align="center"> Welcome to The English Studio </h1>

<img src="staticfiles/compressed/logofull.webp" alt="Learn English with The English Studio" width="30%" style="float:left; margin-right: 20px;"/>

The English Studio is a full-stack web application built for a real client launching a new English language school in Corvetto, Milan. 

Designed to support both public users and administrative staff, the site offers a clean, modern user experience with powerful backend functionality tailored to real educational needs.

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

The primary objective of The English Studio website is to establish a strong and credible online presence, supporting the business from it’s foundation, by giving prospective students clear information that is easy to find and digest, which in turn should build immediate trust - reflecting that the school will be able to teach English in an easy and non-intimidating way. 

The site should foremost and administrative staff clear, engaging information and fully functional backend tools to manage classes, events, and blog content efficiently.

By combining professional design with custom backend development, the platform empowers staff to run the school independently while offering potential students an accessible, user-friendly introduction to the school's values, activities, and educational offerings.

<h3> Further Business Goals</h3>

* Enable Internal Autonomy by providing school staff with an easy-to-use interface to manage blog content, class offerings, and scheduled events without relying on developers.

* Support School Growth by ensuring the site can scale as the business grows, including room for new features such as student logins. 

* Deliver a Professional First Impression by establishing trust with potential clients through a polished, modern design and clear messaging.

* Promote Local and International Visibility by helping local residents and international users find and learn about the school online through optimized structure and engaging content.

* Ensure Data Security and Stability by storing and manage all backend data reliably using PostgreSQL and Django, with secure staff access through a private portal.

* Streamline Communication by providing a contact form with categorised inquiries and optional newsletter sign-up, reducing manual admin and improving response workflows.

* Uphold Accessibility and Responsiveness by making sure the website is usable across all devices and accessible to users with diverse needs and abilities.

<h3> 2. User Profiles </h3>

#### Parents of Young Learners (Primary Audience)

Adults seeking fun, safe, and educational after-school activities for their children aged 6–10. 
They value clear communication, a trustworthy environment, and want to stay updated on events, parties, and club sessions.
- **Needs**: A clear, visual schedule with fun event listings and details.  
- **Goals**: Help children engage joyfully with English while managing family schedules.

#### Adult English Learners
Older students who are preparing for **IELTS exams**, want to improve **Business English**, or are seeking **private lessons** tailored to their needs.  
- **Needs**: Course information, flexible options, and accessible contact forms.  
- **Goals**: Find the right learning path quickly, often with specific professional or immigration requirements in mind.

#### School Owner / Director  
The primary administrator responsible for overseeing both the school’s public image and day-to-day activity updates.  
- **Needs**: A **simple, unified portal** to manage blog posts, club sessions, and events without relying on developers or accessing the Django admin.  
- **Goals**: Keep the site’s content fresh and relevant, share insights and announcements through blog posts, and ensure the public calendar accurately reflects what's happening at the school.

#### English School Teacher / Club Organisers
Internal users like teachers and organisers who manage **recurring lessons, KET prep, Business English sessions**, and **events**
- **Needs**: A **secure internal portal** to add/edit class schedules and event details — without using the Django admin.  
- **Goals**: Keep the public-facing calendar current and reduce reliance on developer support.

#### Sponsors & Professional Partners
Visitors evaluating whether to support or collaborate with the school — possibly through **funding, co-hosting events, or promotional partnerships**.  
- **Needs**: A site that communicates **professionalism, mission clarity, and community engagement**.  
- **Goals**: Assess impact, credibility, and alignment with their values before offering support.


<h3> 3. User Stories </h3>

* As *a teacher at The English Studio*, I want to create and update a monthly schedule with weekly lessons and one-off special events like art parties or seasonal celebrations, so that the calendar always reflects the most up-to-date plan for our students and their families. 

* As *a parent*, I want to browse the site in an interactive way with my children, so we both know what kinds of events are coming up (e.g., Halloween party, Art Workshop, Picnic Day) and I can choose what my child would enjoy and prepare accordingly.

* As *the owner of the School*, I want to manage my personal blog posts and event entries from a single internal portal, so I don’t need to use the Django admin or ask for developer support to update the site.

* As a *student wanting to study in the UK* I want to find a place that offers IELTS test prep, and because I have some learning difficulties, potentially contact the school for private lesson availability which cater to my specific needs.
 
* As an *working professional*, I am required to travel to London for a meeting and really need to polish up my conversational skills fast. Im wondering if I can book group classes because there are others in my business who could benefit from Business English classes too. 

* As a *potential sponsor or partner*, I want to see a professional, well-organised site with examples of the school’s work with children, so I can feel confident about engaging with them.

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

<h2 FEATURES - DATA MODELS & STRUCTURE </h2>

<h3>1. Class Model</h3>

* Stores bilingual class names and an emoji symbol.
* Integrated with translation and dynamic display logic.

<h3> 2. Event Model </h3>

* Linked to Class via ForeignKey.
* Stores start/end times, recurrence type, and optional custom weekdays.
* Supports PostgreSQL ArrayField to store recurrence exceptions.

<h3> 3. BlogPost Model </h3>

* Stores multilingual content, featured media, publication metadata, and SEO slugs.
* Linked to the Django User model for author tracking.

<h3> FEATURES - SCHEDULED UPGRADES. </h3>

As The English Studio grows its offerings and audience, several improvements and new features are planned to expand the functionality of the website and further empower the client to manage content independently through the staff portal.

#### 1. "Upcoming Events" Modal with Flyer Uploads
A dedicated section will be added to highlight upcoming events on the homepage. This feature will:
Display a flyer thumbnail and brief title for each event.
Open a modal popup on click, revealing further event details and a larger version of the flyer.
Be fully editable by the client via the portal, allowing them to:
Upload new event flyers (image or PDF).
Enter a title, description, and optional link or signup info.
Remove or replace outdated entries.
This system will encourage parent engagement and increase visibility of the school's events.

#### 2. Editable Hero Carousel
The current homepage hero carousel is static. This will be replaced with a dynamic content system editable through the portal.
Features will include:
The ability to upload and reorder hero slides.
Fields for title text, subtitle/description, and an optional call-to-action button.
Media previews and automatic fallback handling if an image is missing.
This will allow the school to promote seasonal themes (e.g., summer camp, back-to-school offers) and direct users to relevant pages or contact options.

#### 3. Event Gallery System with List + Masonry Views
A new Gallery section will be introduced to showcase photos from past events and workshops.
Planned features:
A list view displaying all galleries by title and cover image, sorted by date or category.
Clicking a gallery will open a masonry-style image grid, showcasing all images in that gallery.
Each gallery and its photos will be fully manageable from the portal, including:
Creating a new gallery with a title and optional event tag.
Uploading multiple images at once.
Deleting or reordering images.
This system will allow The English Studio to celebrate student activities, build credibility with prospective families, and document its educational and social offerings in a vibrant, visual way.

<h2> INFORMATION ARCHITECTURE </h2>

<h3> 1. DATABASE STRUCTURE </h3>
The English Studio website uses a PostgreSQL database hosted via Render. The schema is normalized and structured to reflect real-world relationships between classes, scheduled events, and blog content.

Key relationships:
- Each Event is linked to a Class using a ForeignKey.
- Events support advanced recurrence logic including custom weekday selection and exception dates.
- Blog posts are multilingual and media-rich, including optional video and image uploads via Cloudinary.
- Models use Django’s translation system and are structured for scalability and clarity.
The three primary data models are: `Class`, `Event`, and `BlogPost`

<h3> 2. DATABASE MODELS </h3>

#### Class Model
| Field Name | Field Type | Info |
|------------|------------|------|
| name_en    | CharField  | English name of the class |
| name_it    | CharField  | Italian translation (optional) |
| emoji      | CharField  | Emoji icon used in calendar views |
| __str__()  | Method     | Dynamically returns name in current language with emoji |

#### Event Model

| Field Name              | Field Type          | Info |
|-------------------------|---------------------|------|
| class_instance          | ForeignKey (to Class) | Links event to a specific class |
| date                    | DateField           | Date of the event |
| start_time              | TimeField           | Start time of the event |
| end_time                | TimeField           | End time of the event |
| recurrence              | CharField (choices) | One-time, weekly, biweekly, monthly, custom_days |
| days_of_week            | CharField           | Used when recurrence is set to custom_days |
| recurrence_exceptions   | ArrayField          | Dates to skip for recurring events (PostgreSQL-only) |
| __str__()               | Method              | Returns readable summary of the event date and time |

#### BlogPost Model

| Field Name      | Field Type       | Info |
|-----------------|------------------|------|
| title_en        | CharField        | Blog title in English |
| title_it        | CharField        | Italian title (optional) |
| slug            | SlugField        | Auto-generated for SEO-friendly URLs |
| body_en         | RichTextField    | Full blog content in English |
| body_it         | RichTextField    | Italian blog content (optional) |
| featured_image  | CloudinaryField  | Header image for the post |
| video           | CloudinaryField  | Optional video attachment |
| author          | ForeignKey (User)| References the blog post author |
| status          | CharField        | Draft or Published |
| created_at      | DateTimeField    | Timestamp of creation |
| updated_at      | DateTimeField    | Timestamp of last update |
| published_at    | DateTimeField    | Used to control post visibility |
| get_absolute_url() | Method        | Returns dynamic URL based on slug |

<h2> TECHNOLOGIES USED </h2>

<h3> 1. LANGUAGES </h3>
- Python: Primary programming language for backend development using Django.
- HTML: Used for markup and templating in all site pages.
- CSS: Used for styling, layout adjustments, and custom visual design.
- JavaScript: Enables dynamic user interactions, form handling, and calendar logic.
- JQuery: Used for animations, modals, and handling UI click events.

<h3> 2. FRAMEWORKS </h3>

- Django (v5.2.1): Full-stack web framework used to build models, views, templates, forms, and the admin interface.
- Bootstrap 5: CSS framework for responsive grid layout and form components.
CKEditor 5: Rich text editor integrated into the blog system for staff content creation.

3. DJANGO / PYTHON PACKAGES
- cloudinary: Handles image and video uploads from the blog to a cloud-hosted media CDN.
- django-cloudinary-storage: Connects Django's storage system to Cloudinary.
- django-ckeditor: Enables WYSIWYG blog content editing.
- dj-database-url: Parses database connection strings from environment variables.
- gunicorn: WSGI server for production deployment on Render.
- pillow: Image processing library required by Django for image fields.
- psycopg2-binary: PostgreSQL database adapter.
- python-decouple / python-dotenv: Manages environment variables and API keys securely.
- requests: Used to send subscriber data to the Mailchimp API from the contact form.
- whitenoise: Efficient static file serving in production.
- sqlparse: Used by Django for admin and shell readability.
- asgiref, certifi, idna, charset-normalizer, tzdata, urllib3: Required dependencies for secure networking and timezone-aware apps.

<h3> 3. THIRD-PARTY SERVICES </h3>

- Cloudinary: Manages and hosts all uploaded blog media (images and videos).
- Mailchimp: Stores newsletter subscribers when users opt-in via the contact form.
- Google Maps API: Displays the school’s Corvetto location on the Contact page.

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
