# Projects Monorepo - Setup & Execution Guide

This is an Nx monorepo containing Python and Node.js projects.

## Prerequisites

- Node.js (v18 or higher)
- Python 3.11 or higher
- npm or yarn

## Initial Setup

### 1. Install Node.js Dependencies

```bash
npm install
```

### 2. Install Python Dependencies for Flask Server

```bash
cd apps/flask-guess-game
pip install -r requirements.txt
# Or use a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ../..
```

## Running the Projects

### Express TypeScript Server

Run the Express server on port 3000:

```bash
npm run express-server
# Or using nx directly:
nx serve express-server
```

The server will be available at: http://localhost:3000

Endpoints:
- `GET /` - Returns a welcome message
- `GET /health` - Returns health status

### Flask Python Server

Run the Flask server on port 5000:

```bash
npm run flask-guess-game
# Or using nx directly:
nx serve flask-guess-game
```

The server will be available at: http://localhost:5000

Endpoints:
- `GET /` - Returns a welcome message
- `GET /health` - Returns health status

### Running Both Servers Simultaneously

You can run both servers in separate terminal windows:

**Terminal 1:**
```bash
npm run express-server
```

**Terminal 2:**
```bash
npm run flask-guess-game
```

## Project Structure

```
projects-monorepo/
├── apps/
│   ├── express-server/          # Express TypeScript application
│   │   ├── src/
│   │   │   └── main.ts         # Express server entry point
│   │   ├── project.json        # Nx project configuration
│   │   └── tsconfig.json       # TypeScript configuration
│   └── flask-guess-game/        # Flask Python guess the number game
│       ├── src/
│       │   └── main.py         # Flask server entry point
│       ├── requirements.txt    # Python dependencies
│       └── project.json        # Nx project configuration
├── nx.json                      # Nx workspace configuration
├── package.json                 # Node.js dependencies and scripts
└── tsconfig.base.json          # Base TypeScript configuration
```

## Development

### Express Server Development

The Express server uses TypeScript and will automatically rebuild on file changes when running with `nx serve`.

### Flask Server Development

The Flask server runs in debug mode by default, which enables auto-reload on file changes.

## Environment Variables

### Express Server
- `PORT` - Server port (default: 3000)

### Flask Server
- `PORT` - Server port (default: 5000)

## Nx Commands

List all projects:
```bash
nx show projects
```

Run a specific target:
```bash
nx serve <project-name>
nx build <project-name>
```

View project graph:
```bash
nx graph
```
