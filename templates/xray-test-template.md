# XRay Test Case Template

## Test Information
**Test ID:** TEST-[Number]  
**Test Type:** [Manual / Automated / Cucumber / Generic]  
**Test Summary:** [Brief test description]  
**Requirement Link:** STORY-[Number]  
**Priority:** [Critical/High/Medium/Low]  
**Test Repository Folder:** [Folder path]

## Test Description
[Detailed description of what this test validates]

## Preconditions
**Precondition ID:** PRECOND-[Number] (if reusable)

[List all conditions that must be met before executing this test]
- [Precondition 1]
- [Precondition 2]
- [Precondition 3]

---

## FOR MANUAL TESTS

### Test Steps

| Step # | Action | Expected Result | Test Data |
|--------|--------|-----------------|-----------|
| 1 | [Action to perform] | [Expected outcome] | [Data to use] |
| 2 | [Action to perform] | [Expected outcome] | [Data to use] |
| 3 | [Action to perform] | [Expected outcome] | [Data to use] |

### Test Data
- **Username:** [test_user@example.com]
- **Password:** [Test@123]
- **Account Number:** [123456789]
- **Test Amount:** [$500.00]

---

## FOR AUTOMATED TESTS

### Test Scenarios

**Tags:** TEST-[Number], [Epic-Tag], [Feature-Tag]

#### Scenario 1: [Test Scenario Name - Happy Path] (smoke, positive)
**Setup:**
- [Common precondition for all scenarios]
- [Another precondition]
- [Initial state]
- [Additional context]

**Steps:**
1. [Action is performed]
2. [Another action]
3. [Expected result occurs]
4. [Verification step]

#### Scenario 2: [Test Scenario Name - Error Case] (negative)
**Setup:**
- [Initial state]

**Steps:**
1. [Action that causes error]
2. [Expected error behavior occurs]
3. [Error message is verified]

#### Scenario 3: [Parameterized Test - Multiple Test Data] (edge-case)
**Test Data Table:**

| Test Case | Initial Balance | Transfer Amount | Expected Result | Final Balance |
|-----------|----------------|-----------------|-----------------|---------------|
| Case 1    | 1000           | 500             | success         | 500           |
| Case 2    | 100            | 500             | failed          | 100           |
| Case 3    | 0              | 100             | failed          | 0             |

**Steps for each test case:**
1. User has account with balance specified in "Initial Balance" column
2. User attempts to transfer amount specified in "Transfer Amount" column
3. Result matches "Expected Result" column
4. Balance is verified to match "Final Balance" column

---

## Test Execution Details

### Test Environment
- **Environment:** [Dev/QA/Staging/Production]
- **Browser:** [Chrome/Firefox/Safari/Edge] - Version [X]
- **OS:** [Windows/Mac/Linux]
- **Device:** [Desktop/Mobile/Tablet]
- **API Version:** [v1/v2]

### Test Data Requirements
- [Specific test data needed]
- [Database state requirements]
- [Mock service requirements]

### Expected Duration
[Estimated time to execute: e.g., 5 minutes]

---

## Test Coverage

### Functional Coverage
- [ ] Happy path scenario
- [ ] Error handling
- [ ] Boundary conditions
- [ ] Edge cases

### Non-Functional Coverage
- [ ] Performance (response time)
- [ ] Security (authentication/authorization)
- [ ] Usability
- [ ] Accessibility

### Compliance Coverage
- [ ] KYC/AML requirements
- [ ] PCI-DSS requirements
- [ ] GDPR requirements
- [ ] SOX audit trail

---

## Post-Execution

### Actual Result
[To be filled during test execution]

### Status
[Pass / Fail / Blocked]

### Defects Found
- [Link to defect tickets]

### Evidence/Attachments
- [Screenshots]
- [Log files]
- [Video recordings]

### Comments
[Any additional notes from test execution]

---

## Example 1: Manual Test Case

**Test ID:** TEST-101  
**Test Type:** Manual  
**Test Summary:** Verify successful fund transfer between own accounts  
**Requirement Link:** STORY-15  
**Priority:** Critical  
**Test Repository Folder:** /Banking/Transfers/Internal

### Test Description
Verify that a customer can successfully transfer funds between their own accounts with proper balance updates, notifications, and transaction history.

### Preconditions
- User has an active account with login credentials
- User has at least two accounts (e.g., Checking and Savings)
- User's checking account has sufficient balance ($5000)
- System is operational and all services are available

### Test Steps

