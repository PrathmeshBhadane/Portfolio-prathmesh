# Portfolio Project - Prathmesh

A modern, responsive portfolio website built with Django that showcases professional experience, projects, and includes a blog section.

## 🚀 Features

### Portfolio Section
- **Professional Experience**: Display work history with company, role, dates, and descriptions
- **Project Showcase**: Highlight personal and professional projects with descriptions and links
- **Responsive Design**: Modern, mobile-friendly interface
- **Static Assets**: Custom CSS styling and profile images

### Blog Section
- **Blog Posts**: Create and manage blog content
- **Image Support**: Upload and display images for blog posts
- **Admin Interface**: Easy content management through Django admin
- **Responsive Layout**: Optimized for all device sizes

## 🏗️ Project Structure

```
portfolio_project/
├── portfolio_project/          # Main Django project
│   ├── settings.py            # Project configuration
│   ├── urls.py               # Main URL routing
│   └── wsgi.py               # WSGI application
├── portfolio/                 # Portfolio app
│   ├── models.py             # Experience & Project models
│   ├── views.py              # Portfolio views
│   ├── urls.py               # Portfolio URL routing
│   ├── templates/            # HTML templates
│   └── static/               # CSS and images
├── blog/                     # Blog app
│   ├── models.py             # Blog post model
│   ├── views.py              # Blog views
│   ├── urls.py               # Blog URL routing
│   ├── templates/            # Blog templates
│   └── static/               # Blog-specific styles
├── media/                    # User-uploaded files
│   └── blog_images/          # Blog post images
└── manage.py                 # Django management script
```

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite3 (development)
- **Frontend**: HTML5, CSS3
- **Template Engine**: Django Templates
- **Static Files**: Django Static Files
- **Media Handling**: Django Media Files

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd portfolio_project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
pip install pillow
pip install jinja2
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📱 Usage

### Portfolio Section
- **Home Page** (`/`): View your experience and projects
- **Admin Interface** (`/admin/`): Manage portfolio content

### Blog Section
- **Blog List** (`/blog/`): View all blog posts
- **Blog Detail** (`/blog/<id>/`): Read individual blog posts
- **Admin Interface** (`/admin/`): Create and manage blog posts

## 🗄️ Database Models

### Experience Model
- Company name
- Role/Position
- Start and end dates
- Job description

### Project Model
- Project title
- Description
- Project link (optional)

### Blog Model
- Post title
- Content
- Featured image
- Creation timestamp

## 🎨 Customization

### Adding Content
1. Access Django admin at `/admin/`
2. Add your professional experience
3. Upload project details
4. Create blog posts with images

### Styling
- Portfolio styles: `portfolio/static/portfolio/portfolio.css`
- Blog styles: `blog/static/blog/blog.css`
- Base template: `portfolio/templates/base.html`

## 🔧 Configuration

### Environment Variables
- `DEBUG`: Set to `False` for production
- `SECRET_KEY`: Change in production
- `ALLOWED_HOSTS`: Configure for production deployment

### Static and Media Files
- Static files are served from `static/` directories
- Media files are stored in `media/` directory
- Configure `STATIC_ROOT` and `MEDIA_ROOT` for production

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for sensitive data
- [ ] Set up proper database (PostgreSQL recommended)
- [ ] Configure static file serving
- [ ] Set up media file storage
- [ ] Configure web server (Nginx/Apache)
- [ ] Set up SSL certificate

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Prathmesh** - Portfolio Project Developer

## 📞 Support

For questions or support, please open an issue in the repository or contact the developer.

---

**Happy Coding! 🎉**
