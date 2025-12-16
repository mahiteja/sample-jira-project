# Confluence-Compatible Documentation Format Research
## Banking JIRA Project Documentation Guide

**Date:** December 15, 2025  
**Project:** Sample JIRA Banking Application  
**Purpose:** Comprehensive research on Confluence formats for creating banking project documentation

---

## EXECUTIVE SUMMARY

### Recommended Approach for Your Banking Project

**Best Format:** Use the **Confluence Rich Text Editor** with strategic HTML/Storage Format where needed
- Confluence does NOT natively use Markdown (it converts it on paste but cannot be re-edited)
- **Primary format:** Create content directly in Confluence's visual editor
- **Alternative for bulk creation:** Write in HTML or Confluence Storage Format (XHTML-based)
- **For copy-paste:** Your existing Markdown files can be pasted and will be auto-converted (one-time only)

**Document Structure Recommendation:** **Multiple Pages with Hierarchy** (NOT a single document)
- Parent page: "Digital Banking Application - Product Documentation"
- 10 child pages (one per EPIC)
- Each EPIC page contains its user stories, acceptance criteria, and roadmap information
- Use Page Tree macro for navigation
- Use Table of Contents macro within each page

---

## 1. CONFLUENCE STORAGE FORMAT

### What Format Does Confluence Use?

**Answer: Confluence Storage Format (XHTML-based XML)**

Confluence stores all content in an XHTML-based storage format, NOT in Markdown. Key characteristics:

```xml
<!-- Example Confluence Storage Format -->
<h1>Banking Application Epic</h1>
<p>This is a <strong>bold</strong> paragraph with <em>emphasis</em>.</p>

<table>
  <tbody>
    <tr>
      <th>Epic Name</th>
      <th>Story Points</th>
    </tr>
    <tr>
      <td>Customer Onboarding</td>
      <td>100</td>
    </tr>
  </tbody>
</table>

<!-- Confluence Macro Example -->
<ac:structured-macro ac:name="jira" ac:schema-version="1">
  <ac:parameter ac:name="server">JIRA</ac:parameter>
  <ac:parameter ac:name="jqlQuery">project = BANK AND type = Epic</ac:parameter>
</ac:structured-macro>
```

**Key Elements:**
- Standard XHTML tags: `<h1>`, `<p>`, `<strong>`, `<em>`, `<table>`, `<ul>`, `<ol>`
- Confluence-specific tags with `ac:` prefix for macros and special features
- Resource identifiers with `ri:` prefix for links, images, attachments

### Supported Formatting

| Element | Confluence Storage Format | Notes |
|---------|---------------------------|-------|
| **Headings** | `<h1>`, `<h2>`, `<h3>`, etc. | H1-H6 supported |
| **Bold** | `<strong>text</strong>` | Also `<b>` |
| **Italic** | `<em>text</em>` | Also `<i>` |
| **Tables** | `<table><tbody><tr><th>`, `<td>` | Full HTML table support |
| **Lists** | `<ul><li>`, `<ol><li>` | Unordered and ordered |
| **Task Lists** | `<ac:task-list><ac:task>` | Confluence-specific |
| **Code Blocks** | `<ac:structured-macro ac:name="code">` | Use Code Block macro |
| **Links** | `<ac:link><ri:page ri:content-title="Page"/>` | Internal pages |
| **Images** | `<ac:image><ri:attachment ri:filename=""/>` | Attached images |
| **Layouts** | `<ac:layout><ac:layout-section>` | Page columns/sections |

---

## 2. CONFLUENCE + JIRA INTEGRATION

### Embedding JIRA Content in Confluence

Confluence provides powerful macros to embed live JIRA data:

#### **JIRA Issues Macro** (Most Important for Your Project)

Displays JIRA issues dynamically in Confluence pages.

**Use Cases for Banking Project:**
- Display all epics from your BANK project
- Show user stories for a specific epic
- Create dynamic roadmap views
- Display issue counts and progress

**Implementation Examples:**

```wiki
{jiraissues:url=https://your-jira.atlassian.net/issues/?jql=project=BANK AND type=Epic}

{jiraissues:url=https://your-jira.atlassian.net/issues/?jql=project=BANK AND "Epic Link"="BANK-1"}

{jiraissues:url=https://your-jira.atlassian.net/issues/?jql=project=BANK AND labels=phase-1|count=true}
```

**Key Parameters:**
- `url`: JIRA filter URL or JQL query
- `columns`: Customize displayed columns (e.g., `key;summary;assignee;status;priority`)
- `count`: Set to `true` to show only issue count
- `renderMode`: `dynamic` for interactive table, `static` for basic display
- `title`: Custom header text
- `height`: Height in pixels (for dynamic mode)

