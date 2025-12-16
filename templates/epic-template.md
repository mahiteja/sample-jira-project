# Epic Template

## Epic Information
**Epic Name:** [Name of the Epic]  
**Epic ID:** EPIC-[Number]  
**Priority:** [High/Medium/Low]  
**Target Release:** [Phase/Version]  
**Story Points Estimate:** [Total Points]

## Description
[Brief description of what this epic aims to achieve]

## Business Value
[Why is this epic important? What value does it deliver?]

## User Personas
- [Primary user type 1]
- [Primary user type 2]

## Success Criteria
1. [Measurable success criterion 1]
2. [Measurable success criterion 2]
3. [Measurable success criterion 3]

## User Stories (Summary)
- [ ] Story 1: [Brief description]
- [ ] Story 2: [Brief description]
- [ ] Story 3: [Brief description]

## Dependencies
- [Dependent Epic/Story 1]
- [Dependent Epic/Story 2]

## Compliance Requirements
- [ ] KYC/AML: [Yes/No] - [Details]
- [ ] PCI-DSS: [Yes/No] - [Details]
- [ ] GDPR: [Yes/No] - [Details]
- [ ] SOX: [Yes/No] - [Details]

## Security Considerations
- [Security requirement 1]
- [Security requirement 2]

## Labels
`[label1]`, `[label2]`, `[label3]`

## Timeline
- **Start Date:** [Date]
- **Target Completion:** [Date]
- **Duration:** [Weeks/Months]

---

## Example: Customer Onboarding Epic

**Epic Name:** Customer Onboarding & Authentication  
**Epic ID:** EPIC-1  
**Priority:** High  
**Target Release:** Phase 1 - MVP  
**Story Points Estimate:** 100

### Description
Enable secure customer registration and identity verification process compliant with banking regulations (KYC/AML). Provide multiple authentication methods including traditional password, biometric, and multi-factor authentication.

### Business Value
- Enables new customer acquisition through digital channels
- Reduces operational costs by 40% (vs. branch onboarding)
- Improves time-to-activation from 3 days to 15 minutes
- Ensures regulatory compliance from day one

### User Personas
- New Banking Customer (primary)
- Existing Customer adding digital access
- Bank Compliance Officer (secondary)

### Success Criteria
1. 80% of customers complete registration within 10 minutes
2. 95% KYC verification success rate
3. Zero security breaches during authentication
4. 100% compliance with banking regulations

### User Stories (Summary)
- [x] Story 1: User Registration with email/phone verification
- [x] Story 2: KYC document upload and validation
- [x] Story 3: Multi-factor authentication setup
- [x] Story 4: Biometric authentication enrollment
- [x] Story 5: Password recovery workflow
- [x] Story 6: Session management and security

### Dependencies
- Identity verification service integration
- Document OCR service
- SMS/Email gateway
- Biometric SDK integration

### Compliance Requirements
- [x] KYC/AML: Yes - Full identity verification required per BSA regulations
- [x] PCI-DSS: Yes - Secure handling of authentication credentials
- [x] GDPR: Yes - Consent management and data privacy
- [ ] SOX: No - Not applicable for this epic

### Security Considerations
- Password must meet complexity requirements (12+ chars, special chars)
- MFA mandatory for accounts with transaction capabilities
- Rate limiting on registration attempts (max 5 per hour per IP)
- Document uploads encrypted in transit and at rest
- Session timeout after 15 minutes of inactivity
- Biometric data stored in secure enclave only

### Labels
`onboarding`, `authentication`, `security`, `kyc`, `compliance`, `phase-1`, `mvp`

### Timeline
- **Start Date:** January 1, 2026
- **Target Completion:** February 28, 2026
- **Duration:** 8 weeks
