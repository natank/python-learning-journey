# Cafe API

A RESTful API for managing cafe information including location, amenities, and pricing.

## Documentation Traceability

**Foundation Setup**: [01-FOUNDATION-INFRASTRUCTURE.md](../../docs/Cafe%20API/01-FOUNDATION-INFRASTRUCTURE.md) - Complete containerized infrastructure setup
**Architecture**: [ARCHITECTURE.md](../../docs/Cafe%20API/ARCHITECTURE.md) - Detailed technical architecture
**Project Context**: [context.md](../../docs/Cafe%20API/context.md) - Project overview and requirements

## Features

- **Database**: SQLAlchemy with SQLite (local dev) / PostgreSQL (containerized)
- **Framework**: Flask 3.1.0
- **ORM**: SQLAlchemy 2.0.37 with typed mappings
- **Python Version**: 3.13.1
- **Container Runtime**: Podman with Podman Compose
- **PostgreSQL**: 16-alpine

## Project Structure

```
cafe-api/
├── src/
│   ├── main.py           # Main Flask application
│   └── templates/
│       └── index.html    # API documentation page
├── Containerfile         # Container image definition
├── compose.yml           # Podman Compose configuration
├── requirements.txt      # Python dependencies
├── project.json          # Nx project configuration
├── .env.example          # Environment variables template
├── pytest.ini            # Test configuration
└── README.md
```

## Setup Instructions

### Development Mode Options

You can run the Cafe API in two modes:

#### Option A: Containerized with Podman (Recommended)
Uses PostgreSQL database in containers - production-like environment.

#### Option B: Local Python Environment
Uses SQLite database - simpler for quick iterations.

---

### Option A: Containerized Development (Podman)

#### Prerequisites
- Podman installed (`brew install podman` on macOS)
- Podman Compose installed (`brew install podman-compose` on macOS)

#### 1. Create Environment File
```bash
cd apps/cafe-api
cp .env.example .env
# Edit .env if you want to change default credentials
```

#### 2. Start Services
```bash
# Using nx
nx run cafe-api:podman:up

# Or manually
cd apps/cafe-api
podman-compose up --build -d
```

This will start:
- **PostgreSQL** on `localhost:5432`
- **Cafe API** on `http://localhost:5000`

#### 3. View Logs
```bash
nx run cafe-api:podman:logs
```

#### 4. Stop Services
```bash
nx run cafe-api:podman:down
```

#### Other Podman Commands
```bash
# Restart just the API container
nx run cafe-api:podman:restart

# View all containers
podman ps

# Access PostgreSQL CLI
podman exec -it cafe-api-postgres psql -U cafe_user -d cafe_db
```

---

### Option B: Local Python Development

#### 1. Install Dependencies
```bash
# Using nx
nx run cafe-api:install

# Or manually
cd apps/cafe-api
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 2. Run the Development Server
```bash
# Using nx
npm run cafe-api
# or
nx serve cafe-api

# Or manually
cd apps/cafe-api
source venv/bin/activate
python src/main.py
```

The API will be available at `http://localhost:5000`

**Note**: This mode uses SQLite (`cafes.db` file) instead of PostgreSQL.

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

## Architecture

### Backend
- **Framework**: Flask REST API
- **Database**: SQLAlchemy ORM
- **Local Dev**: SQLite (file-based)
- **Containerized**: PostgreSQL 16 (production-like)

### Container Architecture
```
┌─────────────────────────────────────┐
│      Podman Compose Network         │
│  ┌──────────────┐  ┌─────────────┐  │
│  │  Cafe API    │→ │ PostgreSQL  │  │
│  │  Flask:5000  │  │   :5432     │  │
│  └──────────────┘  └─────────────┘  │
│         ↓                            │
│   Volume: ./src (hot reload)         │
│   Volume: postgres_data (persist)    │
└─────────────────────────────────────┘
```

### Frontend (Future)
- React/Vue.js SPA for cafe management
- API consumption via fetch/axios
- Containerized with Nginx

## Development Roadmap

1. ✅ Basic Flask app setup with nx integration
2. ✅ Podman Compose configuration with PostgreSQL
3. 🔄 Implement CRUD endpoints incrementally
4. ⏳ Add input validation and error handling
5. ⏳ Implement API authentication
6. ⏳ Add frontend application
7. ⏳ Write comprehensive tests
8. ⏳ Production deployment configuration

## Testing

```bash
nx test cafe-api
```

## Environment Variables

When running with Podman Compose, the following environment variables are available:

| Variable | Default | Description |
|----------|---------|-------------|
| `POSTGRES_USER` | `cafe_user` | PostgreSQL username |
| `POSTGRES_PASSWORD` | `cafe_password` | PostgreSQL password |
| `POSTGRES_DB` | `cafe_db` | PostgreSQL database name |
| `DATABASE_URL` | Auto-generated | Full database connection string |
| `FLASK_ENV` | `development` | Flask environment |
| `FLASK_DEBUG` | `1` | Enable Flask debug mode |

## Notes

- **Local mode**: Database file `cafes.db` created in `instance/` directory
- **Container mode**: PostgreSQL data persisted in named volume `postgres_data`
- Debug mode enabled for development
- API runs on `0.0.0.0:5000` to allow container access
- Hot reload enabled in container mode (src/ directory mounted)
