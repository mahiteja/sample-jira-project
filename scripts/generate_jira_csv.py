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
                "Acceptance Criteria": self._get_gherkin_registration()
            },
            {
                "Summary": "KYC Document Upload",
                "Issue Type": "Story",
                "Description": "As a new customer, I want to upload identity documents for KYC.",
                "Epic Link": "EPIC-1",
                "Priority": "Critical",
                "Labels": "kyc,compliance,document-upload,phase-1",
                "Story Points": 13,
                "Acceptance Criteria": self._get_gherkin_kyc()
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
                "Acceptance Criteria": self._get_gherkin_balance()
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
                "Acceptance Criteria": self._get_gherkin_transfer()
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
                "Test Type": "Cucumber",
                "Description": f"Verify successful completion of {story_key}",
                "Requirement": story_key,
                "Priority": "High",
                "Labels": "automated,bdd,positive",
                "Gherkin Definition": self._get_test_gherkin(story_key)
            },
            {
                "Summary": f"Test: {story_key} - Error Cases",
                "Issue Type": "Test",
                "Test Type": "Cucumber",
                "Description": f"Verify error handling for {story_key}",
                "Requirement": story_key,
                "Priority": "High",
                "Labels": "automated,bdd,negative",
                "Gherkin Definition": self._get_test_error_gherkin(story_key)
            }
        ]
        return tests
    
    def _get_gherkin_registration(self) -> str:
        return """Feature: User Registration
Scenario: New customer registers successfully
  Given a new user visits registration page
  When they provide valid information
  Then account should be created
  And verification email sent"""
    
    def _get_gherkin_kyc(self) -> str:
        return """Feature: KYC Document Upload
Scenario: Upload identity documents
  Given customer has registered
  When they upload valid government ID
  Then documents encrypted and stored
  And compliance team notified"""
    
    def _get_gherkin_balance(self) -> str:
        return """Feature: View Account Balance
Scenario: Customer views balance
  Given customer logged in
  When they navigate to accounts
  Then all accounts displayed with balances"""
    
    def _get_gherkin_transfer(self) -> str:
        return """Feature: Internal Fund Transfer
Scenario: Transfer between own accounts
  Given customer has multiple accounts
  When they transfer funds with MFA
  Then transfer completes successfully
  And balances updated immediately"""
    
    def _get_test_gherkin(self, story_key: str) -> str:
        return f"""@{story_key} @smoke @positive
Feature: Test {story_key}
Scenario: Successful execution
  Given system is operational
  When user performs valid action
  Then expected result achieved"""
    
    def _get_test_error_gherkin(self, story_key: str) -> str:
        return f"""@{story_key} @negative
Feature: Test {story_key} Errors
Scenario: Error handling
  Given system is operational
  When user performs invalid action
  Then appropriate error displayed"""
    
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
                      "Requirement", "Priority", "Labels", "Gherkin Definition"]
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
