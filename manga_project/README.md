# Manga Creators Community - Django Project

## Project Overview

This is a Django-based website for a **Manga Creators Community** where users can register, log in, and discuss their favorite manga or anime characters.

### Features

- **User Authentication**: Register and login system
- **Responsive Design**: Mobile-friendly layout using modern CSS
- **Community Discussion**: Share and discuss manga/anime characters
- **User-Friendly Interface**: Clean, welcoming design matching the prototype
- **Semantic HTML**: Proper use of HTML5 semantic tags

## Project Structure

```
manga_project/
│
├── manga_app/
│   ├── templates/
│   │   ├── index.html          # Home page
│   │   ├── login.html          # Login page
│   │   ├── register.html       # Registration page
│   │   └── about.html          # About/Community Guidelines page
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css      # Shared stylesheet
│   │   └── img/                # Image assets
│   ├── views.py                # View logic
│   ├── urls.py                 # URL routing
│   ├── models.py               # Database models
│   ├── admin.py                # Admin configuration
│   └── apps.py                 # App configuration
│
├── manga_project/
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── __init__.py
│
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies

```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd manga_project
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the website**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Pages Overview

### 1. Home Page (index.html)
- **Purpose**: Displays the latest manga/anime discussion post
- **Features**: 
  - Login/Register buttons in navigation (if not authenticated)
  - User welcome message (if authenticated)
  - Latest post display with featured content
  - Community features cards
  - Call-to-action section
- **Design**: Two-panel layout with image and content

### 2. Register Page (register.html)
- **Purpose**: Allow new users to create an account
- **Features**:
  - Username, email, password fields
  - Password confirmation validation
  - Helpful hints for each field
  - "Why Join Us?" feature cards
  - Link to login page for existing users
- **Design**: Two-panel layout with visual left panel and form right panel

### 3. Login Page (login.html)
- **Purpose**: Allow returning users to log in
- **Features**:
  - Username and password fields
  - Simple, efficient layout
  - Features showcase (what you can do when logged in)
  - Link to register page for new users
- **Design**: Two-panel layout with accent color visual panel

### 4. About Page (about.html)
- **Purpose**: Explain the community purpose and guidelines
- **Features**:
  - Mission statement
  - Six community guidelines cards
  - Core values section with circular components
  - Call-to-action section
- **Design**: Multiple sections with cards, circular components, and panels

## Design System

### Color Scheme
- **Primary Blue**: `#2563eb` - Main brand color
- **Secondary Gray/Silver**: `#e5e7eb` - Secondary elements
- **Accent Orange**: `#f97316` - CTAs and highlights
- **Text Dark**: `#1f2937` - Primary text
- **Text Light**: `#6b7280` - Secondary text
- **White**: `#ffffff` - Backgrounds and cards

### UI Components

#### Buttons
- **Primary**: Blue background with white text
- **Secondary**: Gray background with dark text
- **Accent**: Orange background with white text
- All buttons include hover states with shadow and slight lift effect

#### Form Elements
- **Input Fields**: 2px border with focus states
- **Labels**: Bold, clear labeling above inputs
- **Validation**: Client-side HTML5 validation with helpful hints

#### Cards
- **Card Component**: White background, rounded corners, shadow
- **Card Image**: Gradient backgrounds or image content
- **Card Content**: Title, description, metadata
- **Hover States**: Slight lift effect with enhanced shadow

#### Circular Shapes (Avatars/Icons)
- **Default**: Light blue background
- **Large**: 120px diameter
- **Small**: 60px diameter
- **Accent**: Orange background variant
- **Gray**: Gray background variant

#### Panels
- **Two-Panel Layout**: Grid-based, responsive layout
- **Image Panels**: Gradient backgrounds with centered content
- **Form Panels**: White backgrounds with form elements

### Typography
- **Font Family**: System fonts for optimal performance
- **Headings**: Bold, large text with blue color
- **Body Text**: 16px, 1.6 line-height for readability
- **Links**: Blue with hover effect (underline + orange color)

### Spacing
- Uses consistent rem-based spacing (0.5rem, 1rem, 1.5rem, 2rem)
- Grid gaps: 2rem-3rem for sections
- Form group margins: 1.5rem between inputs

## Responsive Design

The stylesheet includes responsive breakpoints:
- **Desktop**: Full two-panel layouts, full navigation
- **Tablet (768px)**: Single column layouts, adjusted spacing
- **Mobile (480px)**: Compact buttons, smaller fonts, flexible grids

## Database Models

### MangaPost Model
- **title**: CharField (max 200 characters)
- **description**: TextField
- **author**: ForeignKey to User
- **created_at**: DateTimeField (auto-set on creation)
- **image**: Optional ImageField
- Ordered by newest posts first

## User Stories Implementation

✅ **As a new user, I want to create an account easily**
- Dedicated register page with clear form
- Helpful hints for each field
- Link to existing login for returning users

✅ **As a returning user, I want to log in quickly**
- Simple, efficient login form
- Clear input fields and error messages
- Navigation link always available

✅ **As a user, I want clear input fields**
- All fields have descriptive labels
- Placeholder text provides hints
- Focus states clearly indicate active field

✅ **Navigation is intuitive**
- Logo links back to home
- Header navigation on all pages
- Auth buttons in top-right corner
- Footer with site information

## Django Admin Integration

Manage posts and users through Django admin:
- Admin site available at `/admin/`
- MangaPost admin with search and filtering
- User management through Django's built-in admin

## CSS Features

### CSS Variables
All colors and common values use CSS variables for easy theming:
```css
--primary-blue: #2563eb
--accent-orange: #f97316
--secondary-silver: #e5e7eb
--text-dark: #1f2937
--text-light: #6b7280
```

### Utility Classes
- Spacing: `.mt-1` through `.mt-4`, `.mb-0` through `.mb-4`
- Padding: `.px-2`, `.py-2`, `.px-3`, `.py-3`
- Text: `.text-center`, `.text-muted`, `.small`

### Transitions
All interactive elements use smooth transitions (0.3s ease)

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Future Enhancements

- User profiles with avatars
- Comment system for posts
- Like/upvote functionality
- Search and filter posts
- Notification system
- Image upload for posts
- Category/tag system for organization
- User-to-user messaging

## Troubleshooting

### Port Already in Use
If port 8000 is in use, run:
```bash
python manage.py runserver 8001
```

### Database Issues
Reset the database:
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
Collect static files:
```bash
python manage.py collectstatic
```

## Support

For issues or questions, please refer to:
- Django Documentation: https://docs.djangoproject.com/
- Project structure follows Django best practices

---

Created: January 2026
Version: 1.0