**JQL Examples for Your Banking Project:**

```jql
# All Epics
project = BANK AND type = Epic

# Phase 1 Stories
project = BANK AND type = Story AND labels = phase-1

# User Stories for Customer Onboarding Epic
project = BANK AND "Epic Link" = "BANK-1"

# Critical Security Issues
project = BANK AND priority = Critical AND labels = security

# Compliance-tagged Issues
project = BANK AND (labels = KYC OR labels = AML OR labels = PCI-DSS)
```

#### **Roadmap Planner Macro**

Creates visual timeline/roadmap views directly in Confluence.

```wiki
{roadmap-planner:baseurl=https://your-jira.atlassian.net|project=BANK}
```

**Features:**
- Visual timeline with start/end dates
- Drag-and-drop interface
- Filter by epic, release, or custom field
- Shows dependencies

#### **JIRA Chart Macro**

Display charts and graphs from JIRA.

```wiki
{jirachart:type=pie|jql=project=BANK AND type=Epic|
statType=statuses}
```

**Chart Types:**
- Pie charts (status distribution)
- Bar/column charts
- Line charts (trends)
- Created vs Resolved

### Dynamic vs Static Content

| Content Type | Dynamic | Static | Recommendation |
|-------------|---------|--------|----------------|
| **JIRA Issue Lists** | Updates automatically | Fixed snapshot | **Dynamic** - Always current |
| **Issue Counts** | Live count | Fixed number | **Dynamic** - For dashboards |
| **Roadmap** | Real-time updates | Screenshot/image | **Dynamic** - Shows progress |
| **Acceptance Criteria** | Pulled from JIRA | Copied to Confluence | **Static** - Better formatting |
| **Epic Descriptions** | From JIRA | Written in Confluence | **Static** - Rich formatting |

**Best Practice for Banking Project:**
- Use **dynamic JIRA macros** for: Issue tracking, status updates, roadmap views
- Use **static Confluence content** for: Detailed requirements, architecture diagrams, compliance documentation

---

## 3. DOCUMENT STRUCTURE BEST PRACTICES

### Recommended Page Hierarchy for Banking Project

```
📄 Digital Banking Application (Root Page)
   ├── 📄 Project Overview & Roadmap
   │   ├── {jiraissues} All Epics
   │   ├── {roadmap-planner} Timeline
   │   └── Phased Delivery Plan
   │
   ├── 📁 Phase 1: Foundation (Months 1-2)
   │   ├── 📄 EPIC 1: Customer Onboarding & Authentication
   │   ├── 📄 EPIC 5: Security & Fraud Prevention
   │   ├── 📄 EPIC 2: Account Management (View Only)
   │   └── 📄 EPIC 10: Regulatory Compliance (Basic)
   │
   ├── 📁 Phase 2: Core Banking (Months 3-4)
   │   ├── 📄 EPIC 3: Fund Transfers & Payments
   │   └── 📄 EPIC 9: Notifications & Alerts
   │
   ├── 📁 Phase 3: Enhanced Services (Months 5-6)
   │   ├── 📄 EPIC 4: Card Management
   │   ├── 📄 EPIC 8: Customer Support
   │   └── 📄 EPIC 3: External Transfers (Extended)
   │
   ├── 📁 Phase 4: Advanced Features (Months 7-8)
   │   ├── 📄 EPIC 6: Loan Services
   │   └── 📄 EPIC 7: Investment Services
   │
   ├── 📁 Compliance & Security
   │   ├── 📄 KYC/AML Requirements
   │   ├── 📄 PCI-DSS Compliance
   │   ├── 📄 GDPR Data Privacy
   │   └── 📄 SOX Audit Requirements
   │
   └── 📁 Technical Architecture
       ├── 📄 System Design
       ├── 📄 Integration Points
       └── 📄 Security Architecture
```

### Page Structure for Each EPIC

Use this template structure for each of your 10 EPICs:

