# SAST & DAST Security Assessment – OWASP Juice Shop

![SonarQube](https://img.shields.io/badge/SAST-SonarQube-informational)
![OWASP ZAP](https://img.shields.io/badge/DAST-OWASP%20ZAP-informational)
![Docker](https://img.shields.io/badge/Platform-Docker-blue)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## Summary
This project demonstrates a practical **application security assessment workflow** that combines static analysis (SAST) and dynamic analysis (DAST) to evaluate the OWASP Juice Shop application across both code-level and runtime attack surfaces.

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
- **Docker** – Containerized execution for local and CI environments
- **GitHub Actions** – CI/CD automation for SAST and DAST (Phase 2)

---

![Phase 2 Flow Diagram](assets/phase2-diagram.png)

---
## Assessment Approach


### Static Analysis (SAST)
- Analyzed application source code for insecure patterns and security-sensitive constructs
- Identified confirmed security issues and security hotspots requiring manual review
- Established a baseline without modifying application code

**Evidence:**  
SAST findings are summarized in `SECURITY_SUMMARY.md`.  
Raw scan metadata is generated during CI execution and preserved as pipeline artifacts.

---

### Dynamic Analysis (DAST)
- Deployed the application in a containerized environment
- Performed a baseline, unauthenticated ZAP scan against the running service
- Identified runtime configuration and response-level weaknesses

**Evidence:**  
DAST reports are generated during CI execution and preserved as GitHub Actions artifacts.

---

## SAST vs DAST Comparison
A direct comparison was performed to evaluate coverage differences:

- Code-level issues (e.g., hard-coded secrets) identified only via SAST
- Runtime posture issues (e.g., missing security headers) identified only via DAST
- Limited overlap where static risks may or may not be exploitable at runtime

**Comparison and reasoning:**  
`evidence/analysis/overlap.md`

---

## Key Findings (Executive View)
Two representative vulnerabilities were selected to illustrate remediation thinking:

- **SAST:** Hard-coded credential pattern detected in source code  
- **DAST:** Missing Content Security Policy (CSP) header increasing XSS exposure  

Each finding includes impact, remediation strategy, and verification approach.

**See:**  
`SECURITY_SUMMARY.md`

---

## CI Evidence

This project includes a fully automated GitHub Actions pipeline that:
- Runs SAST with SonarQube
- Runs DAST with OWASP ZAP
- Applies a high-severity security gate based on DAST results
- Publishes security summaries and preserves scan artifacts for triage

Screenshots of successful pipeline execution are included in `/screenshots`.

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
