# SAST vs DAST Findings Overlap – OWASP Juice Shop

## SAST Summary (SonarQube)
- Security issues: 10
- Security hotspots: 45
- Example findings:
  - Hard-coded password (typescript:S2068)
  - Angular sanitization bypass risk (typescript:S6268)

## DAST Summary (OWASP ZAP)
- Medium findings: 2
- Low/Informational findings: 10
- Example findings:
  - Content Security Policy (CSP) header not set
  - Cross-domain misconfiguration

---

## Overlap Analysis

| Category | SAST | DAST | Explanation |
|--------|------|------|-------------|
| Hard-coded secrets | ✅ | ❌ | Code-level issue not directly observable at runtime |
| Sanitization / XSS risk | ✅ | ⚠️ | Identified statically; runtime exploitability depends on reachability |
| Missing security headers | ❌ | ✅ | Runtime HTTP posture, not detectable via static code analysis |
| CORS / cross-domain issues | ❌ | ✅ | Configuration-level behavior observed at runtime |

---

## Key Takeaways
- SAST is effective at identifying insecure coding patterns early.
- DAST validates runtime configuration and client-facing controls.
- Not all SAST findings will surface during DAST without specific execution paths.
- Combining both provides more complete coverage than either alone.

