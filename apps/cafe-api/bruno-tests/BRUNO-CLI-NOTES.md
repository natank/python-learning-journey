# Bruno CLI Testing Notes

## Installation

Bruno CLI was successfully installed:
```bash
npm install -g @usebruno/cli
# Version: 3.1.3
```

## Collection Structure

The Bruno collection is properly configured with:
- ✅ `bruno.json` - Collection configuration
- ✅ Environment files in `environments/` directory
- ✅ 6 request files (`.bru` format)
- ✅ All requests properly formatted with tests

## CLI Execution Findings

### Environment Variable Resolution

**Status**: ✅ Working

The CLI correctly resolves environment variables:
- `{{base_url}}` → `http://localhost:5000`
- Requests are properly constructed
- URLs, headers, and body data are correct

### Connection Issue - RESOLVED ✅

**Initial Status**: ⚠️ Socket Hang Up Error
**Resolution**: ✅ Disable proxy in both CLI and GUI

**Root Cause**: System proxy settings (`http://127.0.0.1:9153`) were intercepting localhost connections.

**CLI Solution**:
```bash
bru run --env Local --noproxy
```

**GUI Solution**:
1. Click **"Preferences"** tab in Bruno
2. Navigate to **"Proxy Settings"**
3. Change Mode from **"System Proxy"** to **"Off"**
4. Click "Save" and retry requests

**Results**:
- ✅ All 6 requests pass (200/201 status codes)
- ✅ All 19 test assertions pass
- ✅ Total execution time: ~48ms
- ✅ No connection errors
- ✅ Both CLI and GUI working

**Evidence from JSON output**:
```json
{
  "request": {
    "method": "GET",
    "url": "http://localhost:5000/random",
    "headers": {"content-type": null}
  },
  "response": {
    "status": "error",
    "error": "socket hang up"
  }
}
```

**API Verification**:
- ✅ Flask app is running and healthy
- ✅ Curl requests work perfectly: `curl http://localhost:5000/random`
- ✅ API logs show successful responses to curl
- ✅ Bruno CLI works with --noproxy flag
- ✅ Bruno GUI works with proxy disabled

### Root Cause Analysis

The issue appears to be related to how Bruno CLI handles HTTP connections with Flask's development server. Possible causes:

1. **HTTP/1.1 Keep-Alive**: Flask dev server may not handle keep-alive connections the same way Bruno CLI expects
2. **Connection Pooling**: Bruno CLI might be using connection pooling that conflicts with Flask
3. **Request Timeout**: Bruno CLI may have stricter timeout settings
4. **Header Handling**: Missing or incompatible headers

## Workarounds

### Option 1: Use Bruno GUI Application ✅ Recommended

The Bruno desktop application works perfectly with the collection:

```bash
# Install Bruno app
brew install bruno

# Open collection
# File → Open Collection → apps/cafe-api/bruno-tests
```

**Advantages**:
- ✅ Full test execution
- ✅ Visual test results
- ✅ Interactive debugging
- ✅ All 17 test assertions work
- ✅ No connection issues

### Option 2: Use Alternative CLI Tools

**HTTPie**:
```bash
brew install httpie

# Test endpoints
http GET http://localhost:5000/random
http GET http://localhost:5000/all
http GET "http://localhost:5000/search?location=Dublin 2"
http POST http://localhost:5000/add name="Test" location="Dublin 1" has_wifi=1
```

**curl with jq**:
```bash
# Pretty print JSON responses
curl -s http://localhost:5000/random | jq '.'
curl -s http://localhost:5000/all | jq '.cafes | length'
```

### Option 3: Python Requests Script

Create a simple Python test script using the `requests` library to automate API testing.

### Option 4: Production WSGI Server

The issue may be specific to Flask's development server. Testing with a production WSGI server (Gunicorn, uWSGI) might resolve the connection issue:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 src.main:app

# Then try Bruno CLI again
bru run --env Local
```

## Tested Commands

### ✅ Working Commands

```bash
# Check version
bru --version  # 3.1.3

# View help
bru run --help

# Run collection with proxy bypass (REQUIRED for localhost)
bru run --env Local --noproxy

# Run with output file
bru run --env Local --noproxy --output results.json

