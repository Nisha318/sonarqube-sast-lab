# Security Summary – OWASP Juice Shop SAST & DAST Lab

## Overview
This project demonstrates a combined Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST) workflow using SonarQube and OWASP ZAP against the OWASP Juice Shop application. The objective is to identify code-level and runtime security risks and explain practical remediation and verification strategies.

The application is intentionally vulnerable and was not modified as part of this assessment.

---

## Top Vulnerability #1 (SAST)

**Title:** Hard-coded Password Detected  
**Tool:** SonarQube  
**Rule:** typescript:S2068  
**Category:** Authentication

### Why this matters
Hard-coded credentials significantly increase the risk of credential disclosure and reuse. If source code is exposed through repository access, leaks, or supply chain compromise, embedded secrets can be harvested and abused across environments.

### Recommended remediation
- Remove all secrets from source code
- Use environment variables or a centralized secrets manager
- Rotate any exposed credentials
- Add automated secret scanning to the CI pipeline

### How to verify the fix
- Re-run SonarQube to confirm the hotspot is resolved
- Validate that no secrets remain in the repository or build artifacts

---

## Top Vulnerability #2 (DAST)

**Title:** Content Security Policy (CSP) Header Not Set  
**Tool:** OWASP ZAP  
**Risk Level:** Medium  
**CWE:** 693

### Why this matters
Without a Content Security Policy, the application is more susceptible to client-side attacks such as Cross-Site Scripting (XSS). CSP provides an additional defensive layer by restricting which sources are permitted to execute scripts and load content.

### Recommended remediation
- Implement a strict `Content-Security-Policy` header
- Restrict script, style, and frame sources to trusted origins
- Deploy CSP in report-only mode initially to validate behavior before enforcement

### How to verify the fix
- Re-run OWASP ZAP and confirm the alert is resolved
- Validate response headers using browser developer tools or curl

---

## Why SAST and DAST Findings Differ
- SAST identifies insecure coding patterns regardless of runtime reachability
- DAST identifies vulnerabilities and misconfigurations observable at runtime
- Using both techniques provides broader coverage than either approach alone

This assessment highlights why security findings do not always overlap and why multiple testing methods are required to understand overall risk.

---

## Phase 2 – CI/CD Integration and Security Gating

In Phase 2, the assessment was extended to demonstrate how application security testing is integrated into a continuous integration (CI) workflow, reflecting real-world cloud and DevSecOps practices.

SAST and DAST were automated using a GitHub Actions pipeline. SAST is executed using SonarQube to provide visibility into code-level risks and security hotspots early in the development lifecycle. These results are summarized for awareness and trend tracking but are not enforced as blocking conditions due to the intentionally vulnerable nature of the application.

DAST is performed against a running, containerized instance of the application using an OWASP ZAP baseline scan. A high-signal security gate was introduced to fail the pipeline only when **HIGH-severity runtime findings** are detected. WARN-level findings are permitted to pass, preserving developer velocity while still enforcing meaningful security controls.


Pipeline artifacts, including DAST reports and SonarQube scan metadata, are preserved for triage and verification. A clear security gate decision is published with each run to make pass or fail rationale explicit.


This phase demonstrates how application security evolves from point-in-time testing to repeatable, automated enforcement, supporting secure SDLC practices and software supply chain security prior to deployment.

---

## NIST SP 800-53 Rev. 5 Alignment (Selected Controls)

This project demonstrates activities that align with selected NIST SP 800-53 Rev. 5 control objectives. The mapping below is illustrative and does not represent full system compliance.

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