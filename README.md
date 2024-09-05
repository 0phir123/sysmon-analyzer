# sysmon-analyzer


## Overview

A Django-based web application that allows users to upload and analyze Sysmon logs. It detects potential threats based on specific patterns, provides threat reporting, and allows for API-based interaction with logs.


## Features

- **Upload Sysmon Logs:** Upload JSON-formatted Sysmon logs via API.
- **Threat Detection:** Automatically analyze logs and detect threats based on specified indicators (e.g., mimikatz, lsass, sam).
- **Threat Report:** Monthly reports of detected threats.
- **Token-Based Authentication:** Secure API endpoints with token authentication.
- **API Endpoints:** Interact with logs via various endpoints (upload logs, retrieve logs by date, check for threats, etc.).


## Installation

### Prerequisites
- Python 3.8+ installed on your local machine.
- PostgreSQL (Optional for database configuration).
- Docker installed if you're planning to containerize.
- A DigitalOcean account if you're planning to deploy to the cloud.
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

  ```bash 
  sudo apt update
  sudo apt install docker.io -y
  sudo apt install docker-compose -y
  sudo systemctl start docker
  sudo systemctl enable docker
- [Git](https://git-scm.com/)


### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/sysmon-analyzer.git
   cd sysmon-analyzer
2.Environment Configuration:
Create a .env file in the project root and add the following environment variables:
  
    POSTGRES_DB=finance_db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=yourpassword
    DJANGO_SECRET_KEY=your_secret_key
    DJANGO_DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

3.Build and Run the Application:
  `sudo docker-compose up --build`
 ` sudo docker-compose exec web python manage.py migrate`
  `sudo docker-compose exec web python manage.py createsuperuser`
  `sudo docker run -p 8000:8000 sysmon_analyzer`

4.Access the Application:
  The application should be running at http://localhost:8000. You can use Postman or another tool to interact with the API.


## API Endpoints


### Reports:

- `GET /api/logs/monthly-report/<year>/<month>/` - Provides a summary of threats for a given month.
- `POST /api/upload/`  - Uploads a Sysmon log and analyzes it for threats.
- `GET /api/logs/date/<start_date>/<end_date>/` - Retrieves logs within the specified date range.
- `GET /api/logs/<log_id>/threat/` - Returns whether a specific log contains a threat.
- `GET /api/logs/<log_id>/`




## Testing

Use Postman or another API testing tool to test the endpoints. 






