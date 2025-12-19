# Security Summary – OWASP Juice Shop SAST & DAST Lab

## Overview
This project demonstrates a combined SAST and DAST workflow using SonarQube and OWASP ZAP against the OWASP Juice Shop application. The goal is to identify code-level and runtime security risks and explain practical remediation strategies.

---

## Top Vulnerability #1 (SAST)
**Title:** Hard-coded Password Detected  
**Tool:** SonarQube  
**Rule:** typescript:S2068  
**Category:** Authentication

### Why this matters
Hard-coded credentials increase the risk of credential disclosure, reuse, and compromise if source code is exposed.

### Recommended remediation
- Remove secrets from source code
- Use environment variables or a secrets manager
- Rotate any exposed credentials
- Add automated secret scanning to the pipeline

### How to verify the fix
- Re-run SonarQube to confirm the hotspot is resolved
- Validate that no secrets remain in the repository

---

## Top Vulnerability #2 (DAST)
**Title:** Content Security Policy (CSP) Header Not Set  
**Tool:** OWASP ZAP  
**Risk Level:** Medium  
**CWE:** 693

### Why this matters
Without a CSP header, the application is more susceptible to client-side attacks such as Cross-Site Scripting (XSS).

### Recommended remediation
- Implement a strict Content-Security-Policy header
- Restrict script, style, and frame sources
- Test in report-only mode before enforcement

### How to verify the fix
- Re-run OWASP ZAP and confirm the alert is resolved
- Validate headers using browser developer tools

---

## Why SAST and DAST differ
- SAST identifies insecure coding patterns regardless of reachability
- DAST identifies runtime and configuration-based issues
- Using both tools provides broader security coverage


## NIST SP 800-53 Rev. 5 Alignment (Selected Controls)
## NIST SP 800-53 Rev. 5 Alignment (Selected Controls)

This project demonstrates activities that align with selected NIST SP 800-53 Rev. 5 control objectives. The mapping below is illustrative and not intended to represent full system compliance.

- **RA-5 (Vulnerability Monitoring and Scanning):**
  Static and dynamic analysis were used to identify application vulnerabilities.

- **SA-11 (Developer Security Testing):**
  SAST and DAST were performed to evaluate code-level and runtime security risks.

- **SI-2 (Flaw Remediation):**
  Representative findings were paired with remediation and verification guidance.

- **SA-15 (Development Process, Standards, and Tools):**
  Security testing tools were integrated into a repeatable assessment workflow.

- **CM-6 (Configuration Settings):**
  Runtime misconfigurations, including missing security headers, were identified through DAST.
