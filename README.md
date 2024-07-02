# MySuperDataCompany

## Overview

This project is a proof of concept for MySuperDataCompany Inc., demonstrating a basic data upload, parse, and query engine. It supports JSON and CSV file uploads and provides a simple query interface for the stored data.

## Features

- File upload support for JSON and CSV formats
- Deafult data download for an uploaded files in JSON
- Docker-based deployment for easy setup and testing
- Built with Python, Django, and PostgreSQL

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone the repository:
   git clone https://github.com/amreita/mysuperdatacompany.git

   cd mysuperdatacompany
   
3. Build and start the Docker containers:
   docker-compose up --build

4. Apply database migrations:
  docker-compose exec web python manage.py migrate
   
5. The application is now running at `http://localhost:8000`

## API Endpoints

### Upload File
- **URL:** `/upload/`
- **Method:** POST
- **Content-Type:** multipart/form-data
- **Form Data:** 
- `file`: The file to upload (JSON or CSV)
- **Success Response:** 
- **Code:** 200
- **Content:** `{ "message": "File uploaded successfully" }`
- **Error Response:** 
- **Code:** 400
- **Content:** `{ "error": "Unsupported file type" }`

### Query Data
- **URL:** `/download/`
- **Method:** GET
- **URL Params:** 
- `type` (default): File type ('json')
- **Success Response:** 
- **Code:** 200
- **Content:** JSON array of data entries

## Project Structure
mysuperdatacompany/
├── myapp/
│   ├── models.py
│   ├── views.py
│   └── utils.py
├── mysuperdatacompany/
│   ├── settings.py
│   └── urls.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## Development

To make changes to the project:

1. Modify the code as needed
2. Rebuild the Docker containers:
docker-compose up --build

## Testing

For this proof of concept, testing is performed manually. Use tools like cURL or Postman to test the API endpoints.

Example cURL commands:

1. Upload a file:
curl -X POST -F "file=@path/to/your/file.json" http://localhost:8000/upload/
Copy
2. Query data:
curl http://localhost:8000/query/
   
3. Query data with type filter:
curl http://localhost:8000/query/?type=json

## Future Improvements

- Implement user authentication
- Add automated testing
- Enhance error handling and logging
- Implement more advanced querying capabilities
- Optimize for large file uploads and data processing

## Contributing

This is a proof of concept project. For any suggestions or improvements, please open an issue or submit a pull request.
