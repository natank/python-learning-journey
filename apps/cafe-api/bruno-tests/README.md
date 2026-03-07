# Bruno API Tests - Cafe API

Comprehensive API testing collection for the Cafe API using [Bruno](https://www.usebruno.com/), a fast and Git-friendly open-source API client.

## Overview

This Bruno collection provides complete test coverage for all Cafe API endpoints with:
- Pre-configured environments (Local & Podman)
- Automated test assertions
- Request/response documentation
- Form data examples
- Query parameter templates

## Collection Structure

```
bruno-tests/
├── bruno.json                    # Collection configuration
├── environments/
│   ├── Local.bru                # Local development environment
│   └── Podman.bru               # Podman containerized environment
├── GET Random Cafe.bru          # Random cafe endpoint
├── GET All Cafes.bru            # All cafes endpoint
├── GET Search Cafes.bru         # Search by location endpoint
├── POST Add Cafe.bru            # Create new cafe endpoint
├── PATCH Update Price.bru       # Update price endpoint (stub)
├── DELETE Report Closed.bru     # Delete cafe endpoint (stub)
└── README.md                    # This file
```

## Prerequisites

1. **Install Bruno**
   ```bash
   # macOS
   brew install bruno
   
   # Or download from https://www.usebruno.com/downloads
   ```

2. **Start the Cafe API**
   ```bash
   # Option 1: Podman (recommended)
   nx run cafe-api:podman:up
   
   # Option 2: Local Python
   nx run cafe-api:serve
   ```

3. **Seed the Database** (if not already done)
   ```bash
   podman exec cafe-api-app python src/seed_data.py
   ```

## Getting Started

### 1. Open Collection in Bruno

1. Launch Bruno application
2. Click "Open Collection"
3. Navigate to: `apps/cafe-api/bruno-tests`
4. Select the folder (Bruno will detect `bruno.json`)

### 2. Select Environment

In Bruno's top bar:
- Select **"Local"** for local Python development
- Select **"Podman"** for containerized environment

Both environments use `http://localhost:5000` by default.

### 3. Run Requests

**Using Bruno GUI**:
- Click on any request in the sidebar
- Click "Send" button (or press `Ctrl/Cmd + Enter`)
- View response and test results
- Run all: Right-click collection root → "Run Collection"

**Using Bruno CLI**:
```bash
# Run all tests (use --noproxy for localhost)
bru run --env Local --noproxy

# Run with output file
bru run --env Local --noproxy --output results.json

# Generate HTML report
bru run --env Local --noproxy --format html --output report.html
```

**⚠️ Important**: Always use `--noproxy` flag when testing localhost APIs if you have system proxy configured.

## Endpoints Overview

### ✅ Implemented Endpoints

| Request | Method | Endpoint | Description | Tests |
|---------|--------|----------|-------------|-------|
| GET Random Cafe | GET | `/random` | Get random cafe | 4 assertions |
| GET All Cafes | GET | `/all` | Get all cafes | 4 assertions |
| GET Search Cafes | GET | `/search?location=X` | Search by location | 4 assertions |
| POST Add Cafe | POST | `/add` | Create new cafe | 5 assertions |

### ⏳ Stubbed Endpoints

| Request | Method | Endpoint | Status |
|---------|--------|----------|--------|
| PATCH Update Price | PATCH | `/update-price/:id` | Not implemented |
| DELETE Report Closed | DELETE | `/report-closed/:id` | Not implemented |

## Request Details

### 1. GET Random Cafe

**Endpoint**: `GET /random`

**Tests**:
- ✅ Status code is 200
- ✅ Response has cafe object
- ✅ Cafe has required fields
- ✅ Boolean fields are boolean type

**Example Response**:
```json
{
  "cafe": {
    "id": 1,
    "name": "Science Gallery Cafe",
    "location": "Pearse St, Dublin 2",
    "has_wifi": true,
    "coffee_price": "€3.50"
  }
}
```

### 2. GET All Cafes

**Endpoint**: `GET /all`

**Tests**:
- ✅ Status code is 200
- ✅ Response has cafes array
- ✅ Cafes array is not empty
- ✅ Each cafe has required fields

**Example Response**:
```json
{
  "cafes": [
    { "id": 1, "name": "Science Gallery Cafe", ... },
    { "id": 2, "name": "The Fumbally", ... }
  ]
}
```

### 3. GET Search Cafes

**Endpoint**: `GET /search?location=Dublin 2`

**Query Parameters**:
- `location` (required): Location to search for

**Tests**:
- ✅ Status code is 200
- ✅ Response has cafes array
- ✅ All cafes match location filter
- ✅ Each cafe has required fields

**Modify Query**:
Edit the `params:query` section in Bruno to test different locations:
```
params:query {
  location: Dublin 8
}
```

### 4. POST Add Cafe

**Endpoint**: `POST /add`

**Body Type**: `form-urlencoded`

**Required Fields**:
- `name`: Cafe name (unique)
- `map_url`: Google Maps URL
- `img_url`: Image URL
- `location`: Location description
- `seats`: Seating capacity
- `has_toilet`: 1 or 0
- `has_wifi`: 1 or 0
- `has_sockets`: 1 or 0
- `can_take_calls`: 1 or 0
- `coffee_price`: Price string (optional)

**Tests**:
- ✅ Status code is 201
- ✅ Response has success message
- ✅ Response includes created cafe
- ✅ Boolean fields are correctly set
- ✅ Coffee price is set correctly

**Modify Request**:
Edit the `body:form-urlencoded` section in Bruno to create different cafes.

## Test Assertions

All implemented endpoints include automated test assertions using Bruno's test syntax:

```javascript
test("Status code is 200", function() {
  expect(res.status).to.equal(200);
});

test("Response has cafe object", function() {
  expect(res.body).to.have.property('cafe');
});
```

### Viewing Test Results

After sending a request:
1. Click the "Tests" tab in the response panel
2. View passed/failed assertions
3. Green checkmarks = passed
4. Red X = failed (with error details)

## Environment Variables

Both environments define:
- `base_url`: API base URL (http://localhost:5000)
- `api_name`: Environment identifier

### Using Variables in Requests

Variables are referenced with double curly braces:
```
{{base_url}}/random
```

### Adding Custom Variables

Edit environment files (`environments/*.bru`):
```
vars {
  base_url: http://localhost:5000
  api_key: your-api-key-here
  custom_var: value
}
```

## Tips & Best Practices

### 1. Sequential Testing

Run requests in order for best results:
1. **GET Random Cafe** - Verify API is running
2. **GET All Cafes** - Check database has data
3. **GET Search Cafes** - Test filtering
4. **POST Add Cafe** - Test creation
5. **GET All Cafes** again - Verify new cafe added

### 2. Database State

The **POST Add Cafe** request creates a new cafe each time. To avoid duplicates:
- Change the `name` field before re-running
- Or reset the database by restarting containers

### 3. Modifying Requests

**Change Query Parameters**:
```
params:query {
  location: Your Location Here
}
```

**Change Form Data**:
```
body:form-urlencoded {
  name: New Cafe Name
  location: New Location
}
```

### 4. Debugging Failed Tests

If tests fail:
1. Check the "Response" tab for actual API response
2. Check the "Tests" tab for specific assertion failures
3. Verify the API is running: `curl http://localhost:5000/random`
4. Check Podman logs: `nx run cafe-api:podman:logs`

## Advanced Features

### Scripts

Bruno supports pre-request and post-response scripts:

**Pre-Request Script** (not currently used):
```javascript
// Set dynamic variables
bru.setVar("timestamp", Date.now());
```

**Post-Response Script** (not currently used):
```javascript
// Save response data for next request
bru.setVar("cafe_id", res.body.cafe.id);
```

### Chaining Requests

Use post-response scripts to chain requests:
1. POST Add Cafe → Save `cafe.id`
2. PATCH Update Price → Use saved `cafe_id`
3. DELETE Report Closed → Use saved `cafe_id`

## Troubleshooting

### Collection Not Loading

**Issue**: Bruno doesn't recognize the collection

**Solution**:
- Ensure `bruno.json` exists in the root folder
- Restart Bruno application
- Try "File → Open Collection" again

### Tests Failing

**Issue**: All tests show red X

**Solution**:
1. Verify API is running: `curl http://localhost:5000/random`
2. Check correct environment is selected
3. Verify database has data (run seed script)
4. Check Podman containers: `podman ps`

### Connection Refused

**Issue**: "Failed to fetch" or "Connection refused"

**Solution**:
1. Start the API: `nx run cafe-api:podman:up`
2. Wait for containers to be healthy
3. Verify port 5000 is not in use by another process

### 404 Errors on Search

**Issue**: Search returns 404 even with valid location

**Solution**:
- Check database has cafes: `GET /all`
- Verify location spelling matches database entries
- Try broader search terms (e.g., "Dublin" instead of "Dublin 2")

## Integration with Development Workflow

### 1. During Development

```bash
# Terminal 1: Start API
nx run cafe-api:podman:up

# Terminal 2: Watch logs
nx run cafe-api:podman:logs

# Terminal 3: Run tests after code changes
cd apps/cafe-api/bruno-tests
bru run --env Local --noproxy
```

### 2. Before Committing

Run the full collection to ensure all endpoints work:

**CLI** (Fast):
```bash
cd apps/cafe-api/bruno-tests
bru run --env Local --noproxy
```

**GUI** (Visual):
1. Right-click collection root
2. Select "Run Collection"
3. Verify all tests pass

### 3. CI/CD Integration

Bruno CLI is perfect for automated testing:

```bash
# Install Bruno CLI (one-time)
npm install -g @usebruno/cli

# In CI/CD pipeline
cd apps/cafe-api/bruno-tests
bru run --env Local --noproxy --output results.json --format json

# Generate HTML report
bru run --env Local --noproxy --output report.html --format html
```

**GitHub Actions Example**:
```yaml
- name: Install Bruno CLI
  run: npm install -g @usebruno/cli

- name: Run API Tests
  run: |
    cd apps/cafe-api/bruno-tests
    bru run --env Local --noproxy --output results.json
```

## Documentation

Each request includes inline documentation in the "Docs" tab:
- Endpoint description
- Request/response examples
- Parameter details
- Status codes
- Implementation notes

## Version Control

Bruno collections are Git-friendly:
- ✅ Plain text `.bru` files
- ✅ Easy to diff and merge
- ✅ No binary formats
- ✅ Collaborative-friendly

All files are already tracked in the repository.

## Next Steps

1. **Implement Remaining Endpoints**:
   - Update `PATCH Update Price.bru` when endpoint is implemented
   - Update `DELETE Report Closed.bru` when endpoint is implemented

2. **Add More Tests**:
   - Edge cases (empty strings, special characters)
   - Error scenarios (duplicate names, invalid data)
   - Performance tests (response time assertions)

3. **Environment Expansion**:
   - Add "Production" environment
   - Add "Staging" environment
   - Configure different base URLs

## Resources

- **Bruno Documentation**: https://docs.usebruno.com/
- **Cafe API Docs**: `../../docs/Cafe API/`
- **API Implementation**: `../src/main.py`

## Support

For issues or questions:
1. Check this README
2. Review endpoint documentation in Bruno (Docs tab)
3. Check API logs: `nx run cafe-api:podman:logs`
4. Review implementation: `apps/cafe-api/src/main.py`

---

**Last Updated**: March 7, 2026
**Collection Version**: 1.0
**API Version**: Phase 3 (CRUD endpoints implemented)
