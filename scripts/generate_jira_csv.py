"""
JIRA Banking Project CSV Generator
Generates comprehensive JIRA issue structure for banking application

Usage:
    python generate_jira_csv.py --output-dir ./csv
"""

import csv
import os
from datetime import datetime
from typing import List, Dict

class JIRAIssueGenerator:
    """Generate JIRA issues for banking application"""
    
    def __init__(self, output_dir: str = "./csv"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def generate_epics(self) -> List[Dict]:
        """Generate Epic issues"""
        epics = [
            {
                "Summary": "Customer Onboarding & Authentication",
                "Issue Type": "Epic",
                "Description": "Enable secure customer registration and identity verification compliant with KYC/AML regulations.",
                "Priority": "High",
                "Labels": "onboarding,security,kyc,aml,compliance,phase-1,mvp",
                "Epic Name": "Customer Onboarding & Authentication",
                "Story Points": 100
            },
            {
                "Summary": "Account Management",
                "Issue Type": "Epic",
                "Description": "Provide comprehensive account viewing and management capabilities.",
                "Priority": "High",
                "Labels": "accounts,core-banking,phase-1",
                "Epic Name": "Account Management",
                "Story Points": 80
            },
            {
                "Summary": "Fund Transfers & Payments",
                "Issue Type": "Epic",
                "Description": "Enable secure and efficient money movement.",
                "Priority": "Critical",
                "Labels": "payments,transfers,core-banking,security,phase-2",
                "Epic Name": "Fund Transfers & Payments",
                "Story Points": 120
            },
            {
                "Summary": "Card Management",
                "Issue Type": "Epic",
                "Description": "Comprehensive debit and credit card lifecycle management.",
                "Priority": "High",
                "Labels": "cards,payments,phase-3",
                "Epic Name": "Card Management",
                "Story Points": 90
            },
            {
                "Summary": "Security & Fraud Prevention",
                "Issue Type": "Epic",
                "Description": "Protect customer accounts through real-time fraud detection.",
                "Priority": "Critical",
                "Labels": "security,fraud-detection,compliance,phase-1,phase-2",
                "Epic Name": "Security & Fraud Prevention",
                "Story Points": 110
            },
            {
                "Summary": "Loan & Credit Services",
                "Issue Type": "Epic",
                "Description": "Digital loan application and management.",
                "Priority": "Medium",
                "Labels": "loans,lending,credit,phase-4",
                "Epic Name": "Loan & Credit Services",
                "Story Points": 130
            },
            {
                "Summary": "Investment & Wealth Management",
                "Issue Type": "Epic",
                "Description": "Investment portfolio management and trading.",
                "Priority": "Low",
                "Labels": "investments,wealth,trading,phase-4",
                "Epic Name": "Investment & Wealth Management",
                "Story Points": 140
            },
            {
                "Summary": "Customer Support & Service",
                "Issue Type": "Epic",
                "Description": "Enable seamless customer service interactions.",
                "Priority": "High",
                "Labels": "support,customer-service,phase-3",
                "Epic Name": "Customer Support & Service",
                "Story Points": 70
            },
            {
                "Summary": "Notifications & Alerts",
                "Issue Type": "Epic",
                "Description": "Real-time communication system for alerts and notifications.",
                "Priority": "Medium",
                "Labels": "notifications,alerts,communication,phase-2",
                "Epic Name": "Notifications & Alerts",
                "Story Points": 60
            },
            {
                "Summary": "Regulatory Compliance & Reporting",
                "Issue Type": "Epic",
                "Description": "Ensure compliance with banking regulations.",
                "Priority": "Critical",
                "Labels": "compliance,regulatory,kyc,aml,audit,sox,gdpr,phase-1",
                "Epic Name": "Regulatory Compliance & Reporting",
                "Story Points": 100
            }
        ]
        return epics
    
    def generate_stories(self) -> List[Dict]:
        """Generate User Story issues"""
        stories = [
            # Epic 1: Customer Onboarding
            {
                "Summary": "User Registration",
                "Issue Type": "Story",
                "Description": "As a new customer, I want to register for online banking.",
                "Epic Link": "EPIC-1",
                "Priority": "High",
                "Labels": "registration,onboarding,kyc,phase-1",
                "Story Points": 8,
                "Acceptance Criteria": self._get_plain_registration()
            },
            {
                "Summary": "KYC Document Upload",
                "Issue Type": "Story",
                "Description": "As a new customer, I want to upload identity documents for KYC verification.",
                "Epic Link": "EPIC-1",
                "Priority": "Critical",
                "Labels": "kyc,compliance,document-upload,phase-1",
                "Story Points": 13,
                "Acceptance Criteria": self._get_plain_kyc()
            },
            # Epic 2: Account Management
            {
                "Summary": "View Account Balance",
                "Issue Type": "Story",
                "Description": "As a customer, I want to view my account balance.",
                "Epic Link": "EPIC-2",
                "Priority": "High",
                "Labels": "account-management,balance,core-banking,phase-1",
                "Story Points": 5,
                "Acceptance Criteria": self._get_plain_balance()
            },
            # Epic 3: Transfers
            {
                "Summary": "Internal Fund Transfer",
                "Issue Type": "Story",
                "Description": "As a customer, I want to transfer money between my own accounts.",
                "Epic Link": "EPIC-3",
                "Priority": "Critical",
                "Labels": "transfers,payments,core-banking,security,phase-2",
                "Story Points": 13,
                "Acceptance Criteria": self._get_plain_transfer()
            }
        ]
        return stories
    
    def generate_tasks(self, story_key: str) -> List[Dict]:
        """Generate Task issues for a story"""
        tasks = [
            {
                "Summary": f"Design API endpoint for {story_key}",
                "Issue Type": "Task",
                "Description": "Design RESTful API endpoint with request/response schemas",
                "Parent": story_key,
                "Priority": "High",
                "Labels": "api,design,backend",
                "Story Points": 2
            },
            {
                "Summary": f"Implement backend service for {story_key}",
                "Issue Type": "Task",
                "Description": "Implement business logic and data access layer",
                "Parent": story_key,
                "Priority": "High",
                "Labels": "backend,implementation",
                "Story Points": 5
            },
            {
                "Summary": f"Create UI components for {story_key}",
                "Issue Type": "Task",
                "Description": "Design and implement frontend components",
                "Parent": story_key,
                "Priority": "Medium",
                "Labels": "frontend,ui,react",
                "Story Points": 3
            }
        ]
        return tasks
    
    def generate_xray_tests(self, story_key: str) -> List[Dict]:
        """Generate XRay test cases for a story"""
        tests = [
            {
                "Summary": f"Test: {story_key} - Happy Path",
                "Issue Type": "Test",
                "Test Type": "Manual",
                "Description": f"Verify successful completion of {story_key}",
                "Requirement": story_key,
                "Priority": "High",
                "Labels": "automated,positive",
                "Test Steps": self._get_test_steps(story_key)
            },
            {
                "Summary": f"Test: {story_key} - Error Cases",
                "Issue Type": "Test",
                "Test Type": "Manual",
                "Description": f"Verify error handling for {story_key}",
                "Requirement": story_key,
                "Priority": "High",
                "Labels": "automated,negative",
                "Test Steps": self._get_test_error_steps(story_key)
            }
        ]
        return tests
    
    def _get_plain_registration(self) -> str:
        return """Prerequisites:
- User has valid email address and personal information
- Registration page is accessible

Scenario: New customer registers successfully
1. New user visits registration page
2. User provides valid personal information (name, email, phone, DOB)
3. User creates strong password meeting security requirements
4. User submits registration form
5. System validates all information
6. Account is created with pending status
7. Verification email is sent to user's email address
8. User receives confirmation message"""
    
    def _get_plain_kyc(self) -> str:
        return """Prerequisites:
- Customer has registered account
- Customer has valid government-issued ID
- Customer has proof of address document

Scenario: Upload identity documents
1. Customer logs into account with pending status
2. Customer navigates to KYC document upload section
3. Customer selects and uploads government ID (PDF/JPG/PNG, max 5MB)
4. Customer selects and uploads proof of address
5. Documents are encrypted with AES-256 during upload
6. System stores documents securely
7. Compliance team is notified for review
8. Customer receives upload confirmation with reference number"""
    
    def _get_plain_balance(self) -> str:
        return """Prerequisites:
- Customer is logged into their account
- Customer has at least one active bank account

Scenario: Customer views balance
1. Customer is on the dashboard or navigates to accounts page
2. System displays all linked accounts (checking, savings, credit cards)
3. Each account shows account type and last 4 digits
4. Each account displays current balance prominently
5. Each account shows available balance vs pending balance
6. Last transaction date is visible for each account
7. Customer can click on account to view more details"""
    
    def _get_plain_transfer(self) -> str:
        return """Prerequisites:
- Customer has at least two active accounts
- Source account has sufficient balance
- Customer is logged in with MFA

Scenario: Transfer between own accounts
1. Customer navigates to Transfer Funds page
2. Customer selects source account from dropdown
3. Customer selects destination account (only own accounts shown)
4. Customer enters transfer amount
5. Customer optionally adds description/memo
6. System validates sufficient balance exists
7. Customer reviews transfer preview
8. Customer confirms transfer with MFA verification
9. Transfer processes immediately
10. Balances update in real-time
11. Confirmation message is displayed
12. Confirmation email and SMS are sent"""
    
    def _get_test_steps(self, story_key: str) -> str:
        return f"""Tags: {story_key}, smoke, positive, automated

Test: Verify successful execution of {story_key}

Prerequisites:
- System is operational and all services are available
- Test data is prepared
- User has valid credentials

Test Steps:
1. Log into the system with test credentials
2. Navigate to the feature under test
3. Perform valid user action as per story requirements
4. Verify expected result is achieved
5. Verify all success indicators are displayed
6. Verify data is persisted correctly
7. Log out successfully"""
    
    def _get_test_error_steps(self, story_key: str) -> str:
        return f"""Tags: {story_key}, negative, error-handling, automated

Test: Verify error handling for {story_key}

Prerequisites:
- System is operational
- Test data is prepared
- User has valid credentials

Test Steps:
1. Log into the system with test credentials
2. Navigate to the feature under test
3. Perform invalid user action (e.g., invalid input, missing required fields)
4. Verify appropriate error message is displayed
5. Verify error message is clear and helpful
6. Verify system handles error gracefully without crash
7. Verify no data corruption occurs
8. Verify user can recover from error state"""
    
    def write_csv(self, filename: str, data: List[Dict], fieldnames: List[str]):
        """Write data to CSV file"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"✓ Generated: {filepath} ({len(data)} issues)")
    
    def generate_all(self):
        """Generate all CSV files"""
        print("\n" + "="*60)
        print("JIRA Banking Project CSV Generator")
        print("="*60 + "\n")
        
        # Generate Epics
        epics = self.generate_epics()
        epic_fields = ["Summary", "Issue Type", "Description", "Priority", 
                       "Labels", "Epic Name", "Story Points"]
        self.write_csv("epics.csv", epics, epic_fields)
        
        # Generate Stories
        stories = self.generate_stories()
        story_fields = ["Summary", "Issue Type", "Description", "Epic Link",
                       "Priority", "Labels", "Story Points", "Acceptance Criteria"]
        self.write_csv("stories.csv", stories, story_fields)
        
        # Generate Tasks for first story
        tasks = self.generate_tasks("STORY-1")
        task_fields = ["Summary", "Issue Type", "Description", "Parent",
                      "Priority", "Labels", "Story Points"]
        self.write_csv("tasks_sample.csv", tasks, task_fields)
        
        # Generate XRay Tests for first story
        tests = self.generate_xray_tests("STORY-1")
        test_fields = ["Summary", "Issue Type", "Test Type", "Description",
                      "Requirement", "Priority", "Labels", "Test Steps"]
        self.write_csv("xray_tests_sample.csv", tests, test_fields)
        
        print("\n" + "="*60)
        print("Summary:")
        print(f"  • {len(epics)} Epics")
        print(f"  • {len(stories)} User Stories")
        print(f"  • {len(tasks)} Tasks (sample)")
        print(f"  • {len(tests)} Test Cases (sample)")
        print("="*60)
        print(f"\nFiles generated in: {os.path.abspath(self.output_dir)}")
        print("\nNext Steps:")
        print("  1. Review generated CSV files")
        print("  2. Customize as needed")
        print("  3. Import to JIRA via:")
        print("     Settings > System > External System Import > CSV")
        print("="*60 + "\n")


def main():
    """Main entry point"""
    generator = JIRAIssueGenerator(output_dir="./csv")
    generator.generate_all()


if __name__ == "__main__":
    main()
