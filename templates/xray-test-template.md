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

## FOR CUCUMBER/BDD TESTS

### Gherkin Definition

```gherkin
@TEST-[Number] @[Epic-Tag] @[Feature-Tag]
Feature: [Feature Name]
  As a [user role]
  I want to [perform action]
  So that [achieve goal]

  Background:
    Given [common precondition for all scenarios]
    And [another precondition]

  @smoke @positive
  Scenario: [Test Scenario Name - Happy Path]
    Given [initial state]
    And [additional context]
    When [action is performed]
    And [another action]
    Then [expected result]
    And [verification]

  @negative
  Scenario: [Test Scenario Name - Error Case]
    Given [initial state]
    When [action that causes error]
    Then [expected error behavior]
    And [error message verification]

  @edge-case
  Scenario Outline: [Parameterized Test Scenario]
    Given user has account with balance <initial_balance>
    When user attempts to transfer <amount>
    Then result should be <result>
    And balance should be <final_balance>

    Examples:
      | initial_balance | amount | result   | final_balance |
      | 1000           | 500    | success  | 500          |
      | 100            | 500    | failed   | 100          |
      | 0              | 100    | failed   | 0            |
```

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
Automated BDD test to verify fund transfer functionality including happy path, error cases, and edge cases using Gherkin syntax.

### Preconditions
**Precondition ID:** PRECOND-5

- Test database is seeded with test user accounts
- Notification service is running in test mode
- Fraud detection service is mocked
- MFA service is configured for test mode

### Gherkin Definition

```gherkin
@TEST-102 @transfers @internal-transfer @critical @automated
Feature: Internal Fund Transfer
  As a banking customer
  I want to transfer money between my own accounts
  So that I can manage my finances efficiently

  Background:
    Given the banking application is running
    And the database is in a clean state
    And the following accounts exist:
      | Account Type | Account Number | Balance |
      | Checking     | 1234567890     | 5000.00 |
      | Savings      | 0987654321     | 1000.00 |
    And user "john.doe@example.com" owns both accounts
    And user "john.doe@example.com" is authenticated
    And MFA is set up for the user

  @smoke @positive
  Scenario: Successful transfer between own accounts
    Given user is on the transfer page
    And user selects checking account "1234567890" as source
    And user selects savings account "0987654321" as destination
    When user enters transfer amount "500.00"
    And user enters description "Monthly savings"
    And user clicks "Continue" button
    Then transfer preview should be displayed
    And preview should show source account ending in "7890"
    And preview should show destination account ending in "4321"
    And preview should show amount "$500.00"
    When user clicks "Confirm Transfer" button
    And user completes MFA verification
    Then transfer should be processed successfully
    And success message "Transfer completed successfully" should be displayed
    And checking account balance should be "4500.00"
    And savings account balance should be "1500.00"
    And transaction should appear in checking account history
    And transaction should appear in savings account history
    And confirmation email should be sent to "john.doe@example.com"
    And confirmation SMS should be sent

  @negative @error-handling
  Scenario: Transfer fails with insufficient funds
    Given user is on the transfer page
    And user selects checking account "1234567890" as source
    And checking account has balance "100.00"
    When user attempts to transfer "500.00" to savings account
    And user clicks "Continue" button
    Then error message "Insufficient funds" should be displayed
    And transfer should not proceed to confirmation
    And account balances should remain unchanged

  @negative @validation
  Scenario: Transfer fails with invalid amount
    Given user is on the transfer page
    When user enters invalid amount "0.00"
    Then error message "Amount must be greater than $0" should be displayed
    And "Continue" button should be disabled
    When user enters negative amount "-100.00"
    Then error message "Invalid amount" should be displayed
    And "Continue" button should be disabled

  @edge-case @limits
  Scenario: Transfer fails when exceeding daily limit
    Given user has daily transfer limit of "10000.00"
    And user has already transferred "9500.00" today
    When user attempts to transfer "1000.00"
    Then warning message should display "This transfer will exceed your daily limit"
    And transfer should be blocked
    And user should see option to "Contact Support"

  @security @fraud-detection
  Scenario: Transfer requires additional verification for unusual activity
    Given user typically transfers small amounts
    And fraud detection service is active
    When user attempts to transfer large amount "5000.00"
    Then fraud detection should flag transaction as unusual
    And additional verification should be required
    And user should receive verification code via SMS
    And transfer should only proceed after code verification

  @edge-case @boundary
  Scenario Outline: Transfer with various amounts
    Given user has checking account with balance "<initial_balance>"
    When user attempts to transfer "<transfer_amount>" to savings
    Then transfer result should be "<result>"
    And checking account balance should be "<final_balance>"

    Examples:
      | initial_balance | transfer_amount | result  | final_balance |
      | 1000.00        | 500.00         | success | 500.00       |
      | 1000.00        | 1000.00        | success | 0.00         |
      | 1000.00        | 1001.00        | failure | 1000.00      |
      | 100.00         | 500.00         | failure | 100.00       |
      | 0.00           | 100.00         | failure | 0.00         |
      | 5000.00        | 0.01           | success | 4999.99      |

  @performance
  Scenario: Transfer completes within acceptable time
    Given performance monitoring is enabled
    When user completes a transfer of "500.00"
    Then transfer should complete within 2 seconds
    And API response time should be less than 500 milliseconds

  @compliance @audit
  Scenario: Transfer creates complete audit trail
    Given audit logging is enabled
    When user completes a transfer of "500.00"
    Then audit log should contain entry with:
      | Field          | Value                     |
      | User ID        | john.doe@example.com      |
      | Action         | INTERNAL_TRANSFER         |
      | Source Account | 1234567890                |
      | Dest Account   | 0987654321                |
      | Amount         | 500.00                    |
      | Timestamp      | [current timestamp]       |
      | IP Address     | [user's IP]               |
      | Status         | SUCCESS                   |
```

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
