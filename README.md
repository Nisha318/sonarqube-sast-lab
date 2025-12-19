# SAST & DAST Security Assessment – OWASP Juice Shop

![AppSec](https://img.shields.io/badge/Application%20Security-SAST%20%2B%20DAST-blue)
![SonarQube](https://img.shields.io/badge/SAST-SonarQube-informational)
![OWASP ZAP](https://img.shields.io/badge/DAST-OWASP%20ZAP-informational)
![Docker](https://img.shields.io/badge/Platform-Docker-blue)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)


## Summary
This project demonstrates a practical **application security assessment workflow** by combining **static analysis (SAST)** and **dynamic analysis (DAST)** against the OWASP Juice Shop application.

The focus is not on tool usage alone, but on **how different testing methods surface different risk classes**, how findings are interpreted, and how remediation decisions are made.

---

## What This Demonstrates
- How SAST identifies insecure coding patterns independent of runtime reachability
- How DAST identifies runtime and configuration-level weaknesses
- Why SAST and DAST findings do not fully overlap
- How a security engineer prioritizes and explains remediation

---

## Target System
**OWASP Juice Shop**
- Frontend: Angular / TypeScript  
- Backend: Node.js  
- Deployment: Docker container  

The application is intentionally vulnerable to support security testing and analysis.

---

## Tooling
- **SonarQube (Community Edition)** – Static Application Security Testing
- **OWASP ZAP (Baseline Scan)** – Dynamic Application Security Testing
- **Docker** – Local, repeatable execution

---

## Assessment Approach

### Static Analysis (SAST)
- Analyzed application source code for insecure patterns and security-sensitive constructs
- Identified confirmed security issues and security hotspots requiring manual review
- Established a baseline without modifying application code

Evidence:  evidence/sast/


---

### Dynamic Analysis (DAST)
- Deployed the application locally
- Performed a baseline, unauthenticated ZAP scan against the running service
- Identified runtime configuration and response-level weaknesses

Evidence:  evidence/dast/


---

## SAST vs DAST Comparison
A direct comparison was performed to evaluate coverage differences:

- Code-level issues (e.g., hard-coded secrets) identified only via SAST
- Runtime posture issues (e.g., missing security headers) identified only via DAST
- Limited overlap where static risks may or may not be exploitable at runtime

Comparison and reasoning:  evidence/analysis/overlap.md


---

## Key Findings (Executive View)
Two representative vulnerabilities were selected to illustrate remediation thinking:

- **SAST:** Hard-coded credential pattern detected in source code  
- **DAST:** Missing Content Security Policy (CSP) header increasing XSS exposure  

Each finding includes impact, remediation strategy, and verification approach.

See:  SECURITY_SUMMARY.md



---

## Security Engineering Takeaways
- No single testing technique provides complete coverage
- SAST excels at early detection of insecure patterns
- DAST validates runtime behavior and configuration
- Effective AppSec programs intentionally combine both

---

## Limitations
- SonarQube Community Edition uses an embedded database (lab use only)
- ZAP scan was baseline and unauthenticated
- Juice Shop is intentionally insecure and not representative of production posture

---

## Disclaimer
This project is for educational and demonstration purposes only.  
OWASP Juice Shop should never be deployed in production environments.


