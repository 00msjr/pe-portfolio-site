# Portfolio Site - MLH Production Engineering Fellowship

A full-stack portfolio website built with Flask, featuring dynamic content management, database integration, and production deployment with Docker and Nginx.

## Live Site

**Production URL:** [https://michaelsousa.duckdns.org](https://michaelsousa.duckdns.org)

## Features

### Core Functionality
- **Dynamic Portfolio Pages**: Home, About, Work Experience, Education, Hobbies
- **Interactive Timeline**: Community timeline with post creation and viewing
- **Hobby Detail Pages**: Individual pages for each hobby with images
- **Responsive Design**: Mobile-friendly interface with dynamic navigation
- **Google Maps Integration**: Interactive map showing visited locations

### Technical Implementation
- **Backend**: Flask web framework with Python
- **Database**: MySQL/MariaDB with Peewee ORM
- **Frontend**: HTML5, CSS3, JavaScript with Jinja2 templating
- **Production Deployment**: Docker containers with Nginx reverse proxy
- **SSL/HTTPS**: Automatic SSL certificate generation with Let's Encrypt
- **Testing**: Comprehensive test suite with mocking for CI/CD compatibility

### DevOps & Infrastructure
- **Containerization**: Multi-container Docker setup (Flask app, MySQL, Nginx)
- **Reverse Proxy**: Nginx for load balancing and SSL termination
- **Automated Deployment**: Shell scripts for continuous deployment
- **Environment Management**: Separate development and production configurations

## Quick Start

### Local Development

1. **Clone and setup**
   ```bash
   git clone <repository-url>
   cd pe-portfolio-site
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp example.env .env
   # Edit .env with your configuration
   ```

3. **Run development server**
   ```bash
   export FLASK_ENV=development
   flask run
   ```

   Visit `http://localhost:5000`

### Production Deployment

1. **Deploy to VPS**
   ```bash
   ./redeploy-site.sh
   ```

2. **Verify deployment**
   ```bash
   docker ps  # Check all containers are running
   ```

## Testing

Run the comprehensive test suite:

```bash
./run_tests.sh
```

Tests include:
- Route functionality testing
- Database operations testing
- API endpoint validation
- Mock-based testing for CI/CD environments

## Project Structure

```
pe-portfolio-site/
├── app/                    # Flask application
│   ├── __init__.py        # App factory and routes
│   ├── static/            # CSS, JS, images
│   └── templates/         # Jinja2 HTML templates
├── tests/                 # Test suite
├── user_conf.d/           # Nginx configuration
├── docker-compose.prod.yml # Production Docker setup
├── Dockerfile             # Flask app container
├── requirements.txt       # Python dependencies
└── redeploy-site.sh       # Deployment script
```

## Configuration

### Environment Variables
- `MYSQL_HOST`: Database host (localhost for dev, mysql for production)
- `MYSQL_USER`: Database username
- `MYSQL_PASSWORD`: Database password
- `MYSQL_DATABASE`: Database name
- `GOOGLE_MAPS_API_KEY`: Google Maps API key for location features

### Docker Services
- **myportfolio**: Flask application container
- **mysql**: MariaDB database container
- **nginx**: Reverse proxy with SSL termination

## Future Enhancements

- [ ] GitHub Actions for CI/CD pipeline
- [ ] Monitoring and alerting system
- [ ] Troubleshooting and debugging tools
- [ ] User authentication and authorization
- [ ] Admin dashboard for content management
- [ ] Blog functionality with rich text editor
- [ ] Contact form with email integration
- [ ] Performance analytics and optimization
- [ ] CDN integration for static assets
- [ ] Multi-language support
- [ ] API documentation with Swagger
- [ ] Automated backups and disaster recovery

## Contributing

1. Create an issue for new features or bugs
2. Fork the repository
3. Create a feature branch (`git checkout -b feature/amazing-feature`)
4. Make your changes and add tests
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is part of the MLH Production Engineering Fellowship program.

## Links

- **Live Site**: [https://michaelsousa.duckdns.org](https://michaelsousa.duckdns.org)
- **Timeline Page**: [https://michaelsousa.duckdns.org/content/timeline](https://michaelsousa.duckdns.org/content/timeline)
- **Repository**: [GitHub](https://github.com/00msjr/pe-portfolio-site)
