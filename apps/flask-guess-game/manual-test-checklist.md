# Manual Test Checklist: Guess the Number Web App

## Pre-Test Setup

### Environment Setup
- [ ] Virtual environment is activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Flask server is running (`python src/main.py` or `nx serve flask-guess-game`)
- [ ] Server accessible at http://localhost:5000

### Browser Setup
- [ ] Open browser (Chrome, Firefox, Safari, or Edge)
- [ ] Open Developer Tools (F12 or Cmd+Option+I)
- [ ] Navigate to Application/Storage tab to monitor cookies/session

## Test Scenarios

### Test 1: Welcome Page (Initial Visit)
**Objective**: Verify welcome page displays correctly on first visit

**Steps**:
1. Clear browser cookies/session storage
2. Navigate to http://localhost:5000/
3. Observe the page

**Expected Results**:
- [ ] Page loads successfully (HTTP 200)
- [ ] Welcome message displayed: "Welcome to Guess the Number! I'm thinking of a number between 1 and 100."
- [ ] counter.gif image is displayed
- [ ] Input form is visible with number field
- [ ] Submit button is present
- [ ] "Start New Game" link is visible
- [ ] Session cookie is created (check Developer Tools)

---

### Test 2: Guess Too Low
**Objective**: Verify correct feedback when guess is lower than hidden number

**Steps**:
1. Continue from Test 1 (or refresh to start new game)
2. Enter a low number (e.g., 10) in the input field
3. Click "Submit Guess"

**Expected Results**:
- [ ] Page reloads with response
- [ ] Message displays: "Too low! Try a higher number."
- [ ] lower.gif image is displayed
- [ ] Input field still available for next guess
- [ ] Session persists (same cookie in Developer Tools)

---

### Test 3: Guess Too High
**Objective**: Verify correct feedback when guess is higher than hidden number

**Steps**:
1. Continue from previous test
2. Enter a high number (e.g., 90) in the input field
3. Click "Submit Guess"

**Expected Results**:
- [ ] Page reloads with response
- [ ] Message displays: "Too high! Try a lower number."
- [ ] higher.gif image is displayed
- [ ] Input field still available for next guess
- [ ] Session persists (same cookie)

---

### Test 4: Correct Guess
**Objective**: Verify success message when guessing correctly

**Steps**:
1. Continue guessing based on feedback (too low/too high)
2. When you narrow down the number, enter the correct guess
3. Click "Submit Guess"

**Expected Results**:
- [ ] Page reloads with response
- [ ] Message displays: "Congratulations! You guessed it!"
- [ ] success.gif image is displayed
- [ ] Input field still available
- [ ] Session still persists

---

### Test 5: Session Persistence
**Objective**: Verify hidden number stays the same across multiple guesses

**Steps**:
1. Start a new game (click "Start New Game" or refresh)
2. Make a guess and note the response (too low/too high)
3. Make another guess in the opposite direction
4. Verify the feedback is consistent with the same hidden number

**Expected Results**:
- [ ] Feedback is consistent (e.g., if 50 is too low, 40 should also be too low)
- [ ] Hidden number doesn't change between guesses
- [ ] Session cookie remains the same throughout

---

### Test 6: Invalid Input - Non-Numeric
**Objective**: Verify error handling for non-numeric input

**Steps**:
1. Enter text (e.g., "abc") in the input field
2. Click "Submit Guess"

**Expected Results**:
- [ ] Error message displayed: "Error: Please enter a valid number."
- [ ] HTTP 400 status code (check Network tab)
- [ ] counter.gif is displayed
- [ ] Input field still available

---

### Test 7: Invalid Input - Empty
**Objective**: Verify error handling for empty input

**Steps**:
1. Leave input field empty
2. Click "Submit Guess"

**Expected Results**:
- [ ] Browser validation prevents submission (HTML5 required attribute)
- OR
- [ ] Error message displayed
- [ ] HTTP 400 status code

---

### Test 8: Invalid Input - Float
**Objective**: Verify error handling for decimal numbers

**Steps**:
1. Enter a decimal number (e.g., "50.5") in the input field
2. Click "Submit Guess"

**Expected Results**:
- [ ] Error message displayed
- [ ] HTTP 400 status code
- [ ] Input field still available

---

### Test 9: Edge Cases - Minimum Value (1)
**Objective**: Verify game works with minimum value

