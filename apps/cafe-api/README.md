# Cafe API

A RESTful API for managing cafe information including location, amenities, and pricing.

## Features

- **Database**: SQLAlchemy with SQLite (development) / PostgreSQL (production)
- **Framework**: Flask 3.1.0
- **ORM**: SQLAlchemy 2.0.37 with typed mappings
- **Python Version**: 3.13.1

## Project Structure

```
cafe-api/
├── src/
│   ├── main.py           # Main Flask application
│   └── templates/
│       └── index.html    # API documentation page
├── requirements.txt      # Python dependencies
├── project.json          # Nx project configuration
└── README.md
```

## Setup Instructions

### 1. Install Dependencies

Using nx:
```bash
nx run cafe-api:install
```

Or manually:
```bash
cd apps/cafe-api
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Development Server

Using nx:
```bash
npm run cafe-api
# or
nx serve cafe-api
```

Or manually:
```bash
cd apps/cafe-api
source venv/bin/activate
python src/main.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET Endpoints
- `GET /` - API documentation page
- `GET /random` - Get a random cafe
- `GET /all` - Get all cafes
- `GET /search?location=<location>` - Search cafes by location

### POST Endpoints
- `POST /add` - Add a new cafe

### PATCH Endpoints
- `PATCH /update-price/<cafe_id>` - Update cafe coffee price

### DELETE Endpoints
- `DELETE /report-closed/<cafe_id>` - Delete a cafe

## Database Schema

### Cafe Model
- `id` (Integer, Primary Key)
- `name` (String, Unique)
- `map_url` (String)
- `img_url` (String)
- `location` (String)
- `seats` (String)
- `has_toilet` (Boolean)
- `has_wifi` (Boolean)
- `has_sockets` (Boolean)
- `can_take_calls` (Boolean)
- `coffee_price` (String, Optional)

## Architecture Plan

### Backend
- **Framework**: Flask REST API
- **Database**: SQLAlchemy ORM
- **Development DB**: SQLite (file-based)
- **Production DB**: PostgreSQL (containerized)

### Frontend (Future)
- React/Vue.js SPA for cafe management
- API consumption via fetch/axios

### Deployment
- **Container Runtime**: Podman
- **Orchestration**: Podman Compose
- **Services**:
  - Flask API container
  - PostgreSQL database container
  - (Optional) Frontend container

## Development Roadmap

1. ✅ Basic Flask app setup with nx integration
2. 🔄 Implement CRUD endpoints incrementally
3. ⏳ Add input validation and error handling
4. ⏳ Create Podman Compose configuration
5. ⏳ Add PostgreSQL support for production
6. ⏳ Implement API authentication
7. ⏳ Add frontend application
8. ⏳ Write comprehensive tests

## Testing

```bash
nx test cafe-api
```

## Notes

- Database file `cafes.db` will be created automatically in the `instance/` directory
- Debug mode is enabled for development
- API runs on `0.0.0.0:5000` to allow container access