# Run with HTML report
bru run --env Local --noproxy --format html --output report.html
```

### ❌ Failed Commands (Without --noproxy)

```bash
# All produce "socket hang up" error when system proxy is active
bru run --env Local
bru run --env-file environments/Local.bru
bru run --env-var base_url=http://localhost:5000
bru run --delay 1000
bru run --insecure
```

**Fix**: Add `--noproxy` flag to all commands when testing localhost APIs.

## Collection Validation

Despite CLI connection issues, the collection itself is **fully valid**:

✅ **Request Files**: All 6 `.bru` files are properly formatted
✅ **Environment Variables**: Correctly defined and resolved
✅ **Test Assertions**: 17 total assertions across 4 implemented endpoints
✅ **Documentation**: Inline docs in each request
✅ **Form Data**: POST request body correctly encoded
✅ **Query Parameters**: Search endpoint parameters properly configured

## Recommendations

### For Development

**Option 1: Bruno CLI** (Automated Testing) ✅
```bash
bru run --env Local --noproxy
```
- Fast execution (~48ms for 6 requests)
- All 19 test assertions pass
- Perfect for quick validation
- **Remember**: Always use `--noproxy` flag for localhost

**Option 2: Bruno GUI Application** (Interactive Testing) ✅
- Visual feedback
- Easy request modification
- Test result visualization
- **Important**: Disable proxy in Preferences → Proxy Settings → Mode: Off

### For CI/CD

**Recommended**: Bruno CLI with `--noproxy` flag
```bash
# In CI/CD pipeline
bru run --env Local --noproxy --output results.json --format json

# Generate HTML report
bru run --env Local --noproxy --output report.html --format html
```

**Alternative Options**:
1. **pytest** with `requests` library
2. **Postman CLI** (Newman)
3. **Custom Python test scripts**

### For Manual Testing

Both Bruno CLI and GUI are production-ready. Choose based on preference:
- **CLI**: Fast, scriptable, terminal-based
- **GUI**: Visual, interactive, debugging-friendly

## Next Steps

1. ✅ Use Bruno GUI for manual API testing
2. ⏳ Investigate Bruno CLI + Gunicorn compatibility
3. ⏳ Consider pytest-based API tests for CI/CD
4. ⏳ Report issue to Bruno CLI GitHub repository

## Files Status

| File | Status | Notes |
|------|--------|-------|
| `bruno.json` | ✅ Valid | Collection config correct |
| `environments/Local.bru` | ✅ Valid | Variables resolve properly |
| `environments/Podman.bru` | ✅ Valid | Same as Local |
| `GET Random Cafe.bru` | ✅ Valid | 4 test assertions |
| `GET All Cafes.bru` | ✅ Valid | 4 test assertions |
| `GET Search Cafes.bru` | ✅ Valid | 4 test assertions |
| `POST Add Cafe.bru` | ✅ Valid | 5 test assertions |
| `PATCH Update Price.bru` | ✅ Valid | Stub for future |
| `DELETE Report Closed.bru` | ✅ Valid | Stub for future |

## Conclusion

The Bruno collection is **fully functional and production-ready** for both GUI and CLI usage.

### ✅ Issue Resolved

The "socket hang up" error was caused by system proxy settings intercepting localhost connections. Using the `--noproxy` flag completely resolves the issue.

### Test Results Summary

```
📊 Execution Summary
┌───────────────┬──────────────┐
│ Metric        │    Result    │
├───────────────┼──────────────┤
│ Status        │    ✓ PASS    │
├───────────────┼──────────────┤
│ Requests      │ 6 (6 Passed) │
├───────────────┼──────────────┤
│ Tests         │    19/19     │
├───────────────┼──────────────┤
│ Duration (ms) │      48      │
└───────────────┴──────────────┘
```

### Recommended Workflow

**Development**:
```bash
# CLI (fast)
bru run --env Local --noproxy

# GUI (visual) - disable proxy first
# Preferences → Proxy Settings → Mode: Off
```

**CI/CD**:
```bash
bru run --env Local --noproxy --output results.json
```

**Interactive Testing**:
- Bruno GUI Application (disable proxy in settings)

---

**Date**: March 7, 2026
**Bruno CLI Version**: 3.1.3
**Collection Version**: 1.0
**Status**: Fully Operational ✅ (CLI + GUI)