```confluence
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EPIC: Customer Onboarding & Authentication
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{toc:minLevel=2|maxLevel=3}

## Epic Overview

**Epic ID:** BANK-1
**Story Points:** 100 SP
**Priority:** High
**Target Phase:** Phase 1 (Months 1-2)
**Status:** {jiraissues:url=.../BANK-1|count=true}

### Description
Enable secure customer registration and identity verification...

### Business Value
- Onboard 10,000 customers in first 3 months
- 95% KYC verification success rate
- Reduce onboarding time from 3 days to 15 minutes

### Success Criteria
✅ 100% KYC compliance
✅ < 2-minute registration time
✅ Multi-factor authentication enabled

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## User Stories
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{jiraissues:jqlQuery=project=BANK AND "Epic Link"=BANK-1|
columns=key;summary;status;story-points;assignee}

### Featured Stories

#### BANK-101: User Registration with Email/Phone

**As a** new customer
**I want to** register using my email or phone number
**So that** I can create an account quickly and securely

**Acceptance Criteria:**
```gherkin
Feature: User Registration
  As a new customer
  I want to register for online banking
  So that I can access banking services

  Scenario: Successful registration with email
    Given I am on the registration page
    When I enter valid email "user@example.com"
    And I enter a strong password
    And I accept terms and conditions
    Then I should receive a verification email
    And my account should be created with "Pending" status

  Scenario: Password strength validation
    Given I am on the registration page
    When I enter password "weak"
    Then I should see error "Password must be at least 12 characters"
    And I should see "Must include uppercase, lowercase, number, special char"
```

**Security Requirements:**
- ✅ Password hashing with bcrypt (cost factor 12)
- ✅ Email verification required
- ✅ Rate limiting: 3 attempts per hour per IP
- ✅ Audit logging of all registration attempts

**Compliance Tags:** 
🏷️ KYC | 🏷️ GDPR | 🏷️ Security | 🏷️ Phase-1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Compliance Requirements
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Requirement | Description | Status |
|------------|-------------|--------|
| **KYC** | Identity verification within 24 hours | ✅ Covered |
| **AML** | Customer screening against watchlists | ✅ Covered |
| **GDPR** | Consent collection, data encryption | ✅ Covered |
| **PCI-DSS** | N/A for this epic | N/A |
| **SOX** | Audit trail of all identity changes | ✅ Covered |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Technical Architecture
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Components
- Authentication Service
- Identity Verification Service (3rd party: Onfido/Jumio)
- KYC Service
- Notification Service

### APIs
- POST /api/v1/auth/register
- POST /api/v1/auth/verify-email
- POST /api/v1/kyc/submit-documents

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Dependencies
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Depends on: Infrastructure Setup
- Blocks: EPIC 2 (Account Management)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Timeline & Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Start Date:** January 1, 2026
**Target Completion:** February 28, 2026
**Duration:** 8 weeks

{roadmap-planner:epic=BANK-1}
```

### Navigation Best Practices

**Use these macros for navigation:**

1. **Page Tree Macro** (for space navigation)
```wiki
{pagetree:root=@home|sort=position|searchBox=true|expandCollapseAll=true}
```

2. **Table of Contents Macro** (for within-page navigation)
```wiki
{toc:printable=true|style=disc|minLevel=2|maxLevel=3}
```

3. **Children Display Macro** (show child pages)
```wiki
{children:all=true|sort=title|excerpt=true}
```

4. **Breadcrumbs** - Automatic in Confluence header

---

## 4. IMPORT/EXPORT OPTIONS

### Can You Import Markdown to Confluence?

**Short Answer:** Yes, but with **significant limitations**.

#### Markdown Import Capabilities

**Method 1: Copy-Paste with Auto-Conversion** ✅ LIMITED
- Paste Markdown directly into Confluence editor
- Confluence auto-converts to rich text format **ONE-TIME ONLY**
- ⚠️ **Cannot edit as Markdown after conversion**
- ⚠️ **Loses some formatting** (complex tables, advanced features)