**Steps**:
1. Start new game
2. Keep guessing until you determine the number is 1
3. Enter 1 and submit

**Expected Results**:
- [ ] If 1 is the hidden number: Success message displayed
- [ ] If 1 is too low: "Too low" message displayed
- [ ] No errors or crashes

---

### Test 10: Edge Cases - Maximum Value (100)
**Objective**: Verify game works with maximum value

**Steps**:
1. Start new game
2. Keep guessing until you determine the number is 100
3. Enter 100 and submit

**Expected Results**:
- [ ] If 100 is the hidden number: Success message displayed
- [ ] If 100 is too high: "Too high" message displayed
- [ ] No errors or crashes

---

### Test 11: New Game / Session Reset
**Objective**: Verify starting a new game generates a new hidden number

**Steps**:
1. Play a complete game and guess the correct number
2. Note the winning number
3. Click "Start New Game" link (navigates to `/`)
4. Make a guess and observe feedback

**Expected Results**:
- [ ] Welcome page is displayed again
- [ ] New session is created (new hidden number)
- [ ] Previous game data is cleared
- [ ] Can play a new game successfully

---

### Test 12: Browser Close - Session Cleanup
**Objective**: Verify session is cleared when browser closes

**Steps**:
1. Start a game and make a few guesses
2. Note the session cookie in Developer Tools
3. Close the browser completely (not just the tab)
4. Reopen browser and navigate to http://localhost:5000/

**Expected Results**:
- [ ] Welcome page is displayed
- [ ] New session cookie is created
- [ ] Previous session data is gone
- [ ] New hidden number is generated

---

### Test 13: Multiple Tabs - Session Isolation
**Objective**: Verify each browser session has independent game state

**Steps**:
1. Open the game in one browser (e.g., Chrome)
2. Make a guess and note the feedback
3. Open the game in a different browser (e.g., Firefox)
4. Make the same guess

**Expected Results**:
- [ ] Each browser has its own session
- [ ] Different browsers may have different hidden numbers
- [ ] Feedback may differ between browsers

---

### Test 14: URL Direct Access with Guess
**Objective**: Verify game works when accessing with URL parameter directly

**Steps**:
1. Navigate directly to http://localhost:5000/?guess=50
2. Observe the response

**Expected Results**:
- [ ] Page loads successfully
- [ ] Appropriate feedback is displayed (too low/too high/success)
- [ ] Session is initialized if not exists
- [ ] GIF image is displayed

---

### Test 15: Health Check Endpoint
**Objective**: Verify health check endpoint works

**Steps**:
1. Navigate to http://localhost:5000/health

**Expected Results**:
- [ ] HTTP 200 status code
- [ ] JSON response with `{"status": "healthy"}`

---

## Visual/UI Testing

### Responsive Design
- [ ] Test on desktop (1920x1080)
- [ ] Test on tablet (768x1024)
- [ ] Test on mobile (375x667)
- [ ] Layout adjusts appropriately for each screen size

### Browser Compatibility
- [ ] Chrome (latest version)
- [ ] Firefox (latest version)
- [ ] Safari (latest version)
- [ ] Edge (latest version)

### Visual Elements
- [ ] All GIF images load correctly
- [ ] Text is readable and properly formatted
- [ ] Colors and styling are consistent
- [ ] No layout issues or overlapping elements
- [ ] Form elements are properly styled

---

## Performance Testing

### Response Time
- [ ] Page loads in < 200ms
- [ ] Guess submission responds in < 200ms
- [ ] No noticeable lag or delays

### Resource Usage
- [ ] Images load efficiently
- [ ] No console errors in browser
- [ ] No memory leaks during extended play

---

## Security Testing

### Session Security
- [ ] Session cookie is marked as httponly (check Developer Tools)
- [ ] Session data is cryptographically signed
- [ ] Cannot manually modify session to cheat

### Input Validation
- [ ] SQL injection attempts are handled safely (N/A - no database)
- [ ] XSS attempts are sanitized
- [ ] Invalid input doesn't crash the server

---

## Test Summary

**Total Tests**: 15 core scenarios + additional checks

**Pass Criteria**:
- All core functionality tests pass
- No critical bugs or crashes
- Session management works correctly
- Error handling is appropriate
- UI is usable and responsive

**Sign-off**:
- Tester Name: _______________
- Date: _______________
- Overall Status: [ ] PASS [ ] FAIL
- Notes: _______________________________________________
