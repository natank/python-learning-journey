this project will be an nx monorepo for several projects written in python and nodejs. we will begin with a simple python project and a simple nodejs project.
the nodejs project will be a simple express server written in typescript.
the python project will be a simple flask server written in python.

## Quick Start

See [SETUP.md](SETUP.md) for detailed setup and execution instructions.

### Install Dependencies
```bash
npm install
cd apps/flask-server && pip install -r requirements.txt && cd ../..
```

### Run Express Server (Port 3000)
```bash
npm run express-server
```

### Run Flask Server (Port 5000)
```bash
npm run flask-server
```

### Run Python Exercises
```bash
npm run python-exercises
```

### Test Python Exercises
```bash
npm run test-python
```