**What Works:**
- ✅ Headings (#, ##, ###)
- ✅ Bold (**text**) and Italic (*text*)
- ✅ Simple lists (-, *, 1.)
- ✅ Simple tables (| header | header |)
- ✅ Links [text](url)
- ✅ Code blocks (```)

**What Doesn't Work:**
- ❌ Nested tables
- ❌ HTML in Markdown
- ❌ Some complex list formatting
- ❌ Definition lists
- ❌ Footnotes
- ❌ Task lists (- [ ])

**Method 2: Insert Markup** ✅ BETTER
- In Confluence editor: **Insert → Markup**
- Select "Markdown"
- Paste your Markdown
- Preview and insert
- Still converts to Confluence format (cannot re-edit)

**Method 3: Third-Party Apps** 💰
- [Markdown Macro for Confluence](https://marketplace.atlassian.com/apps/1219621/markdown-for-confluence)
- Allows storing content as Markdown
- Renders as HTML on page display

#### HTML Import Capabilities

**HTML Import is BETTER than Markdown:**

✅ **Native Support** - Confluence storage format is XHTML-based
✅ **Better Conversion** - Most HTML converts cleanly
✅ **More Control** - Direct mapping to Confluence format

**How to Import HTML:**

**Method 1: Paste HTML**
```html
<h1>Epic: Customer Onboarding</h1>
<p>Description with <strong>bold</strong> and <em>italic</em>.</p>
<table>
  <tr><th>Column 1</th><th>Column 2</th></tr>
  <tr><td>Data 1</td><td>Data 2</td></tr>
</table>
```
- Paste into editor
- Auto-converts to Confluence

**Method 2: Insert HTML Macro** (if enabled)
```wiki
{html}
<div class="custom-style">
  <h2>Custom HTML Content</h2>
</div>
{html}
```
⚠️ Note: HTML macro often disabled for security reasons

**Method 3: Storage Format Direct Edit** (Advanced)
- Edit page source
- Paste Confluence Storage Format (XHTML)
- Most accurate conversion

#### Word Document Import

✅ **Fully Supported** via Office Connector

**Process:**
1. In Confluence: **Create** → **Import Word Document**
2. Upload .docx file
3. Confluence converts to pages automatically
4. Preserves:
   - Headings → Confluence headings
   - Tables → Confluence tables
   - Images → Embedded images
   - Styles → Confluence formatting

**Best for:**
- Large documents
- Existing Word-based documentation
- Complex formatting

**Limitations:**
- Custom Word styles may not convert perfectly
- Macros/VBA lost
- Some complex tables may break

#### Copy-Paste Considerations

**From Your Current Markdown Files to Confluence:**

**Recommended Process:**

1. **Quick Preview:** Open README.md, copy content, paste into Confluence editor
2. **Review Conversion:** Check tables, code blocks, lists
3. **Fix Formatting:** Manually adjust what didn't convert well
4. **Add Macros:** Insert JIRA Issues macros, Table of Contents, etc.
5. **Enhance:** Add page layouts, panels (Info, Warning, Tip)

**Alternative Process (Better for Bulk):**

1. **Convert Markdown to HTML** (using Pandoc or similar)
   ```bash
   pandoc README.md -f markdown -t html -o README.html
   ```
2. **Paste HTML** into Confluence (better conversion)
3. **Add Confluence-specific features** (macros, layouts)

---

## 5. BANKING PROJECT DOCUMENTATION

### Best Format for Presenting 10 EPICs with User Stories

**Recommended Structure: Hybrid Approach**

#### Option A: Multiple Pages (RECOMMENDED) ⭐

**Advantages:**
- ✅ Better navigation (page tree)
- ✅ Easier to maintain
- ✅ Better for collaboration (page-level permissions)
- ✅ Faster page loads
- ✅ Individual page analytics
- ✅ Can be organized by phase/sprint

**Structure:**
```
Space: Banking Application

Pages:
├── 🏠 Overview Dashboard
│   ├── {jiraissues} All 10 Epics with counts
│   ├── {roadmap-planner} Full timeline
│   └── Phase breakdown
│
├── 📁 EPIC 1: Customer Onboarding (separate page)
├── 📁 EPIC 2: Account Management (separate page)
├── 📁 EPIC 3: Fund Transfers (separate page)
├── 📁 EPIC 4: Card Management (separate page)
├── 📁 EPIC 5: Security & Fraud (separate page)
├── 📁 EPIC 6: Loan Services (separate page)
├── 📁 EPIC 7: Investment Services (separate page)
├── 📁 EPIC 8: Customer Support (separate page)
├── 📁 EPIC 9: Notifications (separate page)
└── 📁 EPIC 10: Compliance (separate page)
```

**Each EPIC page includes:**
- Epic overview
- {jiraissues} macro showing all stories for that epic
- 3-5 detailed story examples with Gherkin acceptance criteria
- Compliance requirements table
- Technical architecture notes

#### Option B: Single Long Document with Anchors

**Advantages:**
- ✅ Everything in one place
- ✅ Easy to export as PDF
- ✅ Good for printing

**Disadvantages:**
- ❌ Very long page (slow loading)
- ❌ Difficult to navigate
- ❌ Hard to maintain
- ❌ Version control issues

**Only use for:** Final deliverable PDF exports

### How to Structure Roadmap Timelines

**Method 1: Roadmap Planner Macro** (BEST for Interactive)

```wiki
{roadmap-planner:
  baseurl=https://jira.company.com|
  project=BANK|
  epicLabel=phase-1
}
```

**Features:**
- Visual Gantt-chart style
- Drag-and-drop
- Shows dependencies
- Real-time updates from JIRA

**Method 2: Static Timeline Table**

| Phase | Timeline | Epics | Deliverables |
|-------|----------|-------|-------------|
| **Phase 1: Foundation** | Jan-Feb 2026 | EPIC 1, 2, 5, 10 | User registration, KYC, basic security |
| **Phase 2: Core Banking** | Mar-Apr 2026 | EPIC 3, 9 | Internal transfers, notifications |
| **Phase 3: Enhanced** | May-Jun 2026 | EPIC 4, 8 | Cards, customer support |
| **Phase 4: Advanced** | Jul-Aug 2026 | EPIC 6, 7 | Loans, investments |
| **Phase 5: Optimization** | Sep-Oct 2026 | All | Performance, advanced fraud |

**Method 3: Status Macro with Dates**

```wiki
{status:title=Phase 1|colour=Green|subtle=false} Jan-Feb 2026
{status:title=Phase 2|colour=Yellow|subtle=false} Mar-Apr 2026
{status:title=Phase 3|colour=Blue|subtle=false} May-Jun 2026
```

### Tables for Acceptance Criteria vs Macros

**Recommendation: USE BOTH (Strategically)**

#### When to Use Tables for Acceptance Criteria

✅ **Use Static Tables When:**
- Detailed Gherkin scenarios (better formatting)
- Need to include screenshots/annotations
- Want to highlight specific criteria with colors
- Creating documentation templates

**Example:**
```confluence
| Scenario | Given | When | Then | Status |
|----------|-------|------|------|--------|
| Valid login | User has account | Enters correct credentials | Redirected to dashboard | ✅ Done |
| Invalid login | User has account | Enters wrong password | Error message shown | ✅ Done |
| Locked account | Account locked | Any credentials | Account locked message | 🔄 In Progress |
```

#### When to Use Macros

✅ **Use JIRA Macros When:**
- Want live updates from JIRA
- Displaying issue status/progress
- Showing multiple stories at once
- Tracking completion

**Example:**
```wiki
{jiraissues:
  jqlQuery=project=BANK AND "Epic Link"=BANK-1|
  columns=key;summary;acceptance-criteria;status
}
```

### Formatting Regulatory Compliance Information

**Best Practice: Dedicated Compliance Section**

Use **Panel Macros** for regulatory information:

```wiki
{info:title=KYC Requirement}
All customer accounts must complete identity verification within 24 hours of registration, including:
- Government-issued photo ID
- Proof of address (utility bill < 3 months old)
- Selfie verification
{info}

{warning:title=PCI-DSS Compliance}
Card data must NEVER be stored in plain text. Use:
- Tokenization for card numbers
- Encrypted storage for CVV
- PCI-compliant payment gateway
{warning}

{tip:title=GDPR Right to Erasure}
Users can request account deletion. Must be completed within 30 days and include:
- All personal data removed
- Anonymization of transaction history
- Notification to user upon completion
{tip}
```

**Compliance Requirements Table Template:**

| Regulation | Requirement | Implementation | Verification | Status |
|-----------|-------------|----------------|--------------|--------|
| **KYC (Know Your Customer)** | Identity verification within 24h | Onfido integration, document upload | Manual review + AI verification | ✅ Complete |
| **AML (Anti-Money Laundering)** | Transaction monitoring > $10k | Real-time screening, watchlist checks | Quarterly audit reports | ✅ Complete |
| **PCI-DSS Level 1** | No plain text card storage | Tokenization via Stripe | External QSA audit | 🔄 In Progress |
| **GDPR Article 17** | Right to erasure (30 days) | Automated deletion workflow | Deletion confirmation logs | ✅ Complete |
| **SOX Section 404** | Internal control audit | Audit logging, change tracking | Annual external audit | 📅 Planned |

---

## 6. ANALYSIS OF EXISTING WORKSPACE FILES

### What Can Be Reused from Existing Files

Your workspace contains excellent material that can be directly leveraged:

#### Files Reviewed:

1. **README.md** (355 lines)
   - ✅ **Excellent structure** - Use as basis for Confluence Overview page
   - ✅ **Epic overview** - Copy to individual Epic pages
   - ✅ **Phased roadmap** - Convert to Confluence table/macro
   - ⚠️ **Needs conversion** - Markdown → Confluence format

2. **RESEARCH_SUMMARY.md** (873 lines)
   - ✅ **Comprehensive JIRA best practices** - Reference material
   - ✅ **XRay integration details** - Add to Technical Architecture section
   - ✅ **Acceptance criteria examples** - Use as templates for Confluence
   - ⚠️ **Too detailed for Confluence** - Extract key sections only

3. **DELIVERY_SUMMARY.md** (543 lines)
   - ✅ **Project status** - Use for Overview Dashboard
   - ✅ **Research areas covered** - Good for "About this Documentation" page
   - ⚠️ **Internal document** - May not need in Confluence

4. **QUICK_START.md** (448 lines)
   - ✅ **Import process** - Create "Getting Started" page
   - ✅ **Quick reference** - Add to sidebar or Overview

5. **CSV Files** (epics.csv, stories.csv)
   - ✅ **Import to JIRA first** - Then use JIRA macros in Confluence
   - ❌ **Don't display raw CSV in Confluence** - Use JIRA Issues macro instead

6. **Templates** (epic-template.md, user-story-template.md, xray-test-template.md)
   - ✅ **Convert to Confluence Page Templates**
   - ✅ **Excellent structure** - Maintain in Confluence

### Recommended Migration Strategy

**Step 1: Import CSV to JIRA** (Priority 1)
```
1. Import epics.csv to JIRA
2. Import stories.csv to JIRA
3. Verify parent-child relationships
4. Confirm all fields mapped correctly
```

**Step 2: Create Confluence Space** (Priority 1)
```
1. Create space: "Banking Application"
2. Set up permissions
3. Configure space sidebar
```

**Step 3: Create Overview Dashboard** (Priority 2)
```
Source: README.md (lines 1-100)
Content:
- Project overview
- {jiraissues} showing all 10 epics
- {roadmap-planner} macro
- Phase breakdown table
- Links to child pages
```

**Step 4: Create EPIC Pages** (Priority 2)
```
Source: README.md epic descriptions + templates/epic-template.md
For each of 10 epics:
- Create page from template
- Add epic description from README.md
- Insert {jiraissues} macro for that epic's stories
- Add 3-5 detailed story examples with Gherkin
- Add compliance requirements
```

**Step 5: Create Supporting Pages** (Priority 3)
```
- Getting Started (from QUICK_START.md)
- Technical Architecture
- Compliance & Security (extract from RESEARCH_SUMMARY.md)
- Testing Strategy (XRay information)
```

### What Needs to Be Reformatted

**High Priority Reformatting:**

1. **Markdown Tables → Confluence Tables**
   - Your CSV data displays as nice tables in Markdown
   - Convert to HTML tables or use Confluence table editor

2. **Code Blocks → Code Block Macro**
   ```markdown
   # Current Markdown
   ```gherkin
   Feature: Login
   ```
   
   # Confluence Format
   {code:language=gherkin}
   Feature: Login
   {code}
   ```

3. **Links → Confluence Links**
   ```markdown
   # Current Markdown
   [Link text](url)
   
   # Confluence
   [Link text|url]  or use rich text editor
   ```

4. **Checklists → Task Lists**
   ```markdown
   # Current Markdown
   - [ ] Task 1
   - [x] Task 2
   
   # Confluence Task List macro
   ☐ Task 1
   ☑ Task 2
   ```

**Medium Priority Enhancements:**

1. **Add JIRA Macros**
   - Replace static epic lists with {jiraissues} macros
   - Add roadmap visualizations

2. **Add Panel Macros**
   - Wrap important sections in Info/Warning/Tip panels
   - Makes compliance requirements stand out

3. **Add Table of Contents**
   - Each epic page needs {toc} macro
   - Overview page needs page tree

4. **Add Page Layouts**
   - Use 2-column layouts for comparison sections
   - Use sidebars for navigation

---

## 7. SINGLE DOCUMENT VS MULTIPLE PAGES

### Comparison Matrix

| Criteria | Single Document | Multiple Pages | Winner |
|----------|----------------|----------------|--------|
| **Navigation** | Scrolling, TOC anchors | Page tree, breadcrumbs | 🏆 **Multiple** |
| **Load Time** | Slow (very long page) | Fast (smaller pages) | 🏆 **Multiple** |
| **Maintenance** | Difficult (one big file) | Easy (edit individual pages) | 🏆 **Multiple** |
| **Collaboration** | Page-level locking issues | Multiple people can work simultaneously | 🏆 **Multiple** |
| **Search** | Hard to find specific content | Page titles help SEO | 🏆 **Multiple** |
| **Analytics** | One page view count | Per-page analytics | 🏆 **Multiple** |
| **Permissions** | All-or-nothing | Granular per page/section | 🏆 **Multiple** |
| **Export PDF** | Easy (single export) | Need to export multiple | 🏆 **Single** |
| **Printing** | Easy | Must print each page | 🏆 **Single** |
| **Initial Setup** | Faster (one page) | Slower (multiple pages) | 🏆 **Single** |

### Final Recommendation: MULTIPLE PAGES ⭐

**Use Multiple Pages with PDF Export Option**

**Structure:**
- Multiple pages for daily use (better collaboration)
- Use "Export to PDF" (Confluence feature) for deliverables
- Best of both worlds

**Implementation:**
```
Banking Application Space (Multiple Pages)
↓
Export Space to PDF
↓
Single comprehensive PDF for clients/stakeholders
```

---

## 8. IMPLEMENTATION ROADMAP

### Phase 1: Setup (1 day)

**Tasks:**
1. ✅ Create Confluence Space "Banking Application"
2. ✅ Import CSV files to JIRA (epics.csv, stories.csv)
3. ✅ Configure JIRA-Confluence application link
4. ✅ Test JIRA Issues macro connection

### Phase 2: Core Pages (2-3 days)

**Tasks:**
1. ✅ Create Overview Dashboard page
   - Copy content from README.md
   - Add {jiraissues} macro showing all epics
   - Add roadmap visualization
   - Add phase breakdown table

2. ✅ Create page template for EPICs
   - Based on templates/epic-template.md
   - Include standard sections
   - Save as Confluence template

3. ✅ Create 10 EPIC pages
   - Use template for each
   - Populate with data from README.md
   - Add JIRA macros

### Phase 3: Enhancements (1-2 days)

**Tasks:**
1. ✅ Add navigation
   - Page Tree macro on sidebar
   - Table of Contents on each page
   - Breadcrumbs

2. ✅ Add supporting pages
   - Getting Started
   - Compliance & Security
   - Technical Architecture

3. ✅ Format refinement
   - Add Panel macros for important info
   - Add page layouts where needed
   - Insert Info/Warning/Tip macros

### Phase 4: JIRA Integration (1 day)

**Tasks:**
1. ✅ Configure JIRA Issues macros
   - One macro per EPIC showing its stories
   - Dashboard showing all epics
   - Compliance-tagged issues view

2. ✅ Set up Roadmap Planner
   - Timeline view on Overview
   - Per-phase roadmaps

### Phase 5: Polish & Review (1 day)

**Tasks:**
1. ✅ Review all pages for formatting
2. ✅ Test all JIRA macros
3. ✅ Add images/diagrams as needed
4. ✅ Set page permissions
5. ✅ Test PDF export
6. ✅ Share with stakeholders

**Total Time: 5-7 days**

---

## 9. QUICK REFERENCE: CONFLUENCE SYNTAX

### Confluence Wiki Markup (for manual editing)

```wiki
# Headings
h1. Heading 1
h2. Heading 2
h3. Heading 3

# Text Formatting
*bold*
_italic_
-strikethrough-
+underline+
^superscript^
~subscript~
{{monospace}}

# Lists
* Bullet point
** Nested bullet
# Numbered item
## Nested number

# Links
[Page Title]
[Link Text|Page Title]
[http://external.com]
[Link Text|http://external.com]

# Tables
|| Heading 1 || Heading 2 ||
| Cell 1 | Cell 2 |
| Cell 3 | Cell 4 |

# Code
{code:language=python}
def hello():
    print("Hello")
{code}

# Macros
{toc}
{info}Important information{info}
{warning}Warning text{warning}
{tip}Helpful tip{tip}
{jiraissues:jqlQuery=project=BANK}
```

---

## 10. TOOLS & RESOURCES

### Conversion Tools

1. **Pandoc** (Markdown → HTML → Confluence)
   ```bash
   pandoc input.md -f markdown -t html -o output.html
   ```

2. **Mark** (Markdown → Confluence)
   - GitHub: https://github.com/kovetskiy/mark
   - CLI tool for Markdown to Confluence

3. **Confluence Python API**
   - Programmatic page creation
   - Good for bulk operations

### Helpful Atlassian Marketplace Apps

1. **Markdown Macro for Confluence** ($)
   - Store content as Markdown
   - Render as HTML

2. **Scroll Office** ($$$)
   - Professional PDF exports
   - Better formatting control

3. **Advanced Tables** ($)
   - Enhanced table features
   - Better CSV import

4. **Diagramming Apps**
   - draw.io (free)
   - Gliffy ($$)
   - Lucidchart ($$$)

---

## 11. FINAL RECOMMENDATIONS

### For Your Banking Project Specifically:

✅ **DO THIS:**

1. **Multiple Pages Approach**
   - Create separate page for each EPIC
   - Use phase-based folders for organization
   - Add Overview Dashboard with all JIRA macros

2. **Heavy JIRA Integration**
   - Use {jiraissues} macros extensively
   - Keep Confluence synchronized with JIRA
   - Dynamic content > Static content

3. **Rich Formatting**
   - Use Panel macros (Info, Warning, Tip) for compliance
   - Use Table of Contents macro on long pages
   - Use Status macros for phase indicators

4. **Template Creation**
   - Create Confluence page template based on epic-template.md
   - Ensure consistency across all 10 EPICs

5. **PDF Export**
   - Configure for client deliverables
   - Use Confluence export features

❌ **DON'T DO THIS:**

1. **Don't try to keep Markdown**
   - Confluence is not Markdown-native
   - Embrace Confluence format

2. **Don't create one giant page**
   - Poor performance
   - Difficult to maintain

3. **Don't copy-paste JIRA data statically**
   - Use macros for live data
   - Avoid outdated information

4. **Don't ignore compliance sections**
   - Banking requires clear regulatory documentation
   - Use panels and dedicated pages

---

## APPENDIX A: Conversion Script Outline

### Automate Markdown → Confluence Conversion

```python
# Pseudo-code for conversion script
import markdown
import confluence_api

def convert_epic_to_confluence(epic_md_file, confluence_space):
    # Read Markdown
    with open(epic_md_file) as f:
        md_content = f.read()
    
    # Convert to HTML
    html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Add Confluence macros
    html = add_toc_macro(html)
    html = add_jira_macros(html, epic_id)
    
    # Create page in Confluence
    page = confluence_api.create_page(
        space=confluence_space,
        title=epic_title,
        body=html
    )
    
    return page

# Process all EPICs
for epic in epics:
    convert_epic_to_confluence(epic['markdown'], 'BANK')
```

---

## APPENDIX B: Sample Confluence Storage Format

### Complete EPIC Page Example

```xml
<ac:layout>
  <ac:layout-section ac:type="single">
    <ac:layout-cell>
      <h1>EPIC 1: Customer Onboarding &amp; Authentication</h1>
      
      <ac:structured-macro ac:name="toc" ac:schema-version="1">
        <ac:parameter ac:name="minLevel">2</ac:parameter>
        <ac:parameter ac:name="maxLevel">3</ac:parameter>
      </ac:structured-macro>
      
      <h2>Epic Overview</h2>
      <p><strong>Epic ID:</strong> BANK-1</p>
      <p><strong>Story Points:</strong> 100 SP</p>
      
      <h2>User Stories</h2>
      <ac:structured-macro ac:name="jira" ac:schema-version="1">
        <ac:parameter ac:name="server">JIRA</ac:parameter>
        <ac:parameter ac:name="jqlQuery">project=BANK AND "Epic Link"=BANK-1</ac:parameter>
        <ac:parameter ac:name="columns">key;summary;status;assignee</ac:parameter>
      </ac:structured-macro>
      
      <h3>Featured Story: User Registration</h3>
      <ac:structured-macro ac:name="info" ac:schema-version="1">
        <ac:parameter ac:name="title">User Story</ac:parameter>
        <ac:rich-text-body>
          <p><strong>As a</strong> new customer</p>
          <p><strong>I want to</strong> register using email</p>
          <p><strong>So that</strong> I can access banking services</p>
        </ac:rich-text-body>
      </ac:structured-macro>
      
      <ac:structured-macro ac:name="code" ac:schema-version="1">
        <ac:parameter ac:name="language">gherkin</ac:parameter>
        <ac:plain-text-body><![CDATA[
Feature: User Registration
  Scenario: Successful registration
    Given I am on registration page
    When I enter valid credentials
    Then I should receive verification email
        ]]></ac:plain-text-body>
      </ac:structured-macro>
      
    </ac:layout-cell>
  </ac:layout-section>
</ac:layout>
```

---

## CONCLUSION

### Key Takeaways for Your Banking Project:

1. **Format:** Use Confluence Rich Text Editor, not Markdown
2. **Structure:** Multiple pages organized by EPIC and Phase
3. **Integration:** Heavy use of JIRA Issues macros for dynamic content
4. **Reuse:** Leverage existing README.md and templates
5. **Timeline:** 5-7 days for complete migration
6. **Best Practice:** Create comprehensive navigation with Page Tree and TOC macros

### Next Steps:

1. ✅ Import CSV files to JIRA
2. ✅ Create Confluence space
3. ✅ Start with Overview Dashboard page
4. ✅ Create EPIC pages one by one
5. ✅ Add JIRA macros and formatting
6. ✅ Review and publish

**Your existing workspace is excellent** - it provides a solid foundation. The main work is:
- Converting format (Markdown → Confluence)
- Adding dynamic JIRA integration
- Enhancing with Confluence-specific features (macros, panels, layouts)

---

**Document Version:** 1.0  
**Last Updated:** December 15, 2025  
**Author:** GitHub Copilot (Research Assistant)