| Step # | Action | Expected Result | Test Data |
|--------|--------|-----------------|-----------|
| 1 | Navigate to online banking login page | Login page is displayed | URL: https://bank.example.com/login |
| 2 | Enter username and password, click Login | User is authenticated and redirected to dashboard | Username: test.user@example.com<br>Password: SecurePass@123 |
| 3 | Click on "Transfer Funds" menu option | Transfer page is displayed showing owned accounts | - |
| 4 | Select checking account as source | Checking account is selected, current balance shown as $5000.00 | Account: Checking (****1234) |
| 5 | Select savings account as destination | Savings account is selected, current balance shown as $1000.00 | Account: Savings (****5678) |
| 6 | Enter transfer amount | Amount field accepts the value | Amount: $500.00 |
| 7 | Enter transfer description | Description field accepts the value | Description: "Monthly savings" |
| 8 | Click "Continue" button | Transfer preview page is displayed with summary | - |
| 9 | Review transfer details and click "Confirm" | MFA verification prompt appears | - |
| 10 | Enter MFA code | MFA is validated | Code: [from authenticator app] |
| 11 | Verify transfer completion message | Success message: "Transfer completed successfully" is displayed | - |
| 12 | Check checking account balance | Balance updated to $4500.00 | - |
| 13 | Check savings account balance | Balance updated to $1500.00 | - |
| 14 | Check email for confirmation | Email received with transfer details within 1 minute | Email: test.user@example.com |
| 15 | Check SMS for confirmation | SMS received with transfer confirmation within 1 minute | Phone: +1-555-0123 |
| 16 | View transaction history for checking account | Transfer appears as debit transaction with timestamp | - |
| 17 | View transaction history for savings account | Transfer appears as credit transaction with timestamp | - |

### Test Data
- **Username:** test.user@example.com
- **Password:** SecurePass@123
- **Source Account:** Checking (****1234) - Balance: $5000.00
- **Destination Account:** Savings (****5678) - Balance: $1000.00
- **Transfer Amount:** $500.00
- **Description:** Monthly savings
- **Expected Duration:** 3-5 minutes

---

## Example 2: Cucumber/BDD Test Case

**Test ID:** TEST-102  
**Test Type:** Cucumber  
**Test Summary:** Verify fund transfer with various scenarios  
**Requirement Link:** STORY-15  
**Priority:** Critical  
**Test Repository Folder:** /Banking/Transfers/Internal

### Test Description
Automated test to verify fund transfer functionality including happy path, error cases, and edge cases.

### Preconditions
**Precondition ID:** PRECOND-5

- Test database is seeded with test user accounts
- Notification service is running in test mode
- Fraud detection service is mocked
- MFA service is configured for test mode

### Test Scenarios

**Tags:** TEST-102, transfers, internal-transfer, critical, automated

**Common Setup for All Scenarios:**
- Banking application is running
- Database is in a clean state
- Test accounts exist: Checking (1234567890, balance: $5000.00), Savings (0987654321, balance: $1000.00)
- User "john.doe@example.com" owns both accounts
- User "john.doe@example.com" is authenticated
- MFA is set up for the user

#### Scenario 1: Successful Transfer Between Own Accounts (smoke, positive)
1. User is on the transfer page
2. User selects checking account "1234567890" as source
3. User selects savings account "0987654321" as destination
4. User enters transfer amount "$500.00"
5. User enters description "Monthly savings"
6. User clicks "Continue" button
7. Transfer preview is displayed
8. Preview shows source account ending in "7890"
9. Preview shows destination account ending in "4321"
10. Preview shows amount "$500.00"
11. User clicks "Confirm Transfer" button
12. User completes MFA verification
13. Transfer is processed successfully
14. Success message "Transfer completed successfully" is displayed
15. Checking account balance is updated to "$4500.00"
16. Savings account balance is updated to "$1500.00"
17. Transaction appears in checking account history
18. Transaction appears in savings account history
19. Confirmation email is sent to "john.doe@example.com"
20. Confirmation SMS is sent

#### Scenario 2: Transfer Fails with Insufficient Funds (negative, error-handling)
1. User is on the transfer page
2. User selects checking account "1234567890" as source
3. Checking account has balance "$100.00"
4. User attempts to transfer "$500.00" to savings account
5. User clicks "Continue" button
6. Error message "Insufficient funds" is displayed
7. Transfer does not proceed to confirmation page
8. Account balances remain unchanged (Checking: $100.00, Savings: $1000.00)

#### Scenario 3: Transfer Fails with Invalid Amount (negative, validation)
**Test Case 3a: Zero amount**
1. User is on the transfer page
2. User enters invalid amount "$0.00"
3. Error message "Amount must be greater than $0" is displayed
4. "Continue" button is disabled

**Test Case 3b: Negative amount**
1. User is on the transfer page
2. User enters negative amount "$-100.00"
3. Error message "Invalid amount" is displayed
4. "Continue" button is disabled

#### Scenario 4: Transfer Fails When Exceeding Daily Limit (edge-case, limits)
1. User has daily transfer limit of "$10,000.00"
2. User has already transferred "$9,500.00" today
3. User attempts to transfer "$1,000.00" (total would be $10,500)
4. Warning message displays "This transfer will exceed your daily limit"
5. Transfer is blocked
6. User sees option to "Contact Support"

