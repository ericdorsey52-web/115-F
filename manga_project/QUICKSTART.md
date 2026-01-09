# Quick Start Guide for Manga Creators Community

## 🚀 Setup Instructions

### Step 1: Install Django
```bash
pip install Django==4.2.8
```

### Step 2: Run Database Migrations
```bash
cd c:\Users\alllu\OneDrive\Documents\School\115\final\manga_project
python manage.py migrate
```

### Step 3: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account credentials.

### Step 4: Run the Development Server
```bash
python manage.py runserver
```

### Step 5: Access the Website
Open your browser and navigate to:
- **Main Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/ (login with your superuser credentials)

## 📄 Page Routes

- `/` - Home Page (index.html)
- `/register/` - Registration Page (register.html)
- `/login/` - Login Page (login.html)
- `/about/` - About/Community Guidelines Page (about.html)
- `/logout/` - Logout functionality
- `/admin/` - Django Admin Panel

## 🎨 Design Highlights

### Color Palette
- **Primary Blue**: #2563eb
- **Accent Orange**: #f97316
- **Secondary Gray**: #e5e7eb
- **Text Dark**: #1f2937

### UI Components Implemented
✅ Two-panel layouts (visual left + content right)
✅ Circular shape components (avatars)
✅ Square/Card components (image panels)
✅ Styled buttons with hover states
✅ Form elements with labels and validation
✅ Responsive grid layouts
✅ Message/Alert system

### Pages Features

#### Home Page (index.html)
- Hero section with community introduction
- Latest post display
- Three community feature cards
- Call-to-action buttons
- Login prompt in navigation (when not authenticated)

#### Register Page (register.html)
- Two-panel design
- Form with username, email, password fields
- Password confirmation validation
- Three "Why Join Us?" feature cards
- Link to login page

#### Login Page (login.html)
- Two-panel design with accent color
- Simple username/password form
- Three feature cards (what you can do when logged in)
- Link to register page

#### About Page (about.html)
- Mission statement section
- Six community guidelines cards
- Three core values with circular components
- Call-to-action section
- Comprehensive community information

## 🛠️ File Structure

```
manga_project/
├── manage.py                          # Django CLI tool
├── requirements.txt                   # Python dependencies
├── README.md                          # Full documentation
├── QUICKSTART.md                      # This file
├── .gitignore                         # Git ignore patterns
│
├── manga_project/                     # Main Django project
│   ├── __init__.py
│   ├── settings.py                    # Project settings
│   ├── urls.py                        # Main URL routing
│   └── wsgi.py                        # WSGI configuration
│
└── manga_app/                         # Django app
    ├── __init__.py
    ├── admin.py                       # Admin configuration
    ├── apps.py                        # App configuration
    ├── models.py                      # Database models (MangaPost)
    ├── views.py                       # View functions
    ├── urls.py                        # App URL routing
    │
    ├── templates/                     # HTML Templates
    │   ├── index.html                 # Home page
    │   ├── register.html              # Registration
    │   ├── login.html                 # Login
    │   └── about.html                 # About/Guidelines
    │
    └── static/                        # Static files
        ├── css/
        │   └── styles.css             # Shared stylesheet
        └── img/                       # Image assets folder
```

## 📱 Responsive Design

The CSS includes responsive breakpoints:
- **Desktop (1200px+)**: Full layouts
- **Tablet (769-768px)**: Single column layouts
- **Mobile (<480px)**: Compact layouts

All pages adapt automatically to screen size.

## 🔐 User Authentication

### Registration Flow
1. User fills out register form (username, email, password)
2. Form validates:
   - Passwords must match
   - Username must be unique
   - Email must be unique
3. User account is created
4. User is redirected to login page with success message

### Login Flow
1. User enters username and password
2. System authenticates credentials
3. If valid, user is logged in and redirected to home
4. If invalid, error message is shown
5. User welcome message appears in navigation

### Logout
- Available in navigation when user is logged in
- Logs out user and redirects to home page

## 💾 Database Models

### MangaPost Model
```python
- title (CharField, max 200 chars)
- description (TextField)
- author (ForeignKey to User)
- created_at (DateTimeField, auto-set)
- image (ImageField, optional)
```

Posts are ordered by newest first.

## 🎯 Key Features

✨ **User Registration & Login**
- Form validation
- Error messages
- Session management

✨ **Responsive Design**
- Mobile-friendly
- Tablet-optimized
- Desktop layouts

✨ **Semantic HTML**
- Proper semantic tags (main, section, form, etc.)
- Accessibility-friendly
- Clean structure

✨ **Consistent Styling**
- Single shared CSS file
- CSS variables for theming
- Utility classes for common styles

✨ **Component Library**
- Reusable cards
- Button styles (primary, secondary, accent)
- Form elements
- Circular components (avatars)
- Grid layouts

## 🚫 Troubleshooting

### "Module not found" error
Install Django:
```bash
pip install -r requirements.txt
```

### Port 8000 already in use
Run server on different port:
```bash
python manage.py runserver 8001
```

### Static files not loading
Create static files directory:
```bash
python manage.py collectstatic --noinput
```

### Database errors
Reset database:
```bash
python manage.py migrate
```

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/4.2/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/4.2/topics/templates/)

## 📝 Additional Notes

- The CSS uses modern CSS features (Grid, Flexbox, CSS Variables)
- All pages are fully responsive
- Form validation happens both client-side (HTML5) and server-side (Django)
- The project uses Django's built-in user authentication
- Static files are configured for development mode

---

Happy coding! 🎨✨