#### Scenario 5: Transfer Requires Additional Verification for Unusual Activity (security, fraud-detection)
1. User typically transfers small amounts (under $500)
2. Fraud detection service is active and monitoring
3. User attempts to transfer large amount "$5,000.00"
4. Fraud detection flags transaction as unusual
5. Additional verification is required
6. User receives verification code via SMS
7. User must enter verification code
8. Transfer only proceeds after successful code verification

#### Scenario 6: Transfer with Various Amounts (edge-case, boundary)
**Test Data Table:**

| Test Case | Initial Balance | Transfer Amount | Expected Result | Final Balance |
|-----------|----------------|-----------------|-----------------|---------------|
| Case 1    | $1000.00       | $500.00         | success         | $500.00       |
| Case 2    | $1000.00       | $1000.00        | success         | $0.00         |
| Case 3    | $1000.00       | $1001.00        | failure         | $1000.00      |
| Case 4    | $100.00        | $500.00         | failure         | $100.00       |
| Case 5    | $0.00          | $100.00         | failure         | $0.00         |
| Case 6    | $5000.00       | $0.01           | success         | $4999.99      |

**Steps for each test case:**
1. User has checking account with balance specified in "Initial Balance" column
2. User attempts to transfer amount specified in "Transfer Amount" column to savings
3. Transfer result matches "Expected Result" column
4. Checking account balance is verified to match "Final Balance" column

#### Scenario 7: Transfer Completes Within Acceptable Time (performance)
**Setup:**
- Performance monitoring is enabled

**Steps:**
1. User completes a transfer of "$500.00"
2. Transfer completes within 2 seconds
3. API response time is less than 500 milliseconds

#### Scenario 8: Transfer Creates Complete Audit Trail (compliance, audit)
**Setup:**
- Audit logging is enabled

**Steps:**
1. User completes a transfer of "$500.00"
2. Audit log contains entry with the following information:
   - User ID: john.doe@example.com
   - Action: INTERNAL_TRANSFER
   - Source Account: 1234567890
   - Destination Account: 0987654321
   - Amount: $500.00
   - Timestamp: [current timestamp]
   - IP Address: [user's IP address]
   - Status: SUCCESS

### Test Execution Details

**Test Environment:**
- Environment: QA
- Browser: Chrome 120+
- OS: Windows 11 / macOS 13+
- API Version: v1

**Test Data Requirements:**
- Test database with seeded user accounts
- Mock MFA service returning predefined codes
- Mock notification service for email/SMS
- Mock fraud detection service

**Expected Duration:** 2-3 minutes (automated execution)

### Test Coverage
- [x] Happy path scenario
- [x] Error handling (insufficient funds, invalid amounts)
- [x] Boundary conditions (zero, negative, exceeding limits)
- [x] Edge cases (exact balance, daily limit)
- [x] Security (fraud detection, MFA)
- [x] Performance (response time)
- [x] Compliance (audit logging)

---

## Example 3: Security Test Case

**Test ID:** TEST-103  
**Test Type:** Manual  
**Test Summary:** Verify authorization controls for fund transfer  
**Requirement Link:** STORY-15  
**Priority:** Critical  
**Test Repository Folder:** /Security/Authorization

### Test Description
Verify that users cannot transfer funds from accounts they don't own and that proper authorization checks are in place.

### Preconditions
- Two users exist in the system:
  - User A: john.doe@example.com (owns accounts 1234567890, 0987654321)
  - User B: jane.smith@example.com (owns accounts 5555555555, 6666666666)
- User A is authenticated

### Test Steps

| Step # | Action | Expected Result | Test Data |
|--------|--------|-----------------|-----------|
| 1 | User A logs in | Successfully authenticated | User: john.doe@example.com |
| 2 | User A navigates to transfer page | Transfer page loads | - |
| 3 | User A attempts to access transfer API with User B's account | API returns 403 Forbidden | API: POST /api/transfers<br>Body: {"source": "5555555555", "dest": "1234567890", "amount": 100} |
| 4 | Verify error message | "You are not authorized to access this account" | - |
| 5 | Verify transfer did not occur | Account balances unchanged | - |
| 6 | Verify security event logged | Unauthorized access attempt logged with user ID and timestamp | Check audit logs |

### Expected Duration
2 minutes

---

## Test Automation Notes

### Automation Framework
- **Language:** [Java/Python/JavaScript]
- **Framework:** [Cucumber/Selenium/TestNG]
- **Test Runner:** [JUnit/pytest/Mocha]
- **Reporting:** [Allure/ExtentReports/XRay Reports]

### CI/CD Integration
- **Pipeline:** [Jenkins/GitLab CI/Azure DevOps]
- **Trigger:** [On commit/On PR/Scheduled]
- **Test Environment:** [QA/Staging]

### Automation Script Location
- **Repository:** [Git repo URL]
- **Path:** [/tests/features/transfers/internal_transfer.feature]

---

This template provides comprehensive test case documentation for XRay integration in JIRA.